import os
from datetime import datetime
import numpy as np
from zaber_motion.ascii import Connection
from zaber_motion import Units
import time
import win32com.client
import pythoncom
import logging
from enum import Enum
import sys

# Setup logging for Horiba CCD and stage operations
logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")
logger.addHandler(logging.StreamHandler(sys.stdout))


# Horiba CCD constants
class jyCCDDataType(Enum):
    JYMCD_ACQ_FORMAT_BURST = 3
    JYMCD_ACQ_FORMAT_CROP = 2
    JYMCD_ACQ_FORMAT_IMAGE = 0
    JYMCD_ACQ_FORMAT_SCAN = 1


class jyADCType(Enum):
    JY_ADC_14_BIT = 1
    JY_ADC_16_BIT = 0
    JY_ADC_18_BIT = 2


# Horiba CCD class
class horiba_ccd:
    def __init__(self, debug=True):
        self.debug = debug
        self.jy_ccd = None
        self.flip_horizontal = True
        if self.debug: logger.debug("Loading the Synergy CCD Interface")
        try:
            self.jy_config_brower = win32com.client.Dispatch("JYConfigBrowserComponent.JYConfigBrowerInterface.1")
        except Exception as err:
            if self.debug: logger.debug(f"Error loading COM objects for Synergy library: {str(err)}")
            raise Exception("Unable to load COM objects for Synergy Library: " + str(err))

        # Retrieve all device IDs
        self.device_list = []
        try:
            devID, devName = self.jy_config_brower.GetFirstCCD()
            while devID != "" and devName != "":
                self.device_list.append((devID, devName))
                devID, devName = self.jy_config_brower.GetNextCCD()

            if self.debug: logger.debug("Loading CCDs from the Horiba config browser")
            if len(self.device_list) == 0:
                raise Exception(
                    "No valid CCD loaded from the Horiba configuration browser. Check installation and configuration.")
            if self.debug:
                s = ""
                for d in self.device_list:
                    if len(s): s += ", "
                    s += f"({d[0]}, {d[1]})"
                logger.debug("Found the following CCDs: " + s)
        except Exception as err:
            raise Exception("Unable to load a valid CCD from the configuration manager: " + str(err))

    def open_camera(self, dev_id="CCD1"):
        self.dev_id = dev_id
        try:
            self.jy_ccd = win32com.client.Dispatch("JYCCD.JYMCD.1")
        except Exception as err:
            if self.debug: logger.debug(f"Error loading COM object for CCD from Synergy library: {str(err)}")
            self.jy_ccd = None
            raise Exception("Unable to load COM objects for Synergy Library: " + str(err))

        ccd = self.jy_ccd
        try:
            ccd.Uniqueid = self.dev_id
            ccd.Load()
            time.sleep(2)  # Delay after loading to stabilize
        except Exception as err:
            raise Exception(f"Unable to load device {dev_id}: {str(err)}")

        try:
            ccd.OpenCommunications()
            time.sleep(2)  # Delay after opening communications
        except Exception as err:
            raise Exception("Unable to open communications with CCD: " + str(err))

        try:
            self.initialize()
        except Exception as err:
            raise Exception("Unable to initialize: " + str(err))

        return True

    def initialize(self):
        ccd = self.jy_ccd
        try:
            ccd.Initialize(True, False)
            time.sleep(1)  # Delay after initialization
        except Exception as err:
            raise Exception("Library call to Initialize function failed: " + str(err))

        # Hard-coded ADC and gain settings
        self.adc_settings = [
            (jyADCType.JY_ADC_16_BIT.value, "45 kHz"),
            (jyADCType.JY_ADC_14_BIT.value, "500 kHz"),
            (jyADCType.JY_ADC_18_BIT.value, "500 kHz Ultra"),
            (127, "500 kHz Wrap")
        ]
        self.gain_settings = [
            (0, "High Limit"),
            (1, "Best Dynamic Range"),
            (2, "High Sensitivity")
        ]

        sen_size = ccd.GetChipSize()
        self.sensor_width = sen_size[0]
        self.sensor_height = sen_size[1]

        self.set_acquisition_mode("fvb", False)  # Using "fvb" for spectrum mode as in your test code
        self.set_ccd_roi(1, 2048, 1, 100, 1, 100, False)
        self.set_integration_time(2)  # Adjust this value as needed
        self.set_adc(self.adc_settings[0][0])
        self.set_gain(self.gain_settings[0][0])
        self.update_acq_settings_on_ccd()

    def set_acquisition_mode(self, mode, update_ccd=True):
        if mode == "fvb":
            self.jy_acq_mode = jyCCDDataType.JYMCD_ACQ_FORMAT_SCAN.value
        self.acq_mode = mode
        if update_ccd:
            self.update_acq_settings_on_ccd()
        return True

    def set_ccd_roi(self, start_x, width, start_y, height, bin_x=1, bin_y=1, update_ccd=True):
        self.roi_start_x = start_x
        self.roi_start_y = start_y
        self.roi_width = width
        self.roi_height = height
        self.bin_size_x = bin_x
        self.bin_size_y = bin_y
        if update_ccd:
            self.update_acq_settings_on_ccd()
        return True

    def update_acq_settings_on_ccd(self):
        ccd = self.jy_ccd
        try:
            ccd.DefineAcquisitionFormat(self.jy_acq_mode, 1)
            if self.acq_mode == "fvb":
                ccd.DefineArea(1, 1, 1, 2048, 100, 1, 100)
                self.readout_row_count = 1
                self.readout_col_count = int(self.roi_width / self.bin_size_x)
                self.readout_transpose = False
            time.sleep(1)  # Delay after updating settings
        except Exception as err:
            if self.debug: logger.debug(f"Failed to update the acquisition settings: {str(err)}")
            return False
        return True

    def set_integration_time(self, int_time):
        self.jy_ccd.IntegrationTime = int_time

    def set_adc(self, adc_setting):
        found = False
        for adc in self.adc_settings:
            if adc[0] == adc_setting:
                found = True
                break
        if found:
            self.jy_ccd.SelectAdc(adc_setting)
        else:
            raise ValueError(f"Invalid ADC setting: {adc_setting}")
        return True

    def set_gain(self, gain_setting):
        found = False
        for gain in self.gain_settings:
            if gain[0] == gain_setting:
                found = True
                break
        if found:
            self.jy_ccd.Gain = gain_setting
        else:
            raise ValueError("Invalid gain setting")
        return True

    def start_acquisition(self, open_shutter=True):
        try:
            self.jy_ccd.StartAcquisition(open_shutter)
            time.sleep(1)  # Delay after starting acquisition
        except Exception as err:
            raise Exception(f"Failed to start acquisition: {str(err)}")
        return True

    def get_acquisition_busy(self):
        return bool(self.jy_ccd.AcquisitionBusy())

    def get_acquired_data(self):
        if self.debug: logger.debug("Fetching acquired data")
        result = self.jy_ccd.GetResult()
        num_data_obj = int(result.DataObjectCount)
        if num_data_obj == 0:
            raise Exception("No data object to load")
        elif num_data_obj > 1:
            raise NotImplementedError("More than one data object in result collection. Not implemented.")
        data = result.GetFirstDataObject()
        data_array = data.GetDataAsArray()
        buffer = np.empty((1, self.readout_col_count))
        buffer[0, :] = np.array(data_array)
        if self.flip_horizontal:
            buffer = buffer[:, -1::-1]
        return buffer

    def close_camera(self):
        try:
            self.jy_ccd.CloseCommunications()
            time.sleep(1)  # Delay after closing communications
        except Exception as err:
            if self.debug: logger.debug(f"Error closing communications: {str(err)}")
        finally:
            self.jy_ccd = None

    def __del__(self):
        try:
            if self.jy_ccd is not None:
                self.close_camera()
        except Exception as err:
            if self.debug: logger.debug(f"Destructor error: {str(err)}")
        finally:
            self.jy_ccd = None


# Stage control global variables
move_units = Units.LENGTH_MILLIMETRES
disp_units = Units.LENGTH_MILLIMETRES
hor_dis = 1  # Reduced for testing
hor_step = 0.5  # mm
ver_dis = 1  # Reduced for testing
ver_step = 0.5  # mm
hor_home = 0
ver_home = 0
sleep_time = 2.0  # Increased delay to prevent resource contention


def main():
    x = datetime.now()

    # For Windows
    folder_dat = os.path.join(
        'C:\\Users\\sudee\\Box\\My Box\\Python_Code',
        str(x.strftime("20%y_%m_%d"))
    )

    # For macOS (comment out for Windows)
    # folder_dat = os.path.join(
    #     "/Users/hnakamur/Box Sync/Nakamura_Lab/Users/Sudeep/Projects/Test_Results/CCD_and_Stage/2025_03_05",
    #     x.strftime("20%y_%m_%d")
    # )

    os.makedirs(folder_dat, exist_ok=True)

    file_name = "stage_movement_" + x.strftime("20%y_%m_%d_%H%M%S") + ".txt"
    filepath = os.path.join(folder_dat, file_name)

    # Initialize COM for the main thread
    pythoncom.CoInitialize()

    try:
        with open(filepath, "a+") as data_file:
            data_file.write("Hor-psn\tVer-psn\tIntensity\n")

            with Connection.open_serial_port("COM5") as connection:  # For Windows
                # For macOS, use: with Connection.open_serial_port("/dev/tty.usbserial-A10NRIS6") as connection:
                device_list = connection.detect_devices()
                if len(device_list) < 2:
                    print("Error: Less than 2 devices found.")
                    return

                deviceX = device_list[0]
                deviceT = device_list[1]
                axisX = deviceX.get_axis(1)
                axisT = deviceT.get_axis(1)

                print("Homing Devices")
                axisX.move_absolute(hor_home, move_units)
                axisT.move_absolute(ver_home, move_units)
                time.sleep(3)  # Increased delay after homing to stabilize

                # Initialize Horiba CCD
                ccd = horiba_ccd()
                ccd.open_camera("CCD2")
                print("Camera opened")

                arr_x = int(hor_dis / hor_step)
                arr_y = int(ver_dis / ver_step)
                X_coor = np.zeros((arr_y, arr_x))
                T_coor = np.zeros((arr_y, arr_x))

                for i in range(int(ver_dis / ver_step)):
                    position_T = axisT.get_position(move_units)
                    axisX.move_absolute(hor_home, move_units)
                    print(f"Vertical position: {position_T}, Horizontal returned to home")
                    time.sleep(2)  # Delay to ensure stable positioning

                    for j in range(int(hor_dis / hor_step)):
                        position_X = axisX.get_position(move_units)
                        X_coor[i, j] = position_X
                        T_coor[i, j] = position_T

                        # Capture intensity from CCD with added delay and error handling
                        try:
                            ccd.start_acquisition(True)
                            while ccd.get_acquisition_busy():
                                time.sleep(1)  # Increased delay during acquisition
                            buffer = ccd.get_acquired_data()
                            syn_data = buffer[0]
                            first_500 = syn_data[:500]
                            avg_500 = sum(first_500) / 500 if first_500 else 0
                            syn_data = [x - avg_500 for x in syn_data]
                            intensity = max(syn_data) if syn_data else 0  # Use max intensity as the metric
                        except Exception as e:
                            print(f"Error during CCD acquisition: {e}")
                            intensity = 0  # Default value in case of failure

                        # Write to file
                        data_file.write(f"{position_X}\t{position_T}\t{intensity}\n")
                        print(f"X: {position_X}, T: {position_T}, Intensity: {intensity}")

                        axisX.move_relative(hor_step, move_units)
                        time.sleep(sleep_time)  # Delay to prevent rapid movements

                    axisT.move_relative(ver_step, move_units)
                    time.sleep(2)  # Delay after vertical movement

        print("Closing camera")
        ccd.close_camera()

    except Exception as e:
        print(f"Error in main execution: {e}")

    finally:
        # Uninitialize COM for the main thread
        pythoncom.CoUninitialize()


if __name__ == "__main__":
    main()