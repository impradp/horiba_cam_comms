# Python interface to the Horiba CCDs via the Synergy SDK
# Copyright (C) 2022  Nick Borys

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import win32com.client
import numpy as np
import time

from threading import Lock
import logging
from enum import Enum
import sys

logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")
logger.addHandler(logging.StreamHandler(sys.stdout))

# Constants 
class jyCCDDataType(Enum):
    JYMCD_ACQ_FORMAT_BURST  = 3          # from enum jyCCDDataType
    JYMCD_ACQ_FORMAT_CROP   = 2          # from enum jyCCDDataType
    JYMCD_ACQ_FORMAT_IMAGE  = 0          # from enum jyCCDDataType
    JYMCD_ACQ_FORMAT_SCAN   = 1          # from enum jyCCDDataType
    
class jyADCType(Enum):
    JY_ADC_14_BIT           =1          # from enum jyADCType
    JY_ADC_16_BIT           =0          # from enum jyADCType
    JY_ADC_18_BIT           =2          # from enum jyADCType


class horiba_ccd(object):
    
    def __init__(self, debug=True):
        
        self.debug = True
        self.Lock = Lock()
        
        if self.debug: logger.debug("Loading the Synergy CCD Interface")
        
        # Attempt to load the COM objects
        try:
            jyb = self.jy_config_brower = win32com.client.Dispatch("JYConfigBrowserComponent.JYConfigBrowerInterface.1")
        except Exception as err:
            if self.debug:  logger.debug("Error loading COM objects for Synergy library: " + str(err))
            raise Exception("Unable to load COM objects for Synergy Library" + str.err)
        
        
        # Retrieve all device IDs so that we can perform a check when a connection is attempts
        self.device_list = []
        try:
            devID, devName = jyb.GetFirstCCD()
            while devID != "" and devName != "":
                self.device_list.append((devID, devName))
                devID, devName = jyb.GetNextCCD()
            
            if self.debug: logger.debug("Loading CCDs from the Horiba config browser")
            
            if len(self.device_list) ==0:
                raise Exception("A valid CCD was not loaded from the Horiba configuration browser. Check that a CCD is installed and the configuration mangers was ran correctly")
            
            if self.debug:
                s = ""
                for d in self.device_list:
                    if len(s): s += ", "
                    s+= "(" + d[0]+ ", " + d[1] + ")"
                logger.debug("Found the following CCDs: " + s)
        except Exception as err:
            raise Exception("Unable to load a valid CCD from the configuration manager: " + str(err))
        
        # Initalize CCD object to None
        self.jy_ccd = None
        
        self.flip_horizontal = True
        
    
    def open_camera(self, dev_id = "CCD1"):
        self.dev_id = dev_id
        
        # Attempt to load the COM objects
        try:
            self.jy_ccd = win32com.client.Dispatch("JYCCD.JYMCD.1")
        except Exception as err:
            if self.debug:  logger.debug("Error loading COM object for CCD from Synergy library: " + str(err))
            self.jy_ccd = None
            raise Exception("Unable to load COM objects for Synergy Library" + str.err)
        
        #Just a shorter name
        ccd = self.jy_ccd
        
        try:
            ccd.Uniqueid = self.dev_id
            ccd.Load()
        except Exception as err: 
            raise Exception("Unable to load device {0:s}: {1:s}".format(dev_id, str(err)))
        
        # Open communication with the CCD
        try: 
            ccd.OpenCommunications()
        except Exception as err:
            raise Exception("Unable to open communications with CCD: " + str(err))
        
        try:
            self.initialize()
        except Exception as err:
            raise Exception("Unable to initialize:  " + str(err))
        
        return True
    
    def initialize(self):
        #Just a shorter name
        ccd = self.jy_ccd
               
        # Initialize the CCD
        try:
            ccd.Initialize(True, False  )
        except Exception as err:
            raise Exception("Library call to Initial function failed: " + str(err))
        
        
        #### Collect information about the CCD ####
        try:
            # ADC settings
                        
            if 0:
                # Attempt to load from the SDK
                # Presently, this functionality of the SDK is not working.
                self.adc_settings = []
                adc = ccd.GetFirstADC()
                if adc[0] == -1:
                    # No ADC options
                    self.adc_settings.append((-1, "Default"))
                else:
                    while adc[0] != -1:
                        self.adc_settings.append(adc)
                        adc = ccd.GetNextADC()
            else:
                #Hard coded values
                self.adc_settings = []
                self.adc_settings.append((jyADCType.JY_ADC_16_BIT.value, "45 kHz"))
                self.adc_settings.append((jyADCType.JY_ADC_14_BIT.value, "500 kHz"))
                self.adc_settings.append((jyADCType.JY_ADC_18_BIT.value, "500 kHz Ultra"))
                self.adc_settings.append((127, "500 kHz Wrap"))
                           
            # Gain settings
            gain = ccd.GetFirstGain()
            
            if 0:
                # Attempt to load from the SDK
                # Presently, this functionality of the SDK is not working.
                self.gain_settings = []
                if gain[0] == -1:
                    # No ADC options
                    self.gain_settings.append((-1, "Default"))
                else:
                    while gain[0] != -1:
                        self.gain_settings.append(gain)
                        gain = ccd.GetNextGain()
            else:
                #Hard coded values
                self.gain_settings =[]
                self.gain_settings.append((0, "High Limit"))
                self.gain_settings.append((1, "Best Dynamic Range"))
                self.gain_settings.append((2, "High Sensitivity"))
            
            
            # Sensor width and height
            sen_size = ccd.GetChipSize()
            self.sensor_width = sen_size[0]
            self.sensor_height = sen_size[1]
            
            # Fetch units
            # Todo: temperature
            # Todo: integration time
        
        except Exception as err:
            raise Exception("Error fetching device information: " + str(err))
            
        # Initialize the device
        self.get_temperature()
        self.get_temperature_setpoint()
        self.set_acquisition_mode("image", False)
        self.set_ccd_roi(1, self.sensor_width, 1, self.sensor_height, 1, 1, False)
        self.set_integration_time(1)
        self.get_integration_time()
        self.set_hflip(True)
        
        if self.adc_settings[0][0]!=-1:
            self.set_adc(self.adc_settings[0][0])
            self.get_adc()
            
        if self.gain_settings[0][0]!=-1:
            self.set_gain(self.gain_settings[0][0])
            self.get_gain()
        
        self.update_acq_settings_on_ccd()
        
        return True
    
    def set_hflip(self, hflip):
        self.flip_horizontal = hflip
        return True
    
    def get_hflip(self):
        return self.flip_horizontal
    
    def set_adc(self, adc_setting):
        found = False
        for adc in self.adc_settings:
            if adc[0] == adc_setting:
                found = True
                break
            
        if found:
            self.jy_ccd.SelectAdc(adc_setting)
        else:
            raise ValueError("Invalid ADC setting: {0}".format(adc_setting))
        
        return True
    
    def get_adc(self):
        return self.jy_ccd.CurrentADC
    
    
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
    
    def get_gain(self):
        return self.jy_ccd.Gain
    
    def get_temperature(self):
        self.temperature = float(self.jy_ccd.CurrentTemperature)
        return self.temperature
    
    def get_temperature_setpoint(self):
        self.temperature_setpoint = float(self.jy_ccd.TemperatureSetPoint)
        return self.temperature_setpoint
    
    def set_temperature_setpoint(self, temperature):
        self.jy_ccd.TemperatureSetPoint = temperature
        return True
    
    def get_integration_time(self):
        self.int_time = float(self.jy_ccd.IntegrationTime)
        return self.int_time 
    
    def set_integration_time(self, int_time):
        self.jy_ccd.IntegrationTime = int_time
        
    def set_acquisition_mode(self, mode, update_ccd = True):
        
        if mode == "image":
            #Image readout
            self.jy_acq_mode = jyCCDDataType.JYMCD_ACQ_FORMAT_IMAGE.value
        elif mode == "single_track":
            #Spectrum readout from limited area of the chip
            self.jy_acq_mode = jyCCDDataType.JYMCD_ACQ_FORMAT_SCAN.value
        elif mode == "fvb":
            #Spectrum readout from entire chip with full vertical binning
            self.jy_acq_mode = jyCCDDataType.JYMCD_ACQ_FORMAT_SCAN.value
        else:
            raise Exception("Invalid acquisition mode")
        
        self.acq_mode = mode
        
        if update_ccd:
            self.update_acq_settings_on_ccd()
        
        return True
    
    def get_acquisition_mode(self):
        return self.acq_mode
    
    def get_x_bin(self):
        return self.bin_size_x
    
    def set_ccd_roi(self, start_x, width, start_y, height, bin_x=1, bin_y=1, update_ccd=True):#update_ccd changed from False
                       
        self.roi_start_x = start_x
        self.roi_start_y = start_y
        self.roi_width = width
        self.roi_height = height
        self.bin_size_x = bin_x
        self.bin_size_y = bin_y  
       
        if update_ccd:
            self.update_acq_settings_on_ccd()
        
        return True
    
    def check_roi(self, raise_err = True):
        if self.roi_start_x < 1:
            if raise_err: raise Exception("Invalid ROI: bin_start_x out of bounds")
            return False
        if (self.roi_start_x + self.roi_width) > self.sensor_width+1:
            if raise_err: raise Exception("Invalid ROI: bin_width out of bounds")
            return False
        if self.roi_start_y < 1:
            if raise_err: raise Exception("Invalid ROI: bin_start_y out of bounds")
            return False
        if (self.roi_start_y + self.roi_height) > self.sensor_height+1:
            if raise_err: raise Exception("Invalid ROI: bin_height out of bounds")
            return False
        
        if self.roi_width % self.bin_size_x != 0:
            raise Exception("Invalid x binning: binning leaves fractional pixels in ROI")
        
        if self.roi_height % self.bin_size_y != 0:
            raise Exception("Invalid y binning: binning leaves fractional pixels in ROI")
        
    
    def update_acq_settings_on_ccd(self):
        ccd = self.jy_ccd
        
        try:
            
            # Set the acquisition format first (this is set by the set_acquisition_mode function)
            ccd.DefineAcquisitionFormat(self.jy_acq_mode, 1)
            
            if self.acq_mode == "image":
                self.check_roi(True)
                ccd.DefineArea(1,
                               self.roi_start_x,
                               self.roi_start_y,
                               self.roi_width, 
                               self.roi_height,
                               self.bin_size_x,
                               self.bin_size_y)
                
                self.readout_row_count = int(self.roi_height/self.bin_size_y)
                self.readout_col_count = int(self.roi_width/self.bin_size_x)
                self.readout_transpose = True
                
            elif self.acq_mode == "single_track":
                self.check_roi(True)
                ccd.DefineArea(1,
                               self.roi_start_x,
                               self.roi_start_y,
                               self.roi_width, 
                               self.roi_height,
                               self.bin_size_x,
                               self.roi_height)
                self.readout_row_count = 1
                self.readout_col_count = int(self.roi_width/self.bin_size_x)
                self.readout_transpose = False
            
            elif self.acq_mode == "fvb":
                ccd.DefineArea(1,
                               1,
                               1,
                               2048,#self.sensor_width, 
                               100,#self.sensor_height,
                               1,
                               100)#self.sensor_height)
                self.readout_row_count = 1
                self.readout_col_count = int(self.roi_width/self.bin_size_x)
                self.readout_transpose = False
                
            else:
                raise Exception("Invalid acquisition mode")
        
        except Exception as err:
            if self.debug: logger.debug("Failed to update the acquisition settings: " + str(err))
            return False
        
        return True
    
    def get_data_size(self):
        self.data_size = int(self.jy_ccd.DataSize)
        return self.data_size
    
    def get_acquisition_ready(self):
        self.acq_ready = self.jy_ccd.ReadyForAcquisition
        return self.acq_ready

    ##### Acquisition control #####
    #@TODO:  consider threading issues like Andor interface.
    
    def start_acquisition(self, open_shutter=True):
        self.jy_ccd.StartAcquisition(open_shutter)
        return True
        
    def get_acquisition_busy(self):
        busy = bool(self.jy_ccd.AcquisitionBusy())
        return busy
    
    def abort_acquisition(self):
        self.jy_ccd.AbortAcquisition()
        
    def get_acquired_data(self):
        if self.debug: logger.debug("Fetching acquired data")
        
        ccd = self.jy_ccd
        
        # Get the collection of results
        result = ccd.GetResult()
        num_data_obj = int(result.DataObjectCount)
        
        if self.debug: logger.debug("Data object count in Result object: " + str(num_data_obj))
        
        # Expecting only one data object;  if there are more, Raise an error
        if num_data_obj == 0:
            raise Exception("No data object to load")
        elif num_data_obj > 1:
            raise NotImplementedError("More than one data object in result collection.  Not implemented.")
        
        data = result.GetFirstDataObject()
        data_array = data.GetDataAsArray()
        
        if self.readout_transpose:
            self.buffer = np.transpose(np.array(data_array))
        else:
            self.buffer = np.empty((1,self.readout_col_count))
            self.buffer[0,:] = np.array(data_array)
            
        if self.flip_horizontal:
            self.buffer = self.buffer[:,-1::-1]
            
        #print(self.buffer.shape)
        #self.buffer_rows = self.buffer.shape[0]
        #self.buffer_cols = self.buffer.shape[1]
        
        #Explicilty set returned COM objects to None to make sure they unload from memory
        data_array = None 
        data = None
        result = None
        
        return self.buffer
        

    def close_camera(self):
        try:
            self.jy_ccd.CloseCommunications()
        except Exception as err:
            if self.debug: logger.debug("Error closing communications " + str(err))
        finally:
            self.jy_ccd = None
    
    def __del__(self):
        try:
            if self.jy_ccd != None:
                self.close_camera()
        except Exception as err:
            if self.debug: logger.debug("Destructor error " + str(err))
        finally:
            self.jy_ccd = None
    
    def dump_settings(self):
        print("Sensor width", self.sensor_width)
        print("Sensor height", self.sensor_height)
        print("Temperature", self.get_temperature())
        print("ADC settings")
        for adc in self.adc_settings:
            print("", adc[0], adc[1])
        print("Gain settings")
        for gain in self.gain_settings:
            print("", gain[0], gain[1])
            
        print("---- Acquisition Settings ----")
        print("Integration time", self.get_integration_time())
        print("Acquition mode", self.get_acquisition_mode(), self.jy_acq_mode)
        print("ROI X", self.roi_start_x)
        print("ROI Y", self.roi_start_y)
        print("ROI Width", self.roi_width)
        print("ROI Height", self.roi_height)
        print("Binning X", self.bin_size_x)
        print("Binning Y", self.bin_size_y)
        print("Datasize", self.get_data_size())
        print("Acq Ready", self.get_acquisition_ready())
        print("Gain", self.get_gain())
        print("ADC", self.get_adc())
    
        
#### Test code ####
if __name__ == '__main__':
    from matplotlib import pyplot as plt
    
    syn = horiba_ccd()
    syn.open_camera("CCD2")
    print("Camera opened")
    
    syn.set_integration_time(0.1)
    
    fmode = "spec" # "image or "spec"
    
    if fmode=="image":
        syn.set_acquisition_mode("image", True)
    elif fmode == "spec":
        syn.set_acquisition_mode("fvb", True)
    
    syn.dump_settings()
    
    for i in range(3):
        print("Running acquisition:", i)
        syn.set_adc(i)
        syn.update_acq_settings_on_ccd()
        syn.start_acquisition(True)
        
        # Wait for acquisition to complete
        i1 = 0      
        stop_at = 100
        while syn.get_acquisition_busy():
            if i1 % 10 == 0: print("Waiting for acquisition to complete...")
            time.sleep(0.1)
            i1+=1
            if i1>stop_at: break
        
        if i1 >stop_at:
            print("Acquisition failed")
            syn.abort_acquisition()
            break
        else:
            print("Acquisition complete")
        
        buffer = syn.get_acquired_data()
        if fmode == "image": 
            plt.figure()
            plt.imshow(buffer, aspect='auto', cmap='viridis', interpolation='None')
            cb = plt.colorbar()
            plt.show()
        elif fmode == "spec":
            plt.figure()
            plt.plot(buffer)
            plt.show()
    
    time.sleep(1)
    
    print("Closing camera")
    syn.close_camera()
        
        
        
    