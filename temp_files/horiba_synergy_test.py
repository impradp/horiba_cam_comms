#from .horiba_ccd import JYMCD
#from .horiba_config_man import JYConfigBrowerInterface
from horiba_system_lib import constants as JYConstants

from matplotlib import pyplot as plt
import numpy as np

import win32com.client
from ctypes.test.test_pickling import name
from pickle import NONE

jyc = JYConstants()

import time

jyb = win32com.client.Dispatch("JYConfigBrowserComponent.JYConfigBrowerInterface.1")

print(type(jyb))

#jyb = JYConfigBrowerInterface()
ret = jyb.Load()
print("Load", ret)

devID = jyb.GetFirstCCD()
while (devID[0]!="" and devID[1] != ""):

    print("Device ID", type(devID), devID)
    devID = jyb.GetNextCCD()

jyCCD = win32com.client.Dispatch("JYCCD.JYMCD.1")
jyCCD.Uniqueid = 'CCD2'
jyCCD.Load()

print("Loading complete")
print("Chip Description", jyCCD.ChipDescription)

jyCCD.OpenCommunications()

print("Communications opened")
time.sleep(2)

print("Current ADC", jyCCD.CurrentADC)

print("Initializing...")
jyCCD.Initialize()

while not jyCCD.InitializeComplete:
    time.sleep(0.05)
    print("Waiting for initialize to complete..")
    
print("Initialize Complete")

print("Fetching ADCs")
adc = jyCCD.GetFirstADC()
print("First ADC", adc)
#while adc[0]!="":
#    print("ADC", adc)
#    adc = jyCCD.GetNextADC()
#    break

#units = jyCCD.GetDefaultUnits()
#print("Units", units)
print("Fetching gains")
gain = jyCCD.GetFirstGain()
print("First gain", gain)

print("Current Temperature", jyCCD.CurrentTemperature)
print("Temperature Setpoint", jyCCD.TemperatureSetPoint)
print("Integration Time Before", jyCCD.IntegrationTime)
jyCCD.IntegrationTime = 0.2
print("Integration Time After", jyCCD.IntegrationTime)

#Get detector width
size = jyCCD.GetChipSize()
print("Chip size", size)

jyCCD.DefineAcquisitionFormat(jyc.JYMCD_ACQ_FORMAT_IMAGE, 1)
jyCCD.DefineArea(1, 1,1,2048,70, 1, 1)
print("Datasize", jyCCD.DataSize)
print("Acquisition Count", jyCCD.AcquisitionCount)


print("Ready for acquisition", jyCCD.ReadyForAcquisition)




print("Starting an acquistion")
jyCCD.StartAcquisition(True)

i = 0
stop_at = 100
while(jyCCD.AcquisitionBusy()):
    print("Waiting for acquisition to complete...")
    time.sleep(0.1)
    i+=1
    if i>stop_at: break

if i >stop_at:
    print("Acquisition failed")
    jyCCD.AbortAcquisition()
else:
    print("Acquisition complete")


print("Fetching result...")
data = jyCCD.GetResult()
print("Data", data)
print("Data object count", data.DataObjectCount)

data_obj = data.GetFirstDataObject()
data_array = data_obj.GetDataAsArray()

print("Data Object ", data_obj)
print("Data Array", type(data_array))


print("Plotting")
plt.figure()
img = np.transpose(np.array(data_array))
data_array = None
data_obj = None
data=None
print("Shape", img.shape)
plt.imshow(img, aspect='auto', cmap='viridis', interpolation='None')
cb = plt.colorbar()
plt.show()
print("Plotting complete")


jyCCD.CloseCommunications()
print("Communications closed")
#jyCCD.Uninitialize()
#print("Device unitialized")



