import threading
import os
from datetime import datetime
import numpy as np
from zaber_motion.ascii import Connection
from zaber_motion import Units
import time
import win32com.client
from threading import Lock
import logging
from enum import Enum
import sys

# Setup logging for Horiba CCD
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

# Horiba CCD class (simplified for integration, full code assumed available)
class horiba_ccd:
    def __init__(self, debug=True):
        self.debug = debug
        self.Lock = Lock()
        self.jy_ccd = None
        self.flip_horizontal = True
        if self.debug: logger.debug("Loading the Synergy CCD Interface")
        self.jy_config_brower = win32com.client.Dispatch("JYConfigBrowserComponent.JYConfigBrowerInterface.1")
        self.device_list = []
        devID, devName = self.jy_config_brower.GetFirstCCD()
        while devID != "" and devName != "":
            self.device_list.append((devID, devName))
            devID, devName = self.jy_config_brower.GetNextCCD()

    def open_camera(self, dev_id="CCD1"):
        self.dev_id = dev_id
        self.jy_ccd = win32com.client.Dispatch("JYCCD.JYMCD.1")
        self.jy_ccd.Uniqueid = self.dev_id
        self.jy_ccd.Load()
        self.jy_ccd.OpenCommunications()
        self.initialize()
        return True

    def initialize(self):
        self.jy_ccd.Initialize(True, False)
        self.adc_settings = [(jyADCType.JY_ADC_16_BIT.value, "45 kHz"), (jyADCType.JY_ADC_14_BIT.value, "500 kHz"),
                             (jyADCType.JY_ADC_18_BIT.value, "500 kHz Ultra"), (127, "500 kHz Wrap")]
        self.gain_settings = [(0, "High Limit"), (1, "Best Dynamic Range"), (2, "High Sensitivity")]
        sen_size = self.jy_ccd.GetChipSize()
        self.sensor_width, self.sensor_height = sen_size[0], sen_size[1]
        self.set_acquisition_mode("fvb", False)
        self.set_ccd_roi(1, 2048, 1, 100, 1, 100, False)
        self.set_integration_time(2)
        self.set_adc(self.adc_settings[0][0])
        self.set_gain(self.gain_settings[0][0])
        self.update_acq_settings_on_ccd()

    def set_acquisition_mode(self, mode, update_ccd=True):
        if mode == "fvb":
            self.jy_acq_mode = jyCCDDataType.JYMCD_ACQ_FORMAT_SCAN.value
        self.acq_mode = mode
        if update_ccd:
            self.update_acq_settings_on_ccd()

    def set_ccd_roi(self, start_x, width, start_y, height, bin_x=1, bin_y=1, update_ccd=True):
        self.roi_start_x, self.roi_width, self.roi_start_y, self.roi_height = start_x, width, start_y, height
        self.bin_size_x, self.bin_size_y = bin_x, bin_y
        if update_ccd:
            self.update_acq_settings_on_ccd()

    def update_acq_settings_on_ccd(self):
        self.jy_ccd.DefineAcquisitionFormat(self.jy_acq_mode, 1)
        if self.acq_mode == "fvb":
            self.jy_ccd.DefineArea(1, 1, 1, 2048, 100, 1, 100)
            self.readout_row_count = 1
            self.readout_col_count = int(self.roi_width / self.bin_size_x)
            self.readout_transpose = False

    def set_integration_time(self, int_time):
        self.jy_ccd.IntegrationTime = int_time

    def start_acquisition(self, open_shutter=True):
        self.jy_ccd.StartAcquisition(open_shutter)

    def get_acquisition_busy(self):
        return bool(self.jy_ccd.AcquisitionBusy())

    def get_acquired_data(self):
        result = self.jy_ccd.GetResult()
        data = result.GetFirstDataObject()
        data_array = data.GetDataAsArray()
        buffer = np.empty((1, self.readout_col_count))
        buffer[0, :] = np.array(data_array)
        if self.flip_horizontal:
            buffer = buffer[:, -1::-1]
        return buffer

    def close_camera(self):
        self.jy_ccd.CloseCommunications()
        self.jy_ccd = None

# Stage control global variables
stop_flag = False
move_units = Units.LENGTH_MILLIMETRES
disp_units = Units.LENGTH_MILLIMETRES
hor_dis = 5  # mm
hor_step = 0.5  # mm
ver_dis = 5  # mm
ver_step = 0.5  # mm
hor_home = 0
ver_home = 0
sleep_time = 0  # seconds

def start_program():
    global stop_flag, X_coor, T_coor
    arr_x = int(hor_dis / hor_step)
    arr_y = int(ver_dis / ver_step)
    X_coor = np.zeros((arr_y, arr_x))
    T_coor = np.zeros((arr_y, arr_x))
    thread = threading.Thread(target=run_program)
    thread.start()

def stop_program():
    global stop_flag
    stop_flag = True
    print("Stopping program...")

def run_program():
    global stop_flag, X_coor, T_coor
    x = datetime.now()
    folder_dat = os.path.join(
        "/Users/sudeep/Library/CloudStorage/Box-Box/My Box/Python_Code",
        x.strftime("20%y_%m_%d")
    )
    os.makedirs(folder_dat, exist_ok=True)
    file_name = "stage_movement_" + x.strftime("20%y_%m_%d_%H%M%S") + ".txt"
    filepath = os.path.join(folder_dat, file_name)

    # Initialize Horiba CCD
    ccd = horiba_ccd()
    ccd.open_camera("CCD2")
    print("Camera opened")

    with open(filepath, "a+") as data_file:
        data_file.write("Hor-psn\tVer-psn\tIntensity\n")

        with Connection.open_serial_port("/dev/tty.usbserial-A10NRIS6") as connection:
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

            for i in range(int(ver_dis / ver_step)):
                if stop_flag:
                    print("Program stopped.")
                    ccd.close_camera()
                    return

                position_T = axisT.get_position(move_units)
                axisX.move_absolute(hor_home, move_units)
                print(f"Vertical position: {position_T}, Horizontal returned to home")

                for j in range(int(hor_dis / hor_step)):
                    if stop_flag:
                        print("Program stopped.")
                        ccd.close_camera()
                        return

                    position_X = axisX.get_position(move_units)
                    X_coor[i, j] = position_X
                    T_coor[i, j] = position_T

                    # Capture intensity from CCD
                    ccd.start_acquisition(True)
                    while ccd.get_acquisition_busy():
                        time.sleep(0.1)
                    buffer = ccd.get_acquired_data()
                    syn_data = buffer[0]
                    first_500 = syn_data[:500]
                    avg_500 = sum(first_500) / 500
                    syn_data = [x - avg_500 for x in syn_data]
                    intensity = max(syn_data)  # Use max intensity as the metric

                    # Write to file
                    data_file.write(f"{position_X}\t{position_T}\t{intensity}\n")
                    print(f"X: {position_X}, T: {position_T}, Intensity: {intensity}")

                    axisX.move_relative(hor_step, move_units)
                    time.sleep(sleep_time)

                axisT.move_relative(ver_step, move_units)

    print("Closing camera")
    ccd.close_camera()

if __name__ == "__main__":
    start_program()