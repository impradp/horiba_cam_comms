# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.10.4 | packaged by conda-forge | (main, Mar 30 2022, 08:38:02) [MSC v.1916 64 bit (AMD64)]
# From type library 'JYCCD.dll'
# On Fri Aug 12 15:10:53 2022
'JYCCD 1.0 Type Library'
makepy_version = '0.5.01'
python_version = 0x30a04f0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{609CF98A-3973-4250-AFC9-0F5880896BFC}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

from win32com.client import DispatchBaseClass
class IJYCCDReqd(DispatchBaseClass):
	'IJYCCDRequired Interface'
	CLSID = IID('{0D684CA0-9552-4B26-B420-2BEE5BD4F1A0}')
	coclass_clsid = IID('{4D7AAEFC-19F9-49B7-A5BB-814933694FD3}')

	def AbortAcquisition(self):
		'method AbortAcquisition'
		return self._oleobj_.InvokeTypes(219, LCID, 1, (24, 0), (),)

	def AcquisitionBusy(self):
		'method AcquisitionBusy'
		return self._oleobj_.InvokeTypes(200, LCID, 1, (11, 0), (),)

	def CalculateRangeModePositions(self, desiredBegin=defaultNamedNotOptArg, desiredEnd=defaultNamedNotOptArg, pixelOverlap=defaultNamedNotOptArg, numCovers=pythoncom.Missing
			, positions=pythoncom.Missing):
		'Method CalculateRangeModePositions'
		return self._ApplyTypes_(340, 1, (24, 0), ((5, 1), (5, 1), (3, 1), (16387, 2), (16396, 2)), 'CalculateRangeModePositions', None,desiredBegin
			, desiredEnd, pixelOverlap, numCovers, positions)

	def CanDeviceChangeAddress(self):
		'method CanDeviceChangeAddress'
		return self._oleobj_.InvokeTypes(153, LCID, 1, (11, 0), (),)

	def CheckLightPath(self, inPort=defaultNamedNotOptArg, outPort=defaultNamedNotOptArg):
		'method CheckLightPath'
		return self._oleobj_.InvokeTypes(21, LCID, 1, (11, 0), ((3, 1), (3, 1)),inPort
			, outPort)

	def CloseCommunications(self):
		'method CloseCommunications'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), (),)

	def CloseShutter(self):
		'method CloseShutter'
		return self._oleobj_.InvokeTypes(305, LCID, 1, (24, 0), (),)

	def Configure(self):
		'method Configure'
		return self._oleobj_.InvokeTypes(100, LCID, 1, (24, 0), (),)

	def DefineAcquisitionFormat(self, _MIDL__IJYCCDReqd0000_=defaultNamedNotOptArg, numAreas=defaultNamedNotOptArg):
		'method DefineAcquistionFormat'
		return self._oleobj_.InvokeTypes(301, LCID, 1, (24, 0), ((3, 1), (3, 1)),_MIDL__IJYCCDReqd0000_
			, numAreas)

	def DefineArea(self, areaNum=defaultNamedNotOptArg, xOrigin=defaultNamedNotOptArg, yOrigin=defaultNamedNotOptArg, xSize=defaultNamedNotOptArg
			, ySize=defaultNamedNotOptArg, xBin=defaultNamedNotOptArg, yBin=defaultNamedNotOptArg):
		'method DefineArea'
		return self._oleobj_.InvokeTypes(302, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1)),areaNum
			, xOrigin, yOrigin, xSize, ySize, xBin
			, yBin)

	def DeviceMemorySlotFloatRead(self, slotIndex=defaultNamedNotOptArg):
		'method DeviceMemorySlotFloatRead'
		return self._oleobj_.InvokeTypes(34, LCID, 1, (4, 0), ((3, 1),),slotIndex
			)

	def DeviceMemorySlotFloatWrite(self, slotIndex=defaultNamedNotOptArg, floatVal=defaultNamedNotOptArg):
		'method DeviceMemorySlotFloatWrite'
		return self._oleobj_.InvokeTypes(33, LCID, 1, (24, 0), ((3, 1), (4, 1)),slotIndex
			, floatVal)

	def DeviceMemorySlotStringRead(self, slotIndex=defaultNamedNotOptArg):
		'method DeviceMemorySlotStringRead'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(31, LCID, 1, (8, 0), ((3, 1),),slotIndex
			)

	def DeviceMemorySlotStringWrite(self, slotIndex=defaultNamedNotOptArg, stringToWrite=defaultNamedNotOptArg):
		'method DeviceMemorySlotStringWrite'
		return self._oleobj_.InvokeTypes(30, LCID, 1, (24, 0), ((3, 1), (8, 1)),slotIndex
			, stringToWrite)

	def DisableAllInputTriggers(self):
		'method DisableAllInputTriggers'
		return self._oleobj_.InvokeTypes(132, LCID, 1, (24, 0), (),)

	def DisableAllOutputTriggers(self):
		'method DisableAllOutputTriggers'
		return self._oleobj_.InvokeTypes(141, LCID, 1, (24, 0), (),)

	def DisableInputTrigger(self, trigAddress=defaultNamedNotOptArg, event=defaultNamedNotOptArg, sigType=defaultNamedNotOptArg):
		'method DisableInputTrigger'
		return self._oleobj_.InvokeTypes(131, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1)),trigAddress
			, event, sigType)

	def DisableOutputTrigger(self, trigAddress=defaultNamedNotOptArg, event=defaultNamedNotOptArg, sigType=defaultNamedNotOptArg):
		'method DisableOutputTrigger'
		return self._oleobj_.InvokeTypes(140, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1)),trigAddress
			, event, sigType)

	def DoAcquisition(self, ShutterOpen=defaultNamedNotOptArg):
		'method DoAcquisition'
		return self._oleobj_.InvokeTypes(318, LCID, 1, (24, 0), ((11, 1),),ShutterOpen
			)

	def EnableInputTrigger(self, trigAddress=defaultNamedNotOptArg, event=defaultNamedNotOptArg, sigType=defaultNamedNotOptArg):
		'method EnableInputTrigger'
		return self._oleobj_.InvokeTypes(130, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1)),trigAddress
			, event, sigType)

	def EnableOutputTrigger(self, trigAddress=defaultNamedNotOptArg, event=defaultNamedNotOptArg, sigType=defaultNamedNotOptArg):
		'method EnableOutputTrigger'
		return self._oleobj_.InvokeTypes(139, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1)),trigAddress
			, event, sigType)

	def GetAreaSubtimer(self, areaNum=defaultNamedNotOptArg, time=pythoncom.Missing):
		'method GetAreaSubTimer'
		return self._ApplyTypes_(328, 1, (24, 0), ((3, 1), (16389, 2)), 'GetAreaSubtimer', None,areaNum
			, time)

	# Result is of type IJYAxis
	def GetAxisAs(self, dataObj=defaultNamedNotOptArg, whichAxis=defaultNamedNotOptArg, axisType=defaultNamedNotOptArg):
		'method GetAxisAs'
		ret = self._oleobj_.InvokeTypes(326, LCID, 1, (9, 0), ((9, 1), (3, 1), (3, 1)),dataObj
			, whichAxis, axisType)
		if ret is not None:
			ret = Dispatch(ret, 'GetAxisAs', '{75F30081-BED4-4B0A-AB8B-5D3DFEC775D2}')
		return ret

	def GetChipReadoutLocationAndDirection(self):
		'method GetChipReadoutLocationAndDirection'
		return self._oleobj_.InvokeTypes(364, LCID, 1, (3, 0), (),)

	def GetChipSize(self, activeXPixels=pythoncom.Missing, activeYPixels=pythoncom.Missing):
		'method GetChipSize'
		return self._ApplyTypes_(316, 1, (24, 0), ((16387, 2), (16387, 2)), 'GetChipSize', None,activeXPixels
			, activeYPixels)

	def GetComponentVersion(self, major=pythoncom.Missing, minor=pythoncom.Missing, mini=pythoncom.Missing, buildNum=pythoncom.Missing):
		'method GetComponentVersion'
		return self._ApplyTypes_(27, 1, (8, 0), ((16387, 2), (16387, 2), (16387, 2), (16387, 2)), 'GetComponentVersion', None,major
			, minor, mini, buildNum)

	def GetControllerOperationValue(self, token=defaultNamedNotOptArg, lastSet=pythoncom.Missing):
		'method GetControllerOperationValue'
		return self._ApplyTypes_(117, 1, (5, 0), ((3, 1), (16389, 2)), 'GetControllerOperationValue', None,token
			, lastSet)

	def GetConverterReference(self, pVal=pythoncom.Missing):
		'method GetConverterReference'
		return self._ApplyTypes_(112, 1, (24, 0), ((16393, 2),), 'GetConverterReference', None,pVal
			)

	def GetData(self, dataPtr=defaultNamedNotOptArg):
		'method GetData'
		return self._ApplyTypes_(202, 1, (24, 0), ((16396, 3),), 'GetData', None,dataPtr
			)

	def GetDefaultUnits(self, type=defaultNamedNotOptArg, pVal=pythoncom.Missing, pStrVal=pythoncom.Missing):
		'method GetDefaultUnits'
		return self._ApplyTypes_(110, 1, (24, 0), ((3, 1), (16387, 2), (16396, 18)), 'GetDefaultUnits', None,type
			, pVal, pStrVal)

	def GetDeviceAddress(self, devAddress=pythoncom.Missing):
		'method GetDeviceAddress'
		return self._ApplyTypes_(151, 1, (24, 0), ((16396, 2),), 'GetDeviceAddress', None,devAddress
			)

	def GetDeviceConfigProperty(self, property=defaultNamedNotOptArg):
		'method GetDeviceConfigProperty'
		return self._ApplyTypes_(148, 1, (12, 0), ((3, 1),), 'GetDeviceConfigProperty', None,property
			)

	def GetEMADCMode(self):
		'method GetEMADCMode'
		return self._oleobj_.InvokeTypes(360, LCID, 1, (11, 0), (),)

	def GetEMFitParams(self, emParamCount=pythoncom.Missing, vtArray=pythoncom.Missing):
		'property GetEMFitParams'
		return self._ApplyTypes_(358, 1, (24, 0), ((16387, 2), (16396, 2)), 'GetEMFitParams', None,emParamCount
			, vtArray)

	def GetEMState(self):
		'method GetEMState'
		return self._oleobj_.InvokeTypes(359, LCID, 1, (11, 0), (),)

	def GetFirstADC(self, Description=pythoncom.Missing):
		'method GetFirstADC'
		return self._ApplyTypes_(320, 1, (3, 0), ((16392, 2),), 'GetFirstADC', None,Description
			)

	def GetFirstCalibrationCoefficient(self):
		'method GetFirstCalibrationCoefficient'
		return self._oleobj_.InvokeTypes(351, LCID, 1, (4, 0), (),)

	def GetFirstControllerOperation(self, token=pythoncom.Missing, Description=pythoncom.Missing, currentValue=pythoncom.Missing):
		'method GetFirstControllerOperation'
		return self._ApplyTypes_(114, 1, (24, 0), ((16387, 2), (16392, 2), (16389, 2)), 'GetFirstControllerOperation', None,token
			, Description, currentValue)

	def GetFirstGain(self, Description=pythoncom.Missing):
		'method GetFirstGain'
		return self._ApplyTypes_(205, 1, (3, 0), ((16392, 2),), 'GetFirstGain', None,Description
			)

	def GetFirstOperatingMode(self, modeName=pythoncom.Missing):
		'method GetFirstOperatingMode'
		return self._ApplyTypes_(119, 1, (3, 0), ((16392, 2),), 'GetFirstOperatingMode', None,modeName
			)

	def GetFirstParallelSpeed(self, Description=pythoncom.Missing):
		'method GetFirstParallelSpeed'
		return self._ApplyTypes_(361, 1, (3, 0), ((16392, 2),), 'GetFirstParallelSpeed', None,Description
			)

	def GetFirstReferenceGain(self, gainDescription=pythoncom.Missing):
		'method GetFirstReferenceGain'
		return self._ApplyTypes_(336, 1, (3, 0), ((16392, 2),), 'GetFirstReferenceGain', None,gainDescription
			)

	def GetFirstSupportedInputTriggerAddress(self, trigAddress=pythoncom.Missing, trigAddressString=pythoncom.Missing):
		'method GetFirstSupportedInputTriggerAddress'
		return self._ApplyTypes_(124, 1, (24, 0), ((16387, 2), (16392, 2)), 'GetFirstSupportedInputTriggerAddress', None,trigAddress
			, trigAddressString)

	def GetFirstSupportedInputTriggerEvent(self, trigAddress=defaultNamedNotOptArg, eventPtr=pythoncom.Missing, trigEventString=pythoncom.Missing):
		'method GetFirstSupportedInputTriggerEvent'
		return self._ApplyTypes_(126, 1, (24, 0), ((3, 1), (16387, 2), (16392, 2)), 'GetFirstSupportedInputTriggerEvent', None,trigAddress
			, eventPtr, trigEventString)

	def GetFirstSupportedInputTriggerSignalType(self, trigAddress=defaultNamedNotOptArg, event=defaultNamedNotOptArg, trigSigType=pythoncom.Missing, trigSigTypeString=pythoncom.Missing):
		'method GetFirstSupportedInputTriggerSignalType'
		return self._ApplyTypes_(128, 1, (24, 0), ((3, 1), (3, 1), (16387, 2), (16392, 2)), 'GetFirstSupportedInputTriggerSignalType', None,trigAddress
			, event, trigSigType, trigSigTypeString)

	def GetFirstSupportedOutputTriggerAddress(self, trigAddress=pythoncom.Missing, trigAddressString=pythoncom.Missing):
		'method GetFirstSupportedOutputTriggerAddress'
		return self._ApplyTypes_(133, 1, (24, 0), ((16387, 2), (16392, 2)), 'GetFirstSupportedOutputTriggerAddress', None,trigAddress
			, trigAddressString)

	def GetFirstSupportedOutputTriggerEvent(self, trigAddress=defaultNamedNotOptArg, eventPtr=pythoncom.Missing, trigEventString=pythoncom.Missing):
		'method GetFirstSupportedOutputTriggerEvent'
		return self._ApplyTypes_(135, 1, (24, 0), ((3, 1), (16387, 2), (16392, 2)), 'GetFirstSupportedOutputTriggerEvent', None,trigAddress
			, eventPtr, trigEventString)

	def GetFirstSupportedOutputTriggerSignalType(self, trigAddress=defaultNamedNotOptArg, event=defaultNamedNotOptArg, trigSigType=pythoncom.Missing, trigSigTypeString=pythoncom.Missing):
		'method GetFirstSupportedOutputTriggerSignalType'
		return self._ApplyTypes_(137, 1, (24, 0), ((3, 1), (3, 1), (16387, 2), (16392, 2)), 'GetFirstSupportedOutputTriggerSignalType', None,trigAddress
			, event, trigSigType, trigSigTypeString)

	def GetFirstSupportedUnits(self, unitsType=defaultNamedNotOptArg, pVal=pythoncom.Missing, pStrVal=pythoncom.Missing):
		'method GetFirstSupportedUnits'
		return self._ApplyTypes_(108, 1, (24, 0), ((3, 1), (16387, 2), (16396, 18)), 'GetFirstSupportedUnits', None,unitsType
			, pVal, pStrVal)

	def GetLampProperty(self, propToGet=defaultNamedNotOptArg):
		'method GetLampProperty'
		return self._ApplyTypes_(349, 1, (12, 0), ((3, 1),), 'GetLampProperty', None,propToGet
			)

	def GetLaserProperty(self, propToGet=defaultNamedNotOptArg):
		'method GetLaserProperty'
		return self._ApplyTypes_(345, 1, (12, 0), ((3, 1),), 'GetLaserProperty', None,propToGet
			)

	def GetLinearizationParams(self, vtArrayFltParams=pythoncom.Missing):
		'method GetLinearizationParams'
		return self._ApplyTypes_(355, 1, (24, 0), ((16396, 2),), 'GetLinearizationParams', None,vtArrayFltParams
			)

	def GetMono(self, iMono=pythoncom.Missing):
		'method GetMono'
		return self._ApplyTypes_(331, 1, (24, 0), ((16393, 2),), 'GetMono', None,iMono
			)

	def GetMultiAcqCleanCount(self, acqState=defaultNamedNotOptArg):
		'method GetMultiAcqCleanCount'
		return self._oleobj_.InvokeTypes(215, LCID, 1, (3, 0), ((3, 1),),acqState
			)

	def GetMultiAcqDelay(self, acqState=defaultNamedNotOptArg):
		'method GetMultiAcqDelay'
		return self._oleobj_.InvokeTypes(213, LCID, 1, (5, 0), ((3, 1),),acqState
			)

	def GetNextADC(self, Description=pythoncom.Missing):
		'method GetNextADC'
		return self._ApplyTypes_(321, 1, (3, 0), ((16392, 2),), 'GetNextADC', None,Description
			)

	def GetNextCalibrationCoefficient(self):
		'method GetNextCalibrationCoefficient'
		return self._oleobj_.InvokeTypes(352, LCID, 1, (4, 0), (),)

	def GetNextControllerOperation(self, token=pythoncom.Missing, Description=pythoncom.Missing, currentValue=pythoncom.Missing):
		'method GetNextControllerOperation'
		return self._ApplyTypes_(115, 1, (24, 0), ((16387, 2), (16392, 2), (16389, 2)), 'GetNextControllerOperation', None,token
			, Description, currentValue)

	def GetNextGain(self, Description=pythoncom.Missing):
		'method GetNextGain'
		return self._ApplyTypes_(206, 1, (3, 0), ((16392, 2),), 'GetNextGain', None,Description
			)

	def GetNextOperatingMode(self, modeName=pythoncom.Missing):
		'method GetNextOperatingMode'
		return self._ApplyTypes_(120, 1, (3, 0), ((16392, 2),), 'GetNextOperatingMode', None,modeName
			)

	def GetNextParallelSpeed(self, Description=pythoncom.Missing):
		'method GetNextParallelSpeed'
		return self._ApplyTypes_(362, 1, (3, 0), ((16392, 2),), 'GetNextParallelSpeed', None,Description
			)

	def GetNextReferenceGain(self, gainDescription=pythoncom.Missing):
		'method GetNextReferenceGain'
		return self._ApplyTypes_(337, 1, (3, 0), ((16392, 2),), 'GetNextReferenceGain', None,gainDescription
			)

	def GetNextSupportedInputTriggerAddress(self, trigAddress=pythoncom.Missing, trigAddressString=pythoncom.Missing):
		'method GetNextSupportedInputTriggerAddress'
		return self._ApplyTypes_(125, 1, (24, 0), ((16387, 2), (16392, 2)), 'GetNextSupportedInputTriggerAddress', None,trigAddress
			, trigAddressString)

	def GetNextSupportedInputTriggerEvent(self, trigAddress=defaultNamedNotOptArg, eventPtr=pythoncom.Missing, trigEventString=pythoncom.Missing):
		'method GetNextSupportedInputTriggerEvent'
		return self._ApplyTypes_(127, 1, (24, 0), ((3, 1), (16387, 2), (16392, 2)), 'GetNextSupportedInputTriggerEvent', None,trigAddress
			, eventPtr, trigEventString)

	def GetNextSupportedInputTriggerSignalType(self, trigAddress=defaultNamedNotOptArg, event=defaultNamedNotOptArg, trigSigType=pythoncom.Missing, trigSigTypeString=pythoncom.Missing):
		'method GetNextSupportedInputTriggerSignalType'
		return self._ApplyTypes_(129, 1, (24, 0), ((3, 1), (3, 1), (16387, 2), (16392, 2)), 'GetNextSupportedInputTriggerSignalType', None,trigAddress
			, event, trigSigType, trigSigTypeString)

	def GetNextSupportedOutputTriggerAddress(self, trigAddress=pythoncom.Missing, trigAddressString=pythoncom.Missing):
		'method GetNextSupportedOutputTriggerAddress'
		return self._ApplyTypes_(134, 1, (24, 0), ((16387, 2), (16392, 2)), 'GetNextSupportedOutputTriggerAddress', None,trigAddress
			, trigAddressString)

	def GetNextSupportedOutputTriggerEvent(self, trigAddress=defaultNamedNotOptArg, eventPtr=pythoncom.Missing, trigEventString=pythoncom.Missing):
		'method GetNextSupportedOutputTriggerEvent'
		return self._ApplyTypes_(136, 1, (24, 0), ((3, 1), (16387, 2), (16392, 2)), 'GetNextSupportedOutputTriggerEvent', None,trigAddress
			, eventPtr, trigEventString)

	def GetNextSupportedOutputTriggerSignalType(self, trigAddress=defaultNamedNotOptArg, event=defaultNamedNotOptArg, trigSigType=pythoncom.Missing, trigSigTypeString=pythoncom.Missing):
		'method GetNextSupportedOutputTriggerSignalType'
		return self._ApplyTypes_(138, 1, (24, 0), ((3, 1), (3, 1), (16387, 2), (16392, 2)), 'GetNextSupportedOutputTriggerSignalType', None,trigAddress
			, event, trigSigType, trigSigTypeString)

	def GetNextSupportedUnits(self, unitsType=defaultNamedNotOptArg, pVal=pythoncom.Missing, pStrVal=pythoncom.Missing):
		'method GetNextSupportedUnits'
		return self._ApplyTypes_(109, 1, (24, 0), ((3, 1), (16387, 2), (16396, 18)), 'GetNextSupportedUnits', None,unitsType
			, pVal, pStrVal)

	def GetOperatingModeValue(self, whichOpMode=defaultNamedNotOptArg):
		'method GetOperatingMode'
		return self._ApplyTypes_(121, 1, (12, 0), ((3, 1),), 'GetOperatingModeValue', None,whichOpMode
			)

	def GetPixelSpacing(self, horizontalPixelSpacing=pythoncom.Missing, verticalPixelSpacing=pythoncom.Missing):
		'method GetPixelSpacing'
		return self._ApplyTypes_(317, 1, (24, 0), ((16387, 2), (16387, 2)), 'GetPixelSpacing', None,horizontalPixelSpacing
			, verticalPixelSpacing)

	def GetReferenceGain(self):
		'method GetReferenceGain'
		return self._oleobj_.InvokeTypes(335, LCID, 1, (3, 0), (),)

	# Result is of type IJYResultsObject
	def GetResult(self):
		'method GetResult'
		ret = self._oleobj_.InvokeTypes(319, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetResult', '{3948DB1C-95F8-4F57-AE15-2A5FC0B04CF1}')
		return ret

	def GetWavelengthCoverage(self, position=defaultNamedNotOptArg, Units=defaultNamedNotOptArg, start=pythoncom.Missing, end=pythoncom.Missing):
		'method GetWavelengthCoverage'
		return self._ApplyTypes_(332, 1, (24, 0), ((5, 1), (3, 1), (16389, 2), (16389, 2)), 'GetWavelengthCoverage', None,position
			, Units, start, end)

	def Initialize(self, forceInit=defaultNamedOptArg, emulate=defaultNamedOptArg, nonThreaded=defaultNamedOptArg):
		'method Initialize'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), ((12, 17), (12, 17), (12, 17)),forceInit
			, emulate, nonThreaded)

	def IsControllerOperationSupported(self, whichOperation=defaultNamedNotOptArg):
		'method IsControllerOperationSupported'
		return self._oleobj_.InvokeTypes(118, LCID, 1, (11, 0), ((3, 1),),whichOperation
			)

	def IsInputTriggerEnabled(self, trigAddress=defaultNamedNotOptArg, event=defaultNamedNotOptArg, sigType=defaultNamedNotOptArg):
		'method IsInputTriggerEnabled'
		return self._oleobj_.InvokeTypes(144, LCID, 1, (11, 0), ((3, 1), (3, 1), (3, 1)),trigAddress
			, event, sigType)

	def IsInputTriggerSupported(self, trigAddress=defaultNamedNotOptArg, event=defaultNamedNotOptArg, sigType=defaultNamedNotOptArg):
		'method IsInputTriggerSupported'
		return self._oleobj_.InvokeTypes(142, LCID, 1, (11, 0), ((3, 1), (3, 1), (3, 1)),trigAddress
			, event, sigType)

	def IsOperatingModeSupported(self, opModeToCheck=defaultNamedNotOptArg):
		'method IsOperatingModeSupported'
		return self._oleobj_.InvokeTypes(123, LCID, 1, (11, 0), ((3, 1),),opModeToCheck
			)

	def IsOutputTriggerEnabled(self, trigAddress=defaultNamedNotOptArg, event=defaultNamedNotOptArg, sigType=defaultNamedNotOptArg):
		'method IsOutputTriggerEnabled'
		return self._oleobj_.InvokeTypes(145, LCID, 1, (11, 0), ((3, 1), (3, 1), (3, 1)),trigAddress
			, event, sigType)

	def IsOutputTriggerSupported(self, trigAddress=defaultNamedNotOptArg, event=defaultNamedNotOptArg, sigType=defaultNamedNotOptArg):
		'method IsOutputTriggerSupported'
		return self._oleobj_.InvokeTypes(143, LCID, 1, (11, 0), ((3, 1), (3, 1), (3, 1)),trigAddress
			, event, sigType)

	def LampFire(self):
		'method LampFire'
		return self._oleobj_.InvokeTypes(350, LCID, 1, (24, 0), (),)

	def Load(self):
		'Method Load'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (24, 0), (),)

	def OpenCommunications(self):
		'Method OpenCommunications'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), (),)

	def OpenCommunicationsEx(self, _MIDL__IJYDeviceReqd0000_=defaultNamedNotOptArg, portNum=defaultNamedNotOptArg, devName=defaultNamedOptArg, bRate=defaultNamedOptArg
			, databits=defaultNamedOptArg, parityBits=defaultNamedOptArg, jy_pid_comm_stopbits=defaultNamedOptArg):
		'Method OpenCommunicationsEx'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((3, 1), (3, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),_MIDL__IJYDeviceReqd0000_
			, portNum, devName, bRate, databits, parityBits
			, jy_pid_comm_stopbits)

	def OpenShutter(self):
		'method OpenShutter'
		return self._oleobj_.InvokeTypes(304, LCID, 1, (24, 0), (),)

	def ReadCommSetting(self, _MIDL__IJYDeviceReqd0001_=defaultNamedNotOptArg):
		'method ReadCommSetting'
		return self._ApplyTypes_(19, 1, (12, 0), ((3, 1),), 'ReadCommSetting', None,_MIDL__IJYDeviceReqd0001_
			)

	def ReadI2C(self, i2cAddr=defaultNamedNotOptArg, length=defaultNamedNotOptArg, rxData=pythoncom.Missing):
		'method ReadI2C'
		return self._ApplyTypes_(23, 1, (24, 0), ((3, 1), (3, 1), (16396, 2)), 'ReadI2C', None,i2cAddr
			, length, rxData)

	def ReadReferenceValue(self):
		'method ReadReferenceValue'
		return self._oleobj_.InvokeTypes(333, LCID, 1, (5, 0), (),)

	def ReadString(self, charCount=defaultNamedNotOptArg):
		'method ReadString'
		return self._ApplyTypes_(6, 1, (8, 0), ((16387, 3),), 'ReadString', None,charCount
			)

	def RebootDevice(self):
		'method RebootDevice'
		return self._oleobj_.InvokeTypes(152, LCID, 1, (24, 0), (),)

	def Save(self):
		'Method Save'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), (),)

	def SelectADC(self, adc=defaultNamedNotOptArg):
		'method SelectADC'
		return self._oleobj_.InvokeTypes(303, LCID, 1, (24, 0), ((3, 1),),adc
			)

	def SendString(self, stringToSend=defaultNamedNotOptArg, countToSend=defaultNamedOptArg):
		'method SendString'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), ((8, 1), (12, 17)),stringToSend
			, countToSend)

	def SetAreaSubtimer(self, areaNum=defaultNamedNotOptArg, time=defaultNamedNotOptArg):
		'method SetAreaSubTimer'
		return self._oleobj_.InvokeTypes(327, LCID, 1, (24, 0), ((3, 1), (5, 1)),areaNum
			, time)

	def SetControllerOperationValue(self, token=defaultNamedNotOptArg, newValue=defaultNamedNotOptArg):
		'method SetControllerOperationValue'
		return self._oleobj_.InvokeTypes(116, LCID, 1, (24, 0), ((3, 1), (5, 1)),token
			, newValue)

	def SetDefaultUnits(self, type=defaultNamedNotOptArg, newVal=defaultNamedNotOptArg):
		'method SetDefaultUnits'
		return self._oleobj_.InvokeTypes(111, LCID, 1, (24, 0), ((3, 1), (3, 1)),type
			, newVal)

	def SetDeviceAddress(self, newAddress=defaultNamedNotOptArg):
		'method SetDeviceAddress'
		return self._oleobj_.InvokeTypes(150, LCID, 1, (24, 0), ((12, 1),),newAddress
			)

	def SetDeviceConfigProperty(self, property=defaultNamedNotOptArg, newVal=defaultNamedNotOptArg, newVal2=defaultNamedOptArg, newVal3=defaultNamedOptArg
			, newVal4=defaultNamedOptArg):
		'method SetDeviceConfigProperty'
		return self._oleobj_.InvokeTypes(149, LCID, 1, (24, 0), ((3, 1), (12, 1), (12, 17), (12, 17), (12, 17)),property
			, newVal, newVal2, newVal3, newVal4)

	def SetEMFitParams(self, emParamCount=defaultNamedNotOptArg, vtArray=defaultNamedNotOptArg):
		'property SetEMFitParams'
		return self._oleobj_.InvokeTypes(357, LCID, 1, (24, 0), ((3, 1), (12, 1)),emParamCount
			, vtArray)

	def SetLampProperty(self, propToSet=defaultNamedNotOptArg, propVal=defaultNamedNotOptArg):
		'method SetLampProperty'
		return self._oleobj_.InvokeTypes(348, LCID, 1, (24, 0), ((3, 1), (12, 1)),propToSet
			, propVal)

	def SetLaserProperty(self, propToSet=defaultNamedNotOptArg, propVal=defaultNamedNotOptArg):
		'method SetLaserProperty'
		return self._oleobj_.InvokeTypes(344, LCID, 1, (24, 0), ((3, 1), (12, 1)),propToSet
			, propVal)

	def SetLinearizationParams(self, vtArrayFltParams=defaultNamedNotOptArg):
		'method SetLinearizationParams'
		return self._oleobj_.InvokeTypes(354, LCID, 1, (24, 0), ((12, 1),),vtArrayFltParams
			)

	def SetMono(self, iMono=defaultNamedNotOptArg, onExitPortAxial=defaultNamedNotOptArg):
		'method SetMono'
		return self._oleobj_.InvokeTypes(324, LCID, 1, (24, 0), ((9, 1), (11, 1)),iMono
			, onExitPortAxial)

	def SetMonoProperty(self, whichProperty=defaultNamedNotOptArg, propVal=defaultNamedNotOptArg):
		'method SetMonoProperty'
		return self._oleobj_.InvokeTypes(325, LCID, 1, (24, 0), ((3, 1), (12, 1)),whichProperty
			, propVal)

	def SetMultiAcqCleanCount(self, acqState=defaultNamedNotOptArg, cleansForMode=defaultNamedNotOptArg):
		'method SetMultiAcqCleanCount'
		return self._oleobj_.InvokeTypes(214, LCID, 1, (24, 0), ((3, 1), (3, 1)),acqState
			, cleansForMode)

	def SetMultiAcqDelay(self, acqState=defaultNamedNotOptArg, delayForMode=defaultNamedNotOptArg):
		'method SetMultiAcqDelay'
		return self._oleobj_.InvokeTypes(212, LCID, 1, (24, 0), ((3, 1), (5, 1)),acqState
			, delayForMode)

	def SetOperatingModeValue(self, whichOpMode=defaultNamedNotOptArg, newOpModeVal=defaultNamedNotOptArg):
		'method SetOperatingMode'
		return self._oleobj_.InvokeTypes(122, LCID, 1, (24, 0), ((3, 1), (12, 1)),whichOpMode
			, newOpModeVal)

	def SetReferenceGain(self, gainToken=defaultNamedNotOptArg):
		'method SetReferenceGain'
		return self._oleobj_.InvokeTypes(334, LCID, 1, (24, 0), ((3, 1),),gainToken
			)

	def Setup(self):
		'method Setup'
		return self._oleobj_.InvokeTypes(101, LCID, 1, (24, 0), (),)

	def Shutdown(self, msToWait=defaultNamedNotOptArg):
		'method Shutdown'
		return self._oleobj_.InvokeTypes(146, LCID, 1, (24, 0), ((3, 17),),msToWait
			)

	def SoftwareAssertHardwareTrigger(self):
		'method SoftwareAssertHardwareTrigger'
		return self._oleobj_.InvokeTypes(155, LCID, 1, (24, 0), (),)

	def StartAcquisition(self, ShutterOpen=defaultNamedNotOptArg):
		'method StartAcquisition'
		return self._oleobj_.InvokeTypes(201, LCID, 1, (24, 0), ((11, 1),),ShutterOpen
			)

	def StopAcquisition(self):
		'method StopAcquisition'
		return self._oleobj_.InvokeTypes(218, LCID, 1, (24, 0), (),)

	def TalkUSB(self, request=defaultNamedNotOptArg, index=defaultNamedNotOptArg, value=defaultNamedNotOptArg, length=defaultNamedNotOptArg
			, direction=defaultNamedNotOptArg, data=defaultNamedNotOptArg):
		'method TalkUSB'
		return self._ApplyTypes_(154, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (16396, 3)), 'TalkUSB', None,request
			, index, value, length, direction, data
			)

	def TriggerEnable(self, trigenable=defaultNamedNotOptArg, flags=defaultNamedNotOptArg):
		'method TriggerEnable'
		return self._oleobj_.InvokeTypes(312, LCID, 1, (24, 0), ((11, 1), (3, 1)),trigenable
			, flags)

	def Uninitialize(self):
		'method Uninitialize'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), (),)

	def UpdateCommSetting(self, _MIDL__IJYDeviceReqd0002_=defaultNamedNotOptArg, newVal=defaultNamedNotOptArg):
		'method UpdateCommSetting'
		return self._oleobj_.InvokeTypes(20, LCID, 1, (24, 0), ((3, 1), (12, 1)),_MIDL__IJYDeviceReqd0002_
			, newVal)

	def ValidateHW(self):
		'method ValidateHW'
		return self._oleobj_.InvokeTypes(25, LCID, 1, (24, 0), (),)

	def WriteI2C(self, i2cAddr=defaultNamedNotOptArg, length=defaultNamedNotOptArg, txData=defaultNamedNotOptArg):
		'method WriteI2C'
		return self._oleobj_.InvokeTypes(22, LCID, 1, (24, 0), ((3, 1), (3, 1), (12, 1)),i2cAddr
			, length, txData)

	_prop_map_get_ = {
		"AccumulationMode": (207, 2, (3, 0), (), "AccumulationMode", None),
		"AcquisitionCount": (323, 2, (3, 0), (), "AcquisitionCount", None),
		"AutoNormalize": (339, 2, (11, 0), (), "AutoNormalize", None),
		"ChipDescription": (329, 2, (8, 0), (), "ChipDescription", None),
		"ControllerChannelIndex": (113, 2, (12, 0), (), "ControllerChannelIndex", None),
		"CurrentADC": (322, 2, (3, 0), (), "CurrentADC", None),
		"CurrentParallelSpeed": (363, 2, (3, 0), (), "CurrentParallelSpeed", None),
		"CurrentTemperature": (310, 2, (5, 0), (), "CurrentTemperature", None),
		"DarkSubtract": (330, 2, (11, 0), (), "DarkSubtract", None),
		"DataSize": (203, 2, (3, 0), (), "DataSize", None),
		"Description": (147, 2, (8, 0), (), "Description", None),
		"DeviceClass": (104, 2, (3, 0), (), "DeviceClass", None),
		"DeviceMemorySlotsFloatMaxCount": (32, 2, (24, 0), ((16387, 2),), "DeviceMemorySlotsFloatMaxCount", None),
		"DeviceMemorySlotsStringMaxCount": (29, 2, (24, 0), ((16387, 2),), "DeviceMemorySlotsStringMaxCount", None),
		"DeviceMemorySlotsStringMaxLength": (28, 2, (24, 0), ((16387, 2),), "DeviceMemorySlotsStringMaxLength", None),
		"DeviceType": (105, 2, (3, 0), (), "DeviceType", None),
		"EMGain": (356, 2, (3, 0), (), "EMGain", None),
		"Emulating": (9, 2, (11, 0), (), "Emulating", None),
		"ErrDisplayMode": (15, 2, (3, 0), (), "ErrDisplayMode", None),
		"FirmwareVersion": (8, 2, (8, 0), (), "FirmwareVersion", None),
		"FlushCount": (307, 2, (3, 0), (), "FlushCount", None),
		"Gain": (308, 2, (3, 0), (), "Gain", None),
		"HasLampControl": (346, 2, (11, 0), (), "HasLampControl", None),
		"HasLaserControl": (342, 2, (11, 0), (), "HasLaserControl", None),
		"InitializeComplete": (24, 2, (11, 0), (), "InitializeComplete", None),
		"IntegrationTime": (204, 2, (5, 0), (), "IntegrationTime", None),
		"LampEnabled": (347, 2, (11, 0), (), "LampEnabled", None),
		"LaserEnabled": (343, 2, (11, 0), (), "LaserEnabled", None),
		"LastError": (13, 2, (3, 0), (), "LastError", None),
		"LedsOn": (341, 2, (11, 0), (), "LedsOn", None),
		"LinearizationMode": (353, 2, (3, 0), (), "LinearizationMode", None),
		"MultiAcqHardwareMode": (216, 2, (11, 0), (), "MultiAcqHardwareMode", None),
		"MultiAcqShutterMode": (211, 2, (3, 0), (), "MultiAcqShutterMode", None),
		"MultiAcqTotalTime": (217, 2, (5, 0), (), "MultiAcqTotalTime", None),
		"Name": (10, 2, (8, 0), (), "Name", None),
		"NumberOfAccumulations": (208, 2, (3, 0), (), "NumberOfAccumulations", None),
		"PassThruSendTerminationCharacter": (7, 2, (8, 0), (), "PassThruSendTerminationCharacter", None),
		"ReadyForAcquisition": (210, 2, (11, 0), (), "ReadyForAcquisition", None),
		"ReferenceMode": (338, 2, (3, 0), (), "ReferenceMode", None),
		"SerialNumber": (26, 2, (8, 0), (), "SerialNumber", None),
		"SupportFilesPath": (18, 2, (8, 0), (), "SupportFilesPath", None),
		"TemperatureSetPoint": (311, 2, (5, 0), (), "TemperatureSetPoint", None),
		"TimeInterval": (209, 2, (5, 0), (), "TimeInterval", None),
		"Uniqueid": (103, 2, (8, 0), (), "Uniqueid", None),
	}
	_prop_map_put_ = {
		"AccumulationMode": ((207, LCID, 4, 0),()),
		"AcquisitionCount": ((323, LCID, 4, 0),()),
		"AutoNormalize": ((339, LCID, 4, 0),()),
		"ChipDescription": ((329, LCID, 4, 0),()),
		"ControllerChannelIndex": ((113, LCID, 4, 0),()),
		"CurrentADC": ((322, LCID, 4, 0),()),
		"CurrentParallelSpeed": ((363, LCID, 4, 0),()),
		"DarkSubtract": ((330, LCID, 4, 0),()),
		"Description": ((147, LCID, 4, 0),()),
		"EMGain": ((356, LCID, 4, 0),()),
		"ErrDisplayMode": ((15, LCID, 4, 0),()),
		"FlushCount": ((307, LCID, 4, 0),()),
		"Gain": ((308, LCID, 4, 0),()),
		"IntegrationTime": ((204, LCID, 4, 0),()),
		"LampEnabled": ((347, LCID, 4, 0),()),
		"LaserEnabled": ((343, LCID, 4, 0),()),
		"LedsOn": ((341, LCID, 4, 0),()),
		"LinearizationMode": ((353, LCID, 4, 0),()),
		"MultiAcqHardwareMode": ((216, LCID, 4, 0),()),
		"MultiAcqShutterMode": ((211, LCID, 4, 0),()),
		"MultiAcqTotalTime": ((217, LCID, 4, 0),()),
		"Name": ((10, LCID, 4, 0),()),
		"NumberOfAccumulations": ((208, LCID, 4, 0),()),
		"PassThruSendTerminationCharacter": ((7, LCID, 4, 0),()),
		"ReferenceMode": ((338, LCID, 4, 0),()),
		"SupportFilesPath": ((18, LCID, 4, 0),()),
		"TemperatureSetPoint": ((311, LCID, 4, 0),()),
		"TimeInterval": ((209, LCID, 4, 0),()),
		"Uniqueid": ((103, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _IJYDeviceReqdEvents:
	'_IJYDeviceReqdEvents Interface'
	CLSID = CLSID_Sink = IID('{A2C81A78-CA13-4A39-8FCB-CD51BD4E9376}')
	coclass_clsid = IID('{4D7AAEFC-19F9-49B7-A5BB-814933694FD3}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnInitialize",
		        2 : "OnOperationStatus",
		        3 : "OnUpdate",
		        4 : "OnCriticalError",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnInitialize(self, status=defaultNamedNotOptArg, eventInfo=defaultNamedNotOptArg):
#		'method Initialize'
#	def OnOperationStatus(self, status=defaultNamedNotOptArg, eventInfo=defaultNamedNotOptArg):
#		'method OperationStatus'
#	def OnUpdate(self, updateType=defaultNamedNotOptArg, eventInfo=defaultNamedNotOptArg):
#		'method Update'
#	def OnCriticalError(self, status=defaultNamedNotOptArg, eventInfo=defaultNamedNotOptArg):
#		'method CriticalError'


from win32com.client import CoClassBaseClass
# This CoClass is known by the name 'JYCCD.JYMCD.1'
class JYMCD(CoClassBaseClass): # A CoClass
	# JYMCD Class
	CLSID = IID('{4D7AAEFC-19F9-49B7-A5BB-814933694FD3}')
	coclass_sources = [
		_IJYDeviceReqdEvents,
	]
	default_source = _IJYDeviceReqdEvents
	coclass_interfaces = [
		IJYCCDReqd,
	]
	default_interface = IJYCCDReqd

IJYCCDReqd_vtables_dispatch_ = 1
IJYCCDReqd_vtables_ = [
	(( 'DefineAcquisitionFormat' , '__MIDL__IJYCCDReqd0000' , 'numAreas' , ), 301, (301, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 1008 , (3, 0, None, None) , 0 , )),
	(( 'DefineArea' , 'areaNum' , 'xOrigin' , 'yOrigin' , 'xSize' , 
			 'ySize' , 'xBin' , 'yBin' , ), 302, (302, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 1016 , (3, 0, None, None) , 0 , )),
	(( 'SelectADC' , 'adc' , ), 303, (303, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 1024 , (3, 0, None, None) , 0 , )),
	(( 'OpenShutter' , ), 304, (304, (), [ ], 1 , 1 , 4 , 0 , 1032 , (3, 0, None, None) , 0 , )),
	(( 'CloseShutter' , ), 305, (305, (), [ ], 1 , 1 , 4 , 0 , 1040 , (3, 0, None, None) , 0 , )),
	(( 'FlushCount' , 'pVal' , ), 307, (307, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 1048 , (3, 0, None, None) , 0 , )),
	(( 'FlushCount' , 'pVal' , ), 307, (307, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 1056 , (3, 0, None, None) , 0 , )),
	(( 'Gain' , 'pVal' , ), 308, (308, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 1064 , (3, 0, None, None) , 0 , )),
	(( 'Gain' , 'pVal' , ), 308, (308, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 1072 , (3, 0, None, None) , 0 , )),
	(( 'CurrentTemperature' , 'pVal' , ), 310, (310, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 1080 , (3, 0, None, None) , 0 , )),
	(( 'TemperatureSetPoint' , 'pVal' , ), 311, (311, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 1088 , (3, 0, None, None) , 0 , )),
	(( 'TemperatureSetPoint' , 'pVal' , ), 311, (311, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 1096 , (3, 0, None, None) , 0 , )),
	(( 'TriggerEnable' , 'trigenable' , 'flags' , ), 312, (312, (), [ (11, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 1104 , (3, 0, None, None) , 0 , )),
	(( 'GetChipSize' , 'activeXPixels' , 'activeYPixels' , ), 316, (316, (), [ (16387, 2, None, None) , 
			 (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 1112 , (3, 0, None, None) , 0 , )),
	(( 'GetPixelSpacing' , 'horizontalPixelSpacing' , 'verticalPixelSpacing' , ), 317, (317, (), [ (16387, 2, None, None) , 
			 (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 1120 , (3, 0, None, None) , 0 , )),
	(( 'DoAcquisition' , 'ShutterOpen' , ), 318, (318, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 1128 , (3, 0, None, None) , 0 , )),
	(( 'GetResult' , 'resultObj' , ), 319, (319, (), [ (16393, 10, None, "IID('{3948DB1C-95F8-4F57-AE15-2A5FC0B04CF1}')") , ], 1 , 1 , 4 , 0 , 1136 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstADC' , 'Description' , 'adcToken' , ), 320, (320, (), [ (16392, 2, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 1144 , (3, 0, None, None) , 0 , )),
	(( 'GetNextADC' , 'Description' , 'adcToken' , ), 321, (321, (), [ (16392, 2, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 1152 , (3, 0, None, None) , 0 , )),
	(( 'CurrentADC' , 'pVal' , ), 322, (322, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 1160 , (3, 0, None, None) , 0 , )),
	(( 'CurrentADC' , 'pVal' , ), 322, (322, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 1168 , (3, 0, None, None) , 0 , )),
	(( 'AcquisitionCount' , 'pVal' , ), 323, (323, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 1176 , (3, 0, None, None) , 0 , )),
	(( 'AcquisitionCount' , 'pVal' , ), 323, (323, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 1184 , (3, 0, None, None) , 0 , )),
	(( 'SetMono' , 'iMono' , 'onExitPortAxial' , ), 324, (324, (), [ (9, 1, None, "IID('{3B59085A-B951-45C9-ABAD-41E8E96B8DE5}')") , 
			 (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 1192 , (3, 0, None, None) , 0 , )),
	(( 'SetMonoProperty' , 'whichProperty' , 'propVal' , ), 325, (325, (), [ (3, 1, None, None) , 
			 (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 1200 , (3, 0, None, None) , 0 , )),
	(( 'GetAxisAs' , 'dataObj' , 'whichAxis' , 'axisType' , 'axis' , 
			 ), 326, (326, (), [ (9, 1, None, "IID('{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')") , (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{75F30081-BED4-4B0A-AB8B-5D3DFEC775D2}')") , ], 1 , 1 , 4 , 0 , 1208 , (3, 0, None, None) , 0 , )),
	(( 'SetAreaSubtimer' , 'areaNum' , 'time' , ), 327, (327, (), [ (3, 1, None, None) , 
			 (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 1216 , (3, 0, None, None) , 0 , )),
	(( 'GetAreaSubtimer' , 'areaNum' , 'time' , ), 328, (328, (), [ (3, 1, None, None) , 
			 (16389, 2, None, None) , ], 1 , 1 , 4 , 0 , 1224 , (3, 0, None, None) , 0 , )),
	(( 'ChipDescription' , 'pVal' , ), 329, (329, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 1232 , (3, 0, None, None) , 0 , )),
	(( 'ChipDescription' , 'pVal' , ), 329, (329, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 1240 , (3, 0, None, None) , 0 , )),
	(( 'DarkSubtract' , 'doSubtraction' , ), 330, (330, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 1248 , (3, 0, None, None) , 0 , )),
	(( 'DarkSubtract' , 'doSubtraction' , ), 330, (330, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 1256 , (3, 0, None, None) , 0 , )),
	(( 'GetMono' , 'iMono' , ), 331, (331, (), [ (16393, 2, None, "IID('{3B59085A-B951-45C9-ABAD-41E8E96B8DE5}')") , ], 1 , 1 , 4 , 0 , 1264 , (3, 0, None, None) , 0 , )),
	(( 'GetWavelengthCoverage' , 'position' , 'Units' , 'start' , 'end' , 
			 ), 332, (332, (), [ (5, 1, None, None) , (3, 1, None, None) , (16389, 2, None, None) , (16389, 2, None, None) , ], 1 , 1 , 4 , 0 , 1272 , (3, 0, None, None) , 0 , )),
	(( 'ReadReferenceValue' , 'pRefVal' , ), 333, (333, (), [ (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 1280 , (3, 0, None, None) , 0 , )),
	(( 'SetReferenceGain' , 'gainToken' , ), 334, (334, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 1288 , (3, 0, None, None) , 0 , )),
	(( 'GetReferenceGain' , 'pGainToken' , ), 335, (335, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 1296 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstReferenceGain' , 'gainDescription' , 'pGainToken' , ), 336, (336, (), [ (16392, 2, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 1304 , (3, 0, None, None) , 0 , )),
	(( 'GetNextReferenceGain' , 'gainDescription' , 'pGainToken' , ), 337, (337, (), [ (16392, 2, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 1312 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceMode' , 'pRefMode' , ), 338, (338, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 1320 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceMode' , 'pRefMode' , ), 338, (338, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 1328 , (3, 0, None, None) , 0 , )),
	(( 'AutoNormalize' , 'pNormalize' , ), 339, (339, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 1336 , (3, 0, None, None) , 0 , )),
	(( 'AutoNormalize' , 'pNormalize' , ), 339, (339, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 1344 , (3, 0, None, None) , 0 , )),
	(( 'CalculateRangeModePositions' , 'desiredBegin' , 'desiredEnd' , 'pixelOverlap' , 'numCovers' , 
			 'positions' , ), 340, (340, (), [ (5, 1, None, None) , (5, 1, None, None) , (3, 1, None, None) , 
			 (16387, 2, None, None) , (16396, 2, None, None) , ], 1 , 1 , 4 , 0 , 1352 , (3, 0, None, None) , 0 , )),
	(( 'LedsOn' , 'pLedsOn' , ), 341, (341, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 1360 , (3, 0, None, None) , 0 , )),
	(( 'LedsOn' , 'pLedsOn' , ), 341, (341, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 1368 , (3, 0, None, None) , 0 , )),
	(( 'HasLaserControl' , 'pHasLaserControl' , ), 342, (342, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 1376 , (3, 0, None, None) , 0 , )),
	(( 'LaserEnabled' , 'pHasLaserControl' , ), 343, (343, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 1384 , (3, 0, None, None) , 0 , )),
	(( 'LaserEnabled' , 'pHasLaserControl' , ), 343, (343, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 1392 , (3, 0, None, None) , 0 , )),
	(( 'SetLaserProperty' , 'propToSet' , 'propVal' , ), 344, (344, (), [ (3, 1, None, None) , 
			 (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 1400 , (3, 0, None, None) , 0 , )),
	(( 'GetLaserProperty' , 'propToGet' , 'pPropVal' , ), 345, (345, (), [ (3, 1, None, None) , 
			 (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 1408 , (3, 0, None, None) , 0 , )),
	(( 'HasLampControl' , 'pHasLaserControl' , ), 346, (346, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 1416 , (3, 0, None, None) , 0 , )),
	(( 'LampEnabled' , 'pHasLaserControl' , ), 347, (347, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 1424 , (3, 0, None, None) , 0 , )),
	(( 'LampEnabled' , 'pHasLaserControl' , ), 347, (347, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 1432 , (3, 0, None, None) , 0 , )),
	(( 'SetLampProperty' , 'propToSet' , 'propVal' , ), 348, (348, (), [ (3, 1, None, None) , 
			 (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 1440 , (3, 0, None, None) , 0 , )),
	(( 'GetLampProperty' , 'propToGet' , 'pPropVal' , ), 349, (349, (), [ (3, 1, None, None) , 
			 (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 1448 , (3, 0, None, None) , 0 , )),
	(( 'LampFire' , ), 350, (350, (), [ ], 1 , 1 , 4 , 0 , 1456 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstCalibrationCoefficient' , 'coeff' , ), 351, (351, (), [ (16388, 10, None, None) , ], 1 , 1 , 4 , 0 , 1464 , (3, 0, None, None) , 0 , )),
	(( 'GetNextCalibrationCoefficient' , 'coeff' , ), 352, (352, (), [ (16388, 10, None, None) , ], 1 , 1 , 4 , 0 , 1472 , (3, 0, None, None) , 0 , )),
	(( 'LinearizationMode' , 'newMode' , ), 353, (353, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 1480 , (3, 0, None, None) , 0 , )),
	(( 'LinearizationMode' , 'newMode' , ), 353, (353, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 1488 , (3, 0, None, None) , 0 , )),
	(( 'SetLinearizationParams' , 'vtArrayFltParams' , ), 354, (354, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 1496 , (3, 0, None, None) , 0 , )),
	(( 'GetLinearizationParams' , 'vtArrayFltParams' , ), 355, (355, (), [ (16396, 2, None, None) , ], 1 , 1 , 4 , 0 , 1504 , (3, 0, None, None) , 0 , )),
	(( 'EMGain' , 'pVal' , ), 356, (356, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 1512 , (3, 0, None, None) , 0 , )),
	(( 'EMGain' , 'pVal' , ), 356, (356, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 1520 , (3, 0, None, None) , 0 , )),
	(( 'SetEMFitParams' , 'emParamCount' , 'vtArray' , ), 357, (357, (), [ (3, 1, None, None) , 
			 (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 1528 , (3, 0, None, None) , 0 , )),
	(( 'GetEMFitParams' , 'emParamCount' , 'vtArray' , ), 358, (358, (), [ (16387, 2, None, None) , 
			 (16396, 2, None, None) , ], 1 , 1 , 4 , 0 , 1536 , (3, 0, None, None) , 0 , )),
	(( 'GetEMState' , 'bEMState' , ), 359, (359, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1544 , (3, 0, None, None) , 0 , )),
	(( 'GetEMADCMode' , 'bEMADCMode' , ), 360, (360, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1552 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstParallelSpeed' , 'Description' , 'parallelSpeedToken' , ), 361, (361, (), [ (16392, 2, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 1560 , (3, 0, None, None) , 0 , )),
	(( 'GetNextParallelSpeed' , 'Description' , 'parallelSpeedToken' , ), 362, (362, (), [ (16392, 2, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 1568 , (3, 0, None, None) , 0 , )),
	(( 'CurrentParallelSpeed' , 'pVal' , ), 363, (363, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 1576 , (3, 0, None, None) , 0 , )),
	(( 'CurrentParallelSpeed' , 'pVal' , ), 363, (363, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 1584 , (3, 0, None, None) , 0 , )),
	(( 'GetChipReadoutLocationAndDirection' , 'readoutLD' , ), 364, (364, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 1592 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{0D684CA0-9552-4B26-B420-2BEE5BD4F1A0}' : IJYCCDReqd,
	'{A2C81A78-CA13-4A39-8FCB-CD51BD4E9376}' : _IJYDeviceReqdEvents,
	'{4D7AAEFC-19F9-49B7-A5BB-814933694FD3}' : JYMCD,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{0D684CA0-9552-4B26-B420-2BEE5BD4F1A0}' : 'IJYCCDReqd',
}


NamesToIIDMap = {
	'IJYCCDReqd' : '{0D684CA0-9552-4B26-B420-2BEE5BD4F1A0}',
	'_IJYDeviceReqdEvents' : '{A2C81A78-CA13-4A39-8FCB-CD51BD4E9376}',
}


