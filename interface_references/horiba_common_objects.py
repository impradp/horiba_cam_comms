# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.10.4 | packaged by conda-forge | (main, Mar 30 2022, 08:38:02) [MSC v.1916 64 bit (AMD64)]
# From type library 'JYCommonObjects.dll'
# On Fri Aug 12 15:10:53 2022
'JYCommonObjects 1.0 Type Library'
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

CLSID = IID('{9AA124CF-AF8F-4DF7-BF09-132D8E6EE792}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

from win32com.client import DispatchBaseClass
class IJYAnalysisReqd(DispatchBaseClass):
	'IJYAnalysisRequired Interface'
	CLSID = IID('{FAD86B05-955D-47D6-9061-A48D4D4A7C0D}')
	coclass_clsid = IID('{921802FD-513B-482F-A635-1CA0479BEB35}')

	# The method Amplitude is actually a property, but must be used as a method to correctly pass the arguments
	def Amplitude(self, numChannel=defaultNamedNotOptArg):
		'property Amplitude'
		return self._oleobj_.InvokeTypes(2211, LCID, 2, (5, 0), ((3, 1),),numChannel
			)

	def CalculateCZTransform(self, pData=defaultNamedNotOptArg, sampleIndex=defaultNamedNotOptArg):
		'method CalculateCZTransform'
		return self._oleobj_.InvokeTypes(2220, LCID, 1, (24, 0), ((16396, 1), (3, 1)),pData
			, sampleIndex)

	def CalculateClockFrequency(self, numFreq=defaultNamedNotOptArg, incFreq=defaultNamedNotOptArg, mValue=defaultNamedNotOptArg):
		'method CalculateClockFrequency'
		return self._oleobj_.InvokeTypes(2224, LCID, 1, (24, 0), ((3, 1), (5, 1), (2, 1)),numFreq
			, incFreq, mValue)

	def CalculateDSPParameters(self, numFreq=defaultNamedNotOptArg, startFreq=defaultNamedNotOptArg, intTime=defaultNamedNotOptArg, totalTime=defaultNamedNotOptArg):
		'method CalculateDSPParameters'
		return self._oleobj_.InvokeTypes(2225, LCID, 1, (24, 0), ((3, 1), (16389, 1), (5, 1), (5, 1)),numFreq
			, startFreq, intTime, totalTime)

	def CalculateFFT(self, pData=defaultNamedNotOptArg, sampleIndex=defaultNamedNotOptArg):
		'method CalculateFFT'
		return self._oleobj_.InvokeTypes(2228, LCID, 1, (24, 0), ((16396, 1), (3, 1)),pData
			, sampleIndex)

	def CalculateFinalLTADParameters(self, pData=pythoncom.Missing):
		'method CalculateFinalLTADParameters'
		return self._ApplyTypes_(2239, 1, (24, 0), ((16396, 2),), 'CalculateFinalLTADParameters', None,pData
			)

	def CalculateFinalLTParameters(self, pData=pythoncom.Missing):
		'method CalculateFinalLTParameters'
		return self._ApplyTypes_(2226, 1, (24, 0), ((16396, 2),), 'CalculateFinalLTParameters', None,pData
			)

	def CalculateFrequency(self, startFreq=defaultNamedNotOptArg, endFreq=defaultNamedNotOptArg, numFreq=defaultNamedNotOptArg, incFreq=defaultNamedNotOptArg
			, mValue=defaultNamedNotOptArg):
		'method CalculateFrequency'
		return self._oleobj_.InvokeTypes(2216, LCID, 1, (24, 0), ((5, 1), (5, 1), (3, 1), (3, 1), (2, 1)),startFreq
			, endFreq, numFreq, incFreq, mValue)

	def CalculateLTParameters(self, stdSampleNum=defaultNamedNotOptArg, unkSampleNum=defaultNamedNotOptArg, pData=pythoncom.Missing):
		'method CalculateLTParameters'
		return self._ApplyTypes_(2223, 1, (24, 0), ((3, 0), (3, 0), (16396, 2)), 'CalculateLTParameters', None,stdSampleNum
			, unkSampleNum, pData)

	def CalculateLTPolParameters(self, stdSampleNum=defaultNamedNotOptArg, unkSampleNum=defaultNamedNotOptArg, isKinetics=defaultNamedNotOptArg, pData=pythoncom.Missing):
		'method CalculateLTPolParameters'
		return self._ApplyTypes_(2237, 1, (24, 0), ((3, 0), (3, 0), (3, 1), (16396, 2)), 'CalculateLTPolParameters', None,stdSampleNum
			, unkSampleNum, isKinetics, pData)

	def CalculateMFFDisplayData(self, sampleIndex=defaultNamedNotOptArg, pData=pythoncom.Missing):
		'method CalculateMFFDisplayData'
		return self._ApplyTypes_(2221, 1, (24, 0), ((3, 1), (16396, 2)), 'CalculateMFFDisplayData', None,sampleIndex
			, pData)

	def CalculateSampleDataObject(self, sampleIndex=defaultNamedNotOptArg, pData=pythoncom.Missing):
		'method CalculateSampleDataObject'
		return self._ApplyTypes_(2229, 1, (24, 0), ((3, 1), (16396, 2)), 'CalculateSampleDataObject', None,sampleIndex
			, pData)

	def CalculateSampleParameters(self, sampleIndex=defaultNamedNotOptArg):
		'method CalculateSampleParameters'
		return self._oleobj_.InvokeTypes(2227, LCID, 1, (24, 0), ((3, 1),),sampleIndex
			)

	def CalculateSamplePolDataObject(self, sampleIndex=defaultNamedNotOptArg, polPosition=defaultNamedNotOptArg, pData=pythoncom.Missing):
		'method CalculateSamplePolDataObject'
		return self._ApplyTypes_(2238, 1, (24, 0), ((3, 1), (3, 1), (16396, 2)), 'CalculateSamplePolDataObject', None,sampleIndex
			, polPosition, pData)

	def CalculateSamplePolParameters(self, sampleIndex=defaultNamedNotOptArg, polPosition=defaultNamedNotOptArg, sampleNumber=defaultNamedNotOptArg, iKinetics=defaultNamedNotOptArg):
		'method CalculateSamplePolParameters'
		return self._oleobj_.InvokeTypes(2236, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (3, 1)),sampleIndex
			, polPosition, sampleNumber, iKinetics)

	def CalculateScale(self, startFreq=defaultNamedNotOptArg, endFreq=defaultNamedNotOptArg, numFreq=defaultNamedNotOptArg, hiScale=defaultNamedNotOptArg
			, loScale=defaultNamedNotOptArg, isSetA=defaultNamedNotOptArg, scaleType=defaultNamedNotOptArg):
		'method CalculateScale'
		return self._oleobj_.InvokeTypes(2217, LCID, 1, (24, 0), ((5, 1), (5, 1), (3, 1), (5, 1), (5, 1), (11, 1), (3, 1)),startFreq
			, endFreq, numFreq, hiScale, loScale, isSetA
			, scaleType)

	def CalculateStdDevs(self, pData=pythoncom.Missing):
		'method CalculateStdDevs'
		return self._ApplyTypes_(2222, 1, (24, 0), ((16396, 2),), 'CalculateStdDevs', None,pData
			)

	# The method ChannelFrequency is actually a property, but must be used as a method to correctly pass the arguments
	def ChannelFrequency(self, numChannel=defaultNamedNotOptArg):
		'property ChannelFrequency'
		return self._oleobj_.InvokeTypes(2209, LCID, 2, (5, 0), ((3, 1),),numChannel
			)

	# The method ClockMultiplier is actually a property, but must be used as a method to correctly pass the arguments
	def ClockMultiplier(self, numChannel=defaultNamedNotOptArg):
		'property ClockMultiplier'
		return self._oleobj_.InvokeTypes(2203, LCID, 2, (3, 0), ((3, 1),),numChannel
			)

	# The method FilterState is actually a property, but must be used as a method to correctly pass the arguments
	def FilterState(self, numChannel=defaultNamedNotOptArg):
		'property FilterState'
		return self._oleobj_.InvokeTypes(2207, LCID, 2, (2, 0), ((3, 1),),numChannel
			)

	def GetFilterValues(self, taVal=pythoncom.Missing):
		'method GetFilterValues'
		return self._ApplyTypes_(2232, 1, (2, 0), ((16386, 2),), 'GetFilterValues', None,taVal
			)

	def GetFinalLTADKineticsData(self, pData=pythoncom.Missing):
		'method GetFinalLTADKineticsData'
		return self._ApplyTypes_(2240, 1, (24, 0), ((16396, 2),), 'GetFinalLTADKineticsData', None,pData
			)

	def GetFinalLTAvgKineticsData(self, pData=pythoncom.Missing):
		'method GetFinalLTAvgKineticsData'
		return self._ApplyTypes_(2231, 1, (24, 0), ((16396, 2),), 'GetFinalLTAvgKineticsData', None,pData
			)

	def GetFinalLTKineticsData(self, pData=pythoncom.Missing):
		'method GetFinalLTKineticsData'
		return self._ApplyTypes_(2230, 1, (24, 0), ((16396, 2),), 'GetFinalLTKineticsData', None,pData
			)

	def GetLifetimeProperty(self, mffProperty=defaultNamedNotOptArg, pVal=pythoncom.Missing):
		'method GetLifetimeProperty'
		return self._ApplyTypes_(2219, 1, (24, 0), ((3, 1), (16389, 2)), 'GetLifetimeProperty', None,mffProperty
			, pVal)

	def GetNonZeroFreqCount(self):
		'method GetNonZeroFreqCount'
		return self._oleobj_.InvokeTypes(2235, LCID, 1, (3, 0), (),)

	# The method MBClockMultiplier is actually a property, but must be used as a method to correctly pass the arguments
	def MBClockMultiplier(self, numChannel=defaultNamedNotOptArg):
		'property MBClockMultiplier'
		return self._oleobj_.InvokeTypes(2213, LCID, 2, (3, 0), ((3, 1),),numChannel
			)

	# The method PhaseOffset is actually a property, but must be used as a method to correctly pass the arguments
	def PhaseOffset(self, numChannel=defaultNamedNotOptArg):
		'property PhaseOffset'
		return self._oleobj_.InvokeTypes(2210, LCID, 2, (5, 0), ((3, 1),),numChannel
			)

	def ResetLTParameters(self):
		'method ResetLTParameters'
		return self._oleobj_.InvokeTypes(2234, LCID, 1, (24, 0), (),)

	def ResetSampleParameters(self):
		'method ResetSampleParameters'
		return self._oleobj_.InvokeTypes(2233, LCID, 1, (24, 0), (),)

	# The method ScaleFactor is actually a property, but must be used as a method to correctly pass the arguments
	def ScaleFactor(self, numChannel=defaultNamedNotOptArg):
		'property ScaleFactor'
		return self._oleobj_.InvokeTypes(2206, LCID, 2, (5, 0), ((3, 1),),numChannel
			)

	# The method SetAmplitude is actually a property, but must be used as a method to correctly pass the arguments
	def SetAmplitude(self, numChannel=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		'property Amplitude'
		return self._oleobj_.InvokeTypes(2211, LCID, 4, (24, 0), ((3, 1), (5, 1)),numChannel
			, arg1)

	# The method SetChannelFrequency is actually a property, but must be used as a method to correctly pass the arguments
	def SetChannelFrequency(self, numChannel=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		'property ChannelFrequency'
		return self._oleobj_.InvokeTypes(2209, LCID, 4, (24, 0), ((3, 1), (5, 1)),numChannel
			, arg1)

	def SetChannelNumber(self, pVal=defaultNamedNotOptArg):
		'method SetChannelNumber'
		return self._oleobj_.InvokeTypes(2215, LCID, 1, (24, 0), ((3, 1),),pVal
			)

	# The method SetClockMultiplier is actually a property, but must be used as a method to correctly pass the arguments
	def SetClockMultiplier(self, numChannel=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		'property ClockMultiplier'
		return self._oleobj_.InvokeTypes(2203, LCID, 4, (24, 0), ((3, 1), (3, 1)),numChannel
			, arg1)

	# The method SetFilterState is actually a property, but must be used as a method to correctly pass the arguments
	def SetFilterState(self, numChannel=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		'property FilterState'
		return self._oleobj_.InvokeTypes(2207, LCID, 4, (24, 0), ((3, 1), (2, 1)),numChannel
			, arg1)

	def SetLifetimeProperty(self, mffProperty=defaultNamedNotOptArg, pVal=defaultNamedNotOptArg):
		'method SetLifetimeProperty'
		return self._oleobj_.InvokeTypes(2218, LCID, 1, (24, 0), ((3, 1), (5, 1)),mffProperty
			, pVal)

	# The method SetMBClockMultiplier is actually a property, but must be used as a method to correctly pass the arguments
	def SetMBClockMultiplier(self, numChannel=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		'property MBClockMultiplier'
		return self._oleobj_.InvokeTypes(2213, LCID, 4, (24, 0), ((3, 1), (3, 1)),numChannel
			, arg1)

	# The method SetPhaseOffset is actually a property, but must be used as a method to correctly pass the arguments
	def SetPhaseOffset(self, numChannel=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		'property PhaseOffset'
		return self._oleobj_.InvokeTypes(2210, LCID, 4, (24, 0), ((3, 1), (5, 1)),numChannel
			, arg1)

	# The method SetScaleFactor is actually a property, but must be used as a method to correctly pass the arguments
	def SetScaleFactor(self, numChannel=defaultNamedNotOptArg, arg1=defaultUnnamedArg):
		'property ScaleFactor'
		return self._oleobj_.InvokeTypes(2206, LCID, 4, (24, 0), ((3, 1), (5, 1)),numChannel
			, arg1)

	_prop_map_get_ = {
		"CalculationType": (2202, 2, (3, 0), (), "CalculationType", None),
		"CalibrationFactor": (2208, 2, (5, 0), (), "CalibrationFactor", None),
		"CrossCorrelationInc": (2214, 2, (5, 0), (), "CrossCorrelationInc", None),
		"FreqOrder": (2212, 2, (3, 0), (), "FreqOrder", None),
		"FreqRangeType": (2205, 2, (3, 0), (), "FreqRangeType", None),
		"OverSamplingRate": (2204, 2, (3, 0), (), "OverSamplingRate", None),
		"RandomMultiplier": (2201, 2, (5, 0), (), "RandomMultiplier", None),
	}
	_prop_map_put_ = {
		"CalculationType": ((2202, LCID, 4, 0),()),
		"CalibrationFactor": ((2208, LCID, 4, 0),()),
		"CrossCorrelationInc": ((2214, LCID, 4, 0),()),
		"FreqOrder": ((2212, LCID, 4, 0),()),
		"FreqRangeType": ((2205, LCID, 4, 0),()),
		"OverSamplingRate": ((2204, LCID, 4, 0),()),
		"RandomMultiplier": ((2201, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IJYAxis(DispatchBaseClass):
	'IJYAxis Interface'
	CLSID = IID('{75F30081-BED4-4B0A-AB8B-5D3DFEC775D2}')
	coclass_clsid = IID('{9ADFE718-3F8F-40A8-8B65-51CAA3229BA9}')

	def DumpToFile(self, FileName=defaultNamedNotOptArg):
		'method DumpToFile'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	def GetIndexNearestValue(self, value=defaultNamedNotOptArg):
		'method GetValueNearestIndex'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (3, 0), ((12, 1),),value
			)

	def GetLimits(self, min=pythoncom.Missing, max=pythoncom.Missing):
		'method GetLimits'
		return self._ApplyTypes_(2, 1, (24, 0), ((16387, 2), (16387, 2)), 'GetLimits', None,min
			, max)

	def GetValue(self, index=defaultNamedNotOptArg):
		'method GetValue'
		return self._ApplyTypes_(4, 1, (12, 0), ((3, 1),), 'GetValue', None,index
			)

	def GetValuesByArray(self, value=pythoncom.Missing):
		'method GetValuesByArray'
		return self._ApplyTypes_(6, 1, (24, 0), ((16396, 2),), 'GetValuesByArray', None,value
			)

	def SetLimits(self, min=defaultNamedNotOptArg, max=defaultNamedNotOptArg):
		'method SetLimits'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (24, 0), ((3, 1), (3, 1)),min
			, max)

	def SetValue(self, index=defaultNamedNotOptArg, value=defaultNamedNotOptArg):
		'method SetValue'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((3, 1), (12, 1)),index
			, value)

	def SetValuesByArray(self, value=defaultNamedNotOptArg):
		'method SetValuesByArray'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), ((12, 1),),value
			)

	_prop_map_get_ = {
		"Label": (8, 2, (8, 0), (), "Label", None),
		"Units": (9, 2, (3, 0), (), "Units", None),
	}
	_prop_map_put_ = {
		"Label": ((8, LCID, 4, 0),()),
		"Units": ((9, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IJYConverter(DispatchBaseClass):
	'IJYConverter Interface'
	CLSID = IID('{88E3B2DB-44E7-4E37-822B-17D3F604E069}')
	coclass_clsid = IID('{8EE4ADE9-81D7-4970-82FD-13BD5807172D}')

	def Convert(self, sourceVal=defaultNamedNotOptArg, convertFrom=defaultNamedNotOptArg, convertTo=defaultNamedNotOptArg):
		'method Convert'
		return self._ApplyTypes_(1, 1, (12, 0), ((12, 1), (3, 1), (3, 1)), 'Convert', None,sourceVal
			, convertFrom, convertTo)

	def ConvertToBaseGrating(self, posInCurrentGrating=defaultNamedNotOptArg, workingUnits=defaultNamedNotOptArg):
		'method ConvertToBaseGrating'
		return self._ApplyTypes_(12, 1, (12, 0), ((12, 1), (3, 1)), 'ConvertToBaseGrating', None,posInCurrentGrating
			, workingUnits)

	def GetFirstJYUnits(self, pVal=pythoncom.Missing, unitsString=pythoncom.Missing):
		'method GetFirstJYUnits'
		return self._ApplyTypes_(6, 1, (24, 0), ((16387, 2), (16396, 2)), 'GetFirstJYUnits', None,pVal
			, unitsString)

	def GetHardwareProperty(self, jyProperty=defaultNamedNotOptArg):
		'method GetHardwareProperty'
		return self._ApplyTypes_(3, 1, (12, 0), ((3, 1),), 'GetHardwareProperty', None,jyProperty
			)

	def GetHardwarePropertySlits(self, jyProperty=defaultNamedNotOptArg, whichSlit=defaultNamedNotOptArg):
		'method GetHardwarePropertySlits'
		return self._ApplyTypes_(9, 1, (12, 0), ((3, 1), (3, 1)), 'GetHardwarePropertySlits', None,jyProperty
			, whichSlit)

	def GetNextJYUnits(self, pVal=pythoncom.Missing, unitsString=pythoncom.Missing):
		'method GetNextJYUnits'
		return self._ApplyTypes_(7, 1, (24, 0), ((16387, 2), (16396, 2)), 'GetNextJYUnits', None,pVal
			, unitsString)

	def GetStringFromUnits(self, curUnits=defaultNamedNotOptArg):
		'method GetStringFromUnits'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(5, LCID, 1, (8, 0), ((3, 1),),curUnits
			)

	def GetStringFromUnitsType(self, unitsType=defaultNamedNotOptArg):
		'method GetStringFromUnitsType'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(11, LCID, 1, (8, 0), ((3, 1),),unitsType
			)

	def GetUnitsFromString(self, unitsString=defaultNamedNotOptArg):
		'method GetUnitsFromString'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (3, 0), ((8, 1),),unitsString
			)

	def RoundOff(self, unitsType=defaultNamedNotOptArg, curUnits=defaultNamedNotOptArg, curVal=defaultNamedNotOptArg, numDigits=defaultNamedNotOptArg
			, whichSlit=defaultNamedOptArg):
		'method RoundOff'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(13, LCID, 1, (8, 0), ((3, 1), (3, 1), (5, 1), (3, 1), (12, 17)),unitsType
			, curUnits, curVal, numDigits, whichSlit)

	def SetHardwareProperty(self, jyProperty=defaultNamedNotOptArg, newVal=defaultNamedNotOptArg):
		'method SetHardwareProperty'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((3, 1), (12, 1)),jyProperty
			, newVal)

	def SetHardwarePropertySlits(self, jyProperty=defaultNamedNotOptArg, whichSlit=defaultNamedNotOptArg, newVal=defaultNamedNotOptArg):
		'method SetHardwarePropertySlits'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), ((3, 1), (3, 1), (12, 1)),jyProperty
			, whichSlit, newVal)

	def ValidateHardwareProperty(self, devType=defaultNamedNotOptArg, subDevType=defaultNamedNotOptArg, subDevIndex=defaultNamedNotOptArg, targetVal=defaultNamedNotOptArg
			, targetUnits=defaultNamedNotOptArg):
		'method ValidateHardwareProperty'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), ((3, 1), (3, 1), (3, 1), (12, 1), (3, 1)),devType
			, subDevType, subDevIndex, targetVal, targetUnits)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IJYDataObject(DispatchBaseClass):
	'IJYDataObject Interface'
	CLSID = IID('{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')
	coclass_clsid = IID('{9C30FF28-6E5F-46BF-A402-54BD8252C9C1}')

	def ClearRleaseSafeDataArray(self, dataAsSafeArray=pythoncom.Missing):
		'method ClearRleaseSafeDataArray'
		return self._ApplyTypes_(33, 1, (24, 0), ((16396, 2),), 'ClearRleaseSafeDataArray', None,dataAsSafeArray
			)

	def ConvertToDouble(self):
		'method ConvertToDouble'
		return self._oleobj_.InvokeTypes(29, LCID, 1, (24, 0), (),)

	def DoOperation(self, operation=defaultNamedNotOptArg, operand1=defaultNamedNotOptArg, operand2=defaultNamedOptArg):
		'method DoOperation'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), ((3, 1), (12, 1), (12, 17)),operation
			, operand1, operand2)

	def DumpToFile(self, FileName=defaultNamedNotOptArg):
		'method DumpToFile'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	# Result is of type IJYAxis
	def GetAxis(self, whichDimension=defaultNamedNotOptArg):
		'method GetAxis'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), ((3, 1),),whichDimension
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetAxis', '{75F30081-BED4-4B0A-AB8B-5D3DFEC775D2}')
		return ret

	# Result is of type IJYDataObject
	def GetBinnedAsDataObject(self, newXBin=defaultNamedNotOptArg, newYBin=defaultNamedNotOptArg):
		'method GetBinnedAsDataObject'
		ret = self._oleobj_.InvokeTypes(26, LCID, 1, (9, 0), ((3, 1), (3, 1)),newXBin
			, newYBin)
		if ret is not None:
			ret = Dispatch(ret, 'GetBinnedAsDataObject', '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')
		return ret

	def GetCCDDataAppendMode(self):
		'method GetCCDDataAppendMode'
		return self._oleobj_.InvokeTypes(34, LCID, 1, (3, 0), (),)

	def GetCycle(self):
		'method GetCycle'
		return self._oleobj_.InvokeTypes(21, LCID, 1, (3, 0), (),)

	def GetDataAsArray(self, dataAsSafeArray=pythoncom.Missing, copy=defaultNamedOptArg, accumulation=defaultNamedOptArg):
		'method GetDataAsArray'
		return self._ApplyTypes_(18, 1, (24, 0), ((16396, 2), (12, 17), (12, 17)), 'GetDataAsArray', None,dataAsSafeArray
			, copy, accumulation)

	def GetDataBinned(self, xBin=defaultNamedNotOptArg, yBin=defaultNamedNotOptArg, binnedDataAsSafeArray=pythoncom.Missing):
		'method GetDataBinned'
		return self._ApplyTypes_(19, 1, (24, 0), ((3, 1), (3, 1), (16396, 2)), 'GetDataBinned', None,xBin
			, yBin, binnedDataAsSafeArray)

	def GetDataForAxisValue(self, axisValue=defaultNamedNotOptArg):
		'method GetDataForAxisValue'
		return self._ApplyTypes_(27, 1, (12, 0), ((12, 1),), 'GetDataForAxisValue', None,axisValue
			)

	def GetDimension(self, whichDimension=defaultNamedNotOptArg):
		'method GetDimension'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (3, 0), ((3, 1),),whichDimension
			)

	def GetElement(self, numDims=defaultNamedNotOptArg, elementDims=defaultNamedNotOptArg):
		'method GetElement'
		return self._ApplyTypes_(13, 1, (12, 0), ((3, 1), (16387, 1)), 'GetElement', None,numDims
			, elementDims)

	def GetFirstProperty(self, dataItemProp=pythoncom.Missing, dataItemVal=pythoncom.Missing, dataItemPropText=pythoncom.Missing):
		'method GetFirstProperty'
		return self._ApplyTypes_(31, 1, (24, 0), ((16387, 2), (16396, 2), (16396, 18)), 'GetFirstProperty', None,dataItemProp
			, dataItemVal, dataItemPropText)

	def GetNextProperty(self, dataItemProp=pythoncom.Missing, dataItemVal=pythoncom.Missing, dataItemPropText=pythoncom.Missing):
		'method GetNextProperty'
		return self._ApplyTypes_(32, 1, (24, 0), ((16387, 2), (16396, 2), (16396, 18)), 'GetNextProperty', None,dataItemProp
			, dataItemVal, dataItemPropText)

	def GetOffset(self, whichDimension=defaultNamedNotOptArg):
		'method GetOffset'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (3, 0), ((3, 1),),whichDimension
			)

	def GetPropertyValue(self, property=defaultNamedNotOptArg):
		'method GetPropertyValue'
		return self._ApplyTypes_(20, 1, (12, 0), ((3, 1),), 'GetPropertyValue', None,property
			)

	def GetRawData(self):
		'method GetRawData'
		return self._ApplyTypes_(8, 1, (12, 0), (), 'GetRawData', None,)

	def GetSubRegionAsArray(self, newXStart=defaultNamedNotOptArg, newXSize=defaultNamedNotOptArg, newYStart=defaultNamedNotOptArg, newYSize=defaultNamedNotOptArg
			, newXBin=defaultNamedNotOptArg, newYBin=defaultNamedNotOptArg):
		'method GetSubRegionAsArray'
		return self._ApplyTypes_(24, 1, (12, 0), ((3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1)), 'GetSubRegionAsArray', None,newXStart
			, newXSize, newYStart, newYSize, newXBin, newYBin
			)

	# Result is of type IJYDataObject
	def GetSubRegionAsDataObject(self, newXStart=defaultNamedNotOptArg, newXSize=defaultNamedNotOptArg, newYStart=defaultNamedNotOptArg, newYSize=defaultNamedNotOptArg
			, newXBin=defaultNamedNotOptArg, newYBin=defaultNamedNotOptArg):
		'method GetSubRegionAsDataObject'
		ret = self._oleobj_.InvokeTypes(25, LCID, 1, (9, 0), ((3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1)),newXStart
			, newXSize, newYStart, newYSize, newXBin, newYBin
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetSubRegionAsDataObject', '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')
		return ret

	def Load(self, FileName=defaultNamedNotOptArg):
		'method Load'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	def LoadSPCSubfile(self, FileName=defaultNamedNotOptArg, iSubFile=defaultNamedNotOptArg):
		'method LoadSPCSubfile'
		return self._oleobj_.InvokeTypes(30, LCID, 1, (24, 0), ((8, 1), (3, 1)),FileName
			, iSubFile)

	# Result is of type IJYDataObject
	def MakeCopy(self):
		'method MakeCopy'
		ret = self._oleobj_.InvokeTypes(22, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'MakeCopy', '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')
		return ret

	def MakeEven(self, makeEvenBasedOn=defaultNamedOptArg):
		'method MakeEven'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), ((12, 17),),makeEvenBasedOn
			)

	def OnAbort(self):
		'method OnAbort'
		return self._oleobj_.InvokeTypes(28, LCID, 1, (24, 0), (),)

	def PerformAnalysis(self, _MIDL__IJYDataObject0000_=defaultNamedNotOptArg, result=pythoncom.Missing):
		'method PerformAnalysis'
		return self._ApplyTypes_(17, 1, (24, 0), ((3, 1), (16396, 2)), 'PerformAnalysis', None,_MIDL__IJYDataObject0000_
			, result)

	def Save(self, FileName=defaultNamedNotOptArg):
		'method Save'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	def SetElement(self, numDims=defaultNamedNotOptArg, elementDims=defaultNamedNotOptArg, data=defaultNamedNotOptArg):
		'method SetElement'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (24, 0), ((3, 1), (16387, 1), (12, 1)),numDims
			, elementDims, data)

	_prop_map_get_ = {
		"DataFormat": (12, 2, (3, 0), (), "DataFormat", None),
		"DataLayout": (9, 2, (3, 0), (), "DataLayout", None),
		"Description": (16, 2, (8, 0), (), "Description", None),
		"Dimensions": (4, 2, (3, 0), (), "Dimensions", None),
		"FileType": (3, 2, (3, 0), (), "FileType", None),
		"NumberOfDimensions": (15, 2, (3, 0), (), "NumberOfDimensions", None),
	}
	_prop_map_put_ = {
		"Description": ((16, LCID, 4, 0),()),
		"FileType": ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IJYDataProvider(DispatchBaseClass):
	'IJYDataProvider Interface'
	CLSID = IID('{7135B4D1-2238-44D2-B97D-0EEEB291B85A}')
	coclass_clsid = IID('{9C30FF28-6E5F-46BF-A402-54BD8252C9C1}')

	def AppendDataObject(self, dataObject=defaultNamedNotOptArg):
		'method AppendDataObject'
		return self._oleobj_.InvokeTypes(510, LCID, 1, (24, 0), ((9, 1),),dataObject
			)

	def AppendDataPoint(self, dataPoint=defaultNamedNotOptArg):
		'method AppendDataPoint'
		return self._oleobj_.InvokeTypes(506, LCID, 1, (24, 0), ((12, 1),),dataPoint
			)

	def AppendDataPointAsArray(self, dataPoint=defaultNamedNotOptArg):
		'method AppendDataPointAsArray'
		return self._oleobj_.InvokeTypes(528, LCID, 1, (24, 0), ((12, 1),),dataPoint
			)

	def Clear(self):
		'method Clear'
		return self._oleobj_.InvokeTypes(505, LCID, 1, (24, 0), (),)

	def ClearEventMarkers(self):
		'method ClearEventMarkers'
		return self._oleobj_.InvokeTypes(530, LCID, 1, (24, 0), (),)

	def ClearRleaseSafeDataArray(self, dataAsSafeArray=pythoncom.Missing):
		'method ClearRleaseSafeDataArray'
		return self._ApplyTypes_(33, 1, (24, 0), ((16396, 2),), 'ClearRleaseSafeDataArray', None,dataAsSafeArray
			)

	def CommitOperation(self):
		'method CommitOperation'
		return self._oleobj_.InvokeTypes(514, LCID, 1, (24, 0), (),)

	def ConvertToDouble(self):
		'method ConvertToDouble'
		return self._oleobj_.InvokeTypes(29, LCID, 1, (24, 0), (),)

	def DoOperation(self, operation=defaultNamedNotOptArg, operand1=defaultNamedNotOptArg, operand2=defaultNamedOptArg):
		'method DoOperation'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), ((3, 1), (12, 1), (12, 17)),operation
			, operand1, operand2)

	def DumpToFile(self, FileName=defaultNamedNotOptArg):
		'method DumpToFile'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	def FlipX(self):
		'method FlipX'
		return self._oleobj_.InvokeTypes(522, LCID, 1, (24, 0), (),)

	# Result is of type IJYAxis
	def GetAxis(self, whichDimension=defaultNamedNotOptArg):
		'method GetAxis'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), ((3, 1),),whichDimension
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetAxis', '{75F30081-BED4-4B0A-AB8B-5D3DFEC775D2}')
		return ret

	# Result is of type IJYDataObject
	def GetBinnedAsDataObject(self, newXBin=defaultNamedNotOptArg, newYBin=defaultNamedNotOptArg):
		'method GetBinnedAsDataObject'
		ret = self._oleobj_.InvokeTypes(26, LCID, 1, (9, 0), ((3, 1), (3, 1)),newXBin
			, newYBin)
		if ret is not None:
			ret = Dispatch(ret, 'GetBinnedAsDataObject', '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')
		return ret

	def GetCCDDataAppendMode(self):
		'method GetCCDDataAppendMode'
		return self._oleobj_.InvokeTypes(34, LCID, 1, (3, 0), (),)

	def GetCurrentAccumulationIndex(self):
		'method GetCurrentAccumulationIndex'
		return self._oleobj_.InvokeTypes(523, LCID, 1, (3, 0), (),)

	def GetCurrentIndexByDimension(self, index=pythoncom.Missing, dim=defaultNamedNotOptArg):
		'method GetCurrentIndexByDimension'
		return self._ApplyTypes_(512, 1, (24, 0), ((16387, 2), (3, 1)), 'GetCurrentIndexByDimension', None,index
			, dim)

	def GetCycle(self):
		'method GetCycle'
		return self._oleobj_.InvokeTypes(21, LCID, 1, (3, 0), (),)

	def GetDataAsArray(self, dataAsSafeArray=pythoncom.Missing, copy=defaultNamedOptArg, accumulation=defaultNamedOptArg):
		'method GetDataAsArray'
		return self._ApplyTypes_(18, 1, (24, 0), ((16396, 2), (12, 17), (12, 17)), 'GetDataAsArray', None,dataAsSafeArray
			, copy, accumulation)

	def GetDataBinned(self, xBin=defaultNamedNotOptArg, yBin=defaultNamedNotOptArg, binnedDataAsSafeArray=pythoncom.Missing):
		'method GetDataBinned'
		return self._ApplyTypes_(19, 1, (24, 0), ((3, 1), (3, 1), (16396, 2)), 'GetDataBinned', None,xBin
			, yBin, binnedDataAsSafeArray)

	def GetDataForAxisValue(self, axisValue=defaultNamedNotOptArg):
		'method GetDataForAxisValue'
		return self._ApplyTypes_(27, 1, (12, 0), ((12, 1),), 'GetDataForAxisValue', None,axisValue
			)

	def GetDataPtr(self, dataPtr=pythoncom.Missing):
		'method GetDataPtr'
		return self._ApplyTypes_(508, 1, (24, 0), ((16396, 2),), 'GetDataPtr', None,dataPtr
			)

	def GetDimension(self, whichDimension=defaultNamedNotOptArg):
		'method GetDimension'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (3, 0), ((3, 1),),whichDimension
			)

	def GetElement(self, numDims=defaultNamedNotOptArg, elementDims=defaultNamedNotOptArg):
		'method GetElement'
		return self._ApplyTypes_(13, 1, (12, 0), ((3, 1), (16387, 1)), 'GetElement', None,numDims
			, elementDims)

	def GetEventMarker(self, eventInfo=pythoncom.Missing, dataIndex=defaultNamedNotOptArg, accumulation=defaultNamedNotOptArg):
		'method GetEventMarker'
		return self._ApplyTypes_(527, 1, (24, 0), ((16396, 2), (3, 17), (3, 17)), 'GetEventMarker', None,eventInfo
			, dataIndex, accumulation)

	def GetFirstEventMarker(self, eventInfo=pythoncom.Missing, dataPointIndex=pythoncom.Missing, accumluation=pythoncom.Missing):
		'method GetFirstEventMarker'
		return self._ApplyTypes_(524, 1, (24, 0), ((16396, 2), (16387, 2), (16387, 2)), 'GetFirstEventMarker', None,eventInfo
			, dataPointIndex, accumluation)

	def GetFirstProperty(self, property=pythoncom.Missing):
		'method GetFirstProperty'
		return self._ApplyTypes_(518, 1, (12, 0), ((16387, 2),), 'GetFirstProperty', None,property
			)

	def GetNextEventMarker(self, eventInfo=pythoncom.Missing, dataPointIndex=pythoncom.Missing, accumluation=pythoncom.Missing):
		'method GetNextEventMarker'
		return self._ApplyTypes_(525, 1, (24, 0), ((16396, 2), (16387, 2), (16387, 2)), 'GetNextEventMarker', None,eventInfo
			, dataPointIndex, accumluation)

	def GetNextProperty(self, property=pythoncom.Missing):
		'method GetNextProperty'
		return self._ApplyTypes_(519, 1, (12, 0), ((16387, 2),), 'GetNextProperty', None,property
			)

	def GetOffset(self, whichDimension=defaultNamedNotOptArg):
		'method GetOffset'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (3, 0), ((3, 1),),whichDimension
			)

	def GetPropertyValue(self, property=defaultNamedNotOptArg):
		'method GetPropertyValue'
		return self._ApplyTypes_(20, 1, (12, 0), ((3, 1),), 'GetPropertyValue', None,property
			)

	def GetRawData(self):
		'method GetRawData'
		return self._ApplyTypes_(8, 1, (12, 0), (), 'GetRawData', None,)

	def GetSubRegionAsArray(self, newXStart=defaultNamedNotOptArg, newXSize=defaultNamedNotOptArg, newYStart=defaultNamedNotOptArg, newYSize=defaultNamedNotOptArg
			, newXBin=defaultNamedNotOptArg, newYBin=defaultNamedNotOptArg):
		'method GetSubRegionAsArray'
		return self._ApplyTypes_(24, 1, (12, 0), ((3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1)), 'GetSubRegionAsArray', None,newXStart
			, newXSize, newYStart, newYSize, newXBin, newYBin
			)

	# Result is of type IJYDataObject
	def GetSubRegionAsDataObject(self, newXStart=defaultNamedNotOptArg, newXSize=defaultNamedNotOptArg, newYStart=defaultNamedNotOptArg, newYSize=defaultNamedNotOptArg
			, newXBin=defaultNamedNotOptArg, newYBin=defaultNamedNotOptArg):
		'method GetSubRegionAsDataObject'
		ret = self._oleobj_.InvokeTypes(25, LCID, 1, (9, 0), ((3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1)),newXStart
			, newXSize, newYStart, newYSize, newXBin, newYBin
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetSubRegionAsDataObject', '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')
		return ret

	def GlueDataObject(self, dataObject=defaultNamedNotOptArg, mode=defaultNamedNotOptArg, overlap=defaultNamedOptArg):
		'method GlueDataObject'
		return self._oleobj_.InvokeTypes(521, LCID, 1, (24, 0), ((9, 1), (3, 1), (12, 17)),dataObject
			, mode, overlap)

	def GroupDataObjects(self, dataObject=defaultNamedNotOptArg):
		'method GroupDataObjects'
		return self._oleobj_.InvokeTypes(529, LCID, 1, (24, 0), ((9, 1),),dataObject
			)

	def Initialize(self, format=defaultNamedNotOptArg, numDims=defaultNamedNotOptArg, dims=defaultNamedNotOptArg, accumMode=defaultNamedOptArg
			, numAccumulations=defaultNamedOptArg):
		'method Initialize'
		return self._oleobj_.InvokeTypes(500, LCID, 1, (24, 0), ((3, 1), (3, 1), (16387, 1), (12, 17), (12, 17)),format
			, numDims, dims, accumMode, numAccumulations)

	def Load(self, FileName=defaultNamedNotOptArg):
		'method Load'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	def LoadSPCSubfile(self, FileName=defaultNamedNotOptArg, iSubFile=defaultNamedNotOptArg):
		'method LoadSPCSubfile'
		return self._oleobj_.InvokeTypes(30, LCID, 1, (24, 0), ((8, 1), (3, 1)),FileName
			, iSubFile)

	# Result is of type IJYDataObject
	def MakeCopy(self):
		'method MakeCopy'
		ret = self._oleobj_.InvokeTypes(22, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'MakeCopy', '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')
		return ret

	def MakeEven(self, makeEvenBasedOn=defaultNamedOptArg):
		'method MakeEven'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), ((12, 17),),makeEvenBasedOn
			)

	def MakeFakeData(self, functionType=defaultNamedOptArg):
		'method MakeFakeData'
		return self._oleobj_.InvokeTypes(504, LCID, 1, (24, 0), ((12, 17),),functionType
			)

	# Result is of type IJYDataObject
	def MakeMirror(self):
		'method MakeMirror'
		ret = self._oleobj_.InvokeTypes(520, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'MakeMirror', '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')
		return ret

	def OnAbort(self):
		'method OnAbort'
		return self._oleobj_.InvokeTypes(28, LCID, 1, (24, 0), (),)

	def PerformAnalysis(self, _MIDL__IJYDataObject0000_=defaultNamedNotOptArg, result=pythoncom.Missing):
		'method PerformAnalysis'
		return self._ApplyTypes_(17, 1, (24, 0), ((3, 1), (16396, 2)), 'PerformAnalysis', None,_MIDL__IJYDataObject0000_
			, result)

	def Save(self, FileName=defaultNamedNotOptArg):
		'method Save'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	def SetAxis(self, whichDimension=defaultNamedNotOptArg, axis=defaultNamedNotOptArg, IsDefaultAxis=defaultNamedNotOptArg):
		'method SetAxis'
		return self._oleobj_.InvokeTypes(502, LCID, 1, (24, 0), ((3, 1), (9, 1), (3, 1)),whichDimension
			, axis, IsDefaultAxis)

	def SetElement(self, numDims=defaultNamedNotOptArg, elementDims=defaultNamedNotOptArg, data=defaultNamedNotOptArg):
		'method SetElement'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (24, 0), ((3, 1), (16387, 1), (12, 1)),numDims
			, elementDims, data)

	def SetEventMarker(self, eventInfo=defaultNamedNotOptArg):
		'method SetEventMarker'
		return self._oleobj_.InvokeTypes(526, LCID, 1, (24, 0), ((12, 1),),eventInfo
			)

	def SetOffset(self, whichDimension=defaultNamedNotOptArg, offsetValue=defaultNamedNotOptArg):
		'method SetOffset'
		return self._oleobj_.InvokeTypes(501, LCID, 1, (24, 0), ((3, 1), (3, 1)),whichDimension
			, offsetValue)

	def SetPropertyValue(self, property=defaultNamedNotOptArg, value=defaultNamedNotOptArg):
		'method SetPropertyValue'
		return self._oleobj_.InvokeTypes(513, LCID, 1, (24, 0), ((3, 1), (12, 1)),property
			, value)

	def SetRawData(self, rawData=defaultNamedNotOptArg):
		'method SetRawData'
		return self._oleobj_.InvokeTypes(503, LCID, 1, (24, 0), ((12, 1),),rawData
			)

	_prop_map_get_ = {
		"AccumulationCount": (517, 2, (3, 0), (), "AccumulationCount", None),
		"AccumulationIndex": (515, 2, (3, 0), (), "AccumulationIndex", None),
		"AppendMode": (511, 2, (3, 0), (), "AppendMode", None),
		"CurrentDataPointIndex": (507, 2, (3, 0), (), "CurrentDataPointIndex", None),
		"DataFormat": (12, 2, (3, 0), (), "DataFormat", None),
		"DataLayout": (9, 2, (3, 0), (), "DataLayout", None),
		"Description": (16, 2, (8, 0), (), "Description", None),
		"Dimensions": (4, 2, (3, 0), (), "Dimensions", None),
		"FileType": (3, 2, (3, 0), (), "FileType", None),
		"NumberOfDimensions": (15, 2, (3, 0), (), "NumberOfDimensions", None),
		"SignalIndex": (509, 2, (3, 0), (), "SignalIndex", None),
	}
	_prop_map_put_ = {
		"AccumulationCount": ((517, LCID, 4, 0),()),
		"AccumulationIndex": ((515, LCID, 4, 0),()),
		"AppendMode": ((511, LCID, 4, 0),()),
		"CurrentDataPointIndex": ((507, LCID, 4, 0),()),
		"Cycle": ((516, LCID, 4, 0),()),
		"Description": ((16, LCID, 4, 0),()),
		"FileType": ((3, LCID, 4, 0),()),
		"SignalIndex": ((509, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IJYEventInfo(DispatchBaseClass):
	'IJYEventInfo Interface'
	CLSID = IID('{F7D651D7-D95D-4D49-A2BD-789987BF1D22}')
	coclass_clsid = IID('{81697F83-4E1C-45E2-985E-373BA254BD60}')

	def AttachData(self, dataObject=defaultNamedNotOptArg):
		'method AttachData'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), ((9, 1),),dataObject
			)

	def AttachResults(self, resultsObject=defaultNamedNotOptArg):
		'method AttachResults'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), ((9, 1),),resultsObject
			)

	# Result is of type IJYResultsObject
	def GetResult(self):
		'method GetResult'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetResult', '{3948DB1C-95F8-4F57-AE15-2A5FC0B04CF1}')
		return ret

	_prop_map_get_ = {
		"Description": (2, 2, (8, 0), (), "Description", None),
		# Method 'Source' returns object of type 'IJYDeviceReqd'
		"Source": (1, 2, (9, 0), (), "Source", '{7C269B67-FABB-4998-B00F-A43043E6F86C}'),
		"Val": (3, 2, (12, 0), (), "Val", None),
	}
	_prop_map_put_ = {
		"Description": ((2, LCID, 4, 0),()),
		"Source": ((1, LCID, 4, 0),()),
		"Val": ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IJYLogger(DispatchBaseClass):
	'IJYLogger Interface'
	CLSID = IID('{572C08BD-7991-43A9-924C-DC4C670DF2FD}')
	coclass_clsid = IID('{D4CE928C-6ED8-4A73-B406-92AF84B69C1F}')

	def Log(self, level=defaultNamedNotOptArg, formatString=defaultNamedNotOptArg, functionName=defaultNamedNotOptArg, vt1=defaultNamedOptArg
			, vt2=defaultNamedOptArg, vt3=defaultNamedOptArg, vt4=defaultNamedOptArg, vt5=defaultNamedOptArg):
		'method Log'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (24, 0), ((3, 1), (8, 1), (8, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),level
			, formatString, functionName, vt1, vt2, vt3
			, vt4, vt5)

	_prop_map_get_ = {
		"FileName": (2, 2, (8, 0), (), "FileName", None),
		"FilePath": (3, 2, (8, 0), (), "FilePath", None),
		"LoggingLevel": (4, 2, (3, 0), (), "LoggingLevel", None),
		"MaxBackupFiles": (5, 2, (3, 0), (), "MaxBackupFiles", None),
		"MaxFileSizeKB": (6, 2, (3, 0), (), "MaxFileSizeKB", None),
	}
	_prop_map_put_ = {
		"FileName": ((2, LCID, 4, 0),()),
		"FilePath": ((3, LCID, 4, 0),()),
		"LoggingLevel": ((4, LCID, 4, 0),()),
		"MaxBackupFiles": ((5, LCID, 4, 0),()),
		"MaxFileSizeKB": ((6, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IJYResultsObject(DispatchBaseClass):
	'IJYResultsObject Interface'
	CLSID = IID('{3948DB1C-95F8-4F57-AE15-2A5FC0B04CF1}')
	coclass_clsid = IID('{F58ACFF4-2B84-4755-A967-38DA7202D6DE}')

	def AppendOverlayFile(self, FileName=defaultNamedNotOptArg, identifier=defaultNamedNotOptArg):
		'method AppendOverlayFile'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (24, 0), ((8, 1), (8, 1)),FileName
			, identifier)

	def DoOperation(self, operation=defaultNamedNotOptArg, operand1=defaultNamedNotOptArg, operand2=defaultNamedOptArg):
		'method DoOperation'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), ((3, 1), (12, 1), (12, 17)),operation
			, operand1, operand2)

	def DumpToFile(self, FileName=defaultNamedNotOptArg):
		'method DumpToFile'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), ((8, 0),),FileName
			)

	def FinalizeResult(self):
		'method FinalizeResult'
		return self._oleobj_.InvokeTypes(26, LCID, 1, (24, 0), (),)

	def GetDataObjectByIndex(self, dataObjectIndex=defaultNamedNotOptArg, dataObj=pythoncom.Missing):
		'method GetDataObjectByIndex'
		return self._ApplyTypes_(12, 1, (24, 0), ((3, 1), (16393, 2)), 'GetDataObjectByIndex', None,dataObjectIndex
			, dataObj)

	def GetDataSetName(self, dataSetIdx=defaultNamedNotOptArg):
		'method GetDataSetName'
		return self._oleobj_.InvokeTypes(21, LCID, 1, (5, 0), ((3, 1),),dataSetIdx
			)

	# Result is of type IJYDataObject
	def GetFirstDarkDataObject(self):
		'method GetFirstDarkDataObject'
		ret = self._oleobj_.InvokeTypes(32, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetFirstDarkDataObject', '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')
		return ret

	# Result is of type IJYDataObject
	def GetFirstDataObject(self):
		'method GetFirstDataObject'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetFirstDataObject', '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')
		return ret

	# Result is of type IJYDataObject
	def GetFirstDataObjectByCycle(self, cycleNumber=defaultNamedNotOptArg):
		'method GetFirstDataObjectByCycle'
		ret = self._oleobj_.InvokeTypes(24, LCID, 1, (9, 0), ((3, 1),),cycleNumber
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetFirstDataObjectByCycle', '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')
		return ret

	# Result is of type IJYDataObject
	def GetFirstDataObjectBySource(self, dataSource=defaultNamedNotOptArg):
		'method GetFirstDataObjectBySource'
		ret = self._oleobj_.InvokeTypes(29, LCID, 1, (9, 0), ((12, 1),),dataSource
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetFirstDataObjectBySource', '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')
		return ret

	# Result is of type IJYDataObject
	def GetFirstDataObjectFromDataSet(self, dataSetIdx=defaultNamedNotOptArg):
		'method GetFirstDataObjectFromDataSet'
		ret = self._oleobj_.InvokeTypes(19, LCID, 1, (9, 0), ((3, 1),),dataSetIdx
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetFirstDataObjectFromDataSet', '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')
		return ret

	def GetFirstDataSource(self):
		'method GetFirstDataSource'
		return self._ApplyTypes_(27, 1, (12, 0), (), 'GetFirstDataSource', None,)

	# Result is of type IJYDataObject
	def GetFirstOverlay(self, identifier=pythoncom.Missing):
		'method GetFirstOverlay'
		return self._ApplyTypes_(17, 1, (9, 0), ((16396, 2),), 'GetFirstOverlay', '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}',identifier
			)

	# Result is of type IJYDataObject
	def GetFirstPreAcqDataObject(self):
		'method GetFirstPreAcqDataObject'
		ret = self._oleobj_.InvokeTypes(34, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetFirstPreAcqDataObject', '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')
		return ret

	# Result is of type IJYDataObject
	def GetFirstRawDataObject(self):
		'method GetFirstRawDataObject'
		ret = self._oleobj_.InvokeTypes(22, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetFirstRawDataObject', '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')
		return ret

	# Result is of type IJYDataObject
	def GetNextDarkDataObject(self):
		'method GetNextDarkDataObject'
		ret = self._oleobj_.InvokeTypes(33, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetNextDarkDataObject', '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')
		return ret

	# Result is of type IJYDataObject
	def GetNextDataObject(self):
		'method GetNextDataObject'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetNextDataObject', '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')
		return ret

	# Result is of type IJYDataObject
	def GetNextDataObjectByCycle(self, cycleNumber=defaultNamedNotOptArg):
		'method GetNextDataObjectByCycle'
		ret = self._oleobj_.InvokeTypes(25, LCID, 1, (9, 0), ((3, 1),),cycleNumber
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetNextDataObjectByCycle', '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')
		return ret

	# Result is of type IJYDataObject
	def GetNextDataObjectBySource(self, dataSource=defaultNamedNotOptArg):
		'method GetNextDataObjectBySource'
		ret = self._oleobj_.InvokeTypes(30, LCID, 1, (9, 0), ((12, 1),),dataSource
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetNextDataObjectBySource', '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')
		return ret

	# Result is of type IJYDataObject
	def GetNextDataObjectFromDataSet(self, dataSetIdx=defaultNamedNotOptArg):
		'method GetNextDataObjectFromDataSet'
		ret = self._oleobj_.InvokeTypes(20, LCID, 1, (9, 0), ((3, 1),),dataSetIdx
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetNextDataObjectFromDataSet', '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')
		return ret

	def GetNextDataSource(self):
		'method GetNextDataSource'
		return self._ApplyTypes_(28, 1, (12, 0), (), 'GetNextDataSource', None,)

	# Result is of type IJYDataObject
	def GetNextOverlay(self, identifier=pythoncom.Missing):
		'method GetNextOverlay'
		return self._ApplyTypes_(18, 1, (9, 0), ((16396, 2),), 'GetNextOverlay', '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}',identifier
			)

	# Result is of type IJYDataObject
	def GetNextPreAcqDataObject(self):
		'method GetNextPreAcqDataObject'
		ret = self._oleobj_.InvokeTypes(35, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetNextPreAcqDataObject', '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')
		return ret

	# Result is of type IJYDataObject
	def GetNextRawDataObject(self):
		'method GetNextRawDataObject'
		ret = self._oleobj_.InvokeTypes(23, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetNextRawDataObject', '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')
		return ret

	def GetProperty(self, whichProperty=defaultNamedNotOptArg):
		'method GetProperty'
		return self._ApplyTypes_(13, 1, (12, 0), ((3, 1),), 'GetProperty', None,whichProperty
			)

	def GetSourceCount(self):
		'method GetSourceCount'
		return self._oleobj_.InvokeTypes(31, LCID, 1, (3, 0), (),)

	def InterpretAsImage(self, maxXCount=defaultNamedNotOptArg, maxYCount=defaultNamedNotOptArg, image=pythoncom.Missing):
		'method InterpretAsImage'
		return self._ApplyTypes_(11, 1, (24, 0), ((3, 1), (3, 1), (16396, 2)), 'InterpretAsImage', None,maxXCount
			, maxYCount, image)

	def Load(self, FileName=defaultNamedNotOptArg):
		'method Load'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	# Result is of type IJYResultsObject
	def MakeCopy(self):
		'method MakeCopy'
		ret = self._oleobj_.InvokeTypes(15, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'MakeCopy', '{3948DB1C-95F8-4F57-AE15-2A5FC0B04CF1}')
		return ret

	def Save(self, FileName=defaultNamedNotOptArg):
		'method Save'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	_prop_map_get_ = {
		"CurrentCycle": (14, 2, (3, 0), (), "CurrentCycle", None),
		"DataObjectCount": (10, 2, (3, 0), (), "DataObjectCount", None),
		"Description": (7, 2, (8, 0), (), "Description", None),
		"FileType": (6, 2, (3, 0), (), "FileType", None),
	}
	_prop_map_put_ = {
		"Description": ((7, LCID, 4, 0),()),
		"FileType": ((6, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IJYResultsProvider(DispatchBaseClass):
	'IJYResultsProvider Interface'
	CLSID = IID('{5EF255B2-C040-4801-84FF-BD1C2679F3A8}')
	coclass_clsid = IID('{F58ACFF4-2B84-4755-A967-38DA7202D6DE}')

	def AppendDataObject(self, dataObj=defaultNamedNotOptArg, dataObjId=defaultNamedOptArg):
		'method AppendDataObject'
		return self._oleobj_.InvokeTypes(501, LCID, 1, (24, 0), ((9, 1), (12, 17)),dataObj
			, dataObjId)

	def AppendOverlayFile(self, FileName=defaultNamedNotOptArg, identifier=defaultNamedNotOptArg):
		'method AppendOverlayFile'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (24, 0), ((8, 1), (8, 1)),FileName
			, identifier)

	def AppendRawDataObject(self, dataObj=defaultNamedNotOptArg, dataObjId=defaultNamedOptArg):
		'method AppendRawDataObject'
		return self._oleobj_.InvokeTypes(512, LCID, 1, (24, 0), ((9, 1), (12, 17)),dataObj
			, dataObjId)

	def AppendResult(self, resultInterface=defaultNamedNotOptArg):
		'method AppendResult'
		return self._oleobj_.InvokeTypes(500, LCID, 1, (24, 0), ((9, 1),),resultInterface
			)

	def AppendUpdate(self, resultInterface=defaultNamedNotOptArg):
		'method AppendUpdate'
		return self._oleobj_.InvokeTypes(508, LCID, 1, (24, 0), ((9, 1),),resultInterface
			)

	def Clear(self):
		'method Clear'
		return self._oleobj_.InvokeTypes(505, LCID, 1, (24, 0), (),)

	def ClearDataObjectsMap(self):
		'method ClearDataObjectsMap'
		return self._oleobj_.InvokeTypes(514, LCID, 1, (24, 0), (),)

	def DoOperation(self, operation=defaultNamedNotOptArg, operand1=defaultNamedNotOptArg, operand2=defaultNamedOptArg):
		'method DoOperation'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), ((3, 1), (12, 1), (12, 17)),operation
			, operand1, operand2)

	def DumpToFile(self, FileName=defaultNamedNotOptArg):
		'method DumpToFile'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), ((8, 0),),FileName
			)

	def FinalizeResult(self):
		'method FinalizeResult'
		return self._oleobj_.InvokeTypes(26, LCID, 1, (24, 0), (),)

	def GetDataObjectById(self, dataObjId=defaultNamedNotOptArg, dataObj=pythoncom.Missing, Cycle=defaultNamedOptArg):
		'method GetDataObjectById'
		return self._ApplyTypes_(502, 1, (24, 0), ((12, 1), (16393, 2), (12, 17)), 'GetDataObjectById', None,dataObjId
			, dataObj, Cycle)

	def GetDataObjectByIndex(self, dataObjectIndex=defaultNamedNotOptArg, dataObj=pythoncom.Missing):
		'method GetDataObjectByIndex'
		return self._ApplyTypes_(12, 1, (24, 0), ((3, 1), (16393, 2)), 'GetDataObjectByIndex', None,dataObjectIndex
			, dataObj)

	def GetDataSetName(self, dataSetIdx=defaultNamedNotOptArg):
		'method GetDataSetName'
		return self._oleobj_.InvokeTypes(21, LCID, 1, (5, 0), ((3, 1),),dataSetIdx
			)

	# Result is of type IJYDataObject
	def GetFirstDarkDataObject(self):
		'method GetFirstDarkDataObject'
		ret = self._oleobj_.InvokeTypes(32, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetFirstDarkDataObject', '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')
		return ret

	# Result is of type IJYDataObject
	def GetFirstDataObject(self):
		'method GetFirstDataObject'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetFirstDataObject', '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')
		return ret

	# Result is of type IJYDataObject
	def GetFirstDataObjectByCycle(self, cycleNumber=defaultNamedNotOptArg):
		'method GetFirstDataObjectByCycle'
		ret = self._oleobj_.InvokeTypes(24, LCID, 1, (9, 0), ((3, 1),),cycleNumber
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetFirstDataObjectByCycle', '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')
		return ret

	# Result is of type IJYDataObject
	def GetFirstDataObjectBySource(self, dataSource=defaultNamedNotOptArg):
		'method GetFirstDataObjectBySource'
		ret = self._oleobj_.InvokeTypes(29, LCID, 1, (9, 0), ((12, 1),),dataSource
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetFirstDataObjectBySource', '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')
		return ret

	# Result is of type IJYDataObject
	def GetFirstDataObjectFromDataSet(self, dataSetIdx=defaultNamedNotOptArg):
		'method GetFirstDataObjectFromDataSet'
		ret = self._oleobj_.InvokeTypes(19, LCID, 1, (9, 0), ((3, 1),),dataSetIdx
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetFirstDataObjectFromDataSet', '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')
		return ret

	def GetFirstDataSource(self):
		'method GetFirstDataSource'
		return self._ApplyTypes_(27, 1, (12, 0), (), 'GetFirstDataSource', None,)

	# Result is of type IJYDataObject
	def GetFirstOverlay(self, identifier=pythoncom.Missing):
		'method GetFirstOverlay'
		return self._ApplyTypes_(17, 1, (9, 0), ((16396, 2),), 'GetFirstOverlay', '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}',identifier
			)

	# Result is of type IJYDataObject
	def GetFirstPreAcqDataObject(self):
		'method GetFirstPreAcqDataObject'
		ret = self._oleobj_.InvokeTypes(34, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetFirstPreAcqDataObject', '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')
		return ret

	# Result is of type IJYDataObject
	def GetFirstRawDataObject(self):
		'method GetFirstRawDataObject'
		ret = self._oleobj_.InvokeTypes(22, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetFirstRawDataObject', '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')
		return ret

	# Result is of type IJYDataObject
	def GetNextDarkDataObject(self):
		'method GetNextDarkDataObject'
		ret = self._oleobj_.InvokeTypes(33, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetNextDarkDataObject', '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')
		return ret

	# Result is of type IJYDataObject
	def GetNextDataObject(self):
		'method GetNextDataObject'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetNextDataObject', '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')
		return ret

	# Result is of type IJYDataObject
	def GetNextDataObjectByCycle(self, cycleNumber=defaultNamedNotOptArg):
		'method GetNextDataObjectByCycle'
		ret = self._oleobj_.InvokeTypes(25, LCID, 1, (9, 0), ((3, 1),),cycleNumber
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetNextDataObjectByCycle', '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')
		return ret

	# Result is of type IJYDataObject
	def GetNextDataObjectBySource(self, dataSource=defaultNamedNotOptArg):
		'method GetNextDataObjectBySource'
		ret = self._oleobj_.InvokeTypes(30, LCID, 1, (9, 0), ((12, 1),),dataSource
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetNextDataObjectBySource', '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')
		return ret

	# Result is of type IJYDataObject
	def GetNextDataObjectFromDataSet(self, dataSetIdx=defaultNamedNotOptArg):
		'method GetNextDataObjectFromDataSet'
		ret = self._oleobj_.InvokeTypes(20, LCID, 1, (9, 0), ((3, 1),),dataSetIdx
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetNextDataObjectFromDataSet', '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')
		return ret

	def GetNextDataSource(self):
		'method GetNextDataSource'
		return self._ApplyTypes_(28, 1, (12, 0), (), 'GetNextDataSource', None,)

	# Result is of type IJYDataObject
	def GetNextOverlay(self, identifier=pythoncom.Missing):
		'method GetNextOverlay'
		return self._ApplyTypes_(18, 1, (9, 0), ((16396, 2),), 'GetNextOverlay', '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}',identifier
			)

	# Result is of type IJYDataObject
	def GetNextPreAcqDataObject(self):
		'method GetNextPreAcqDataObject'
		ret = self._oleobj_.InvokeTypes(35, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetNextPreAcqDataObject', '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')
		return ret

	# Result is of type IJYDataObject
	def GetNextRawDataObject(self):
		'method GetNextRawDataObject'
		ret = self._oleobj_.InvokeTypes(23, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetNextRawDataObject', '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')
		return ret

	def GetProperty(self, whichProperty=defaultNamedNotOptArg):
		'method GetProperty'
		return self._ApplyTypes_(13, 1, (12, 0), ((3, 1),), 'GetProperty', None,whichProperty
			)

	def GetSourceCount(self):
		'method GetSourceCount'
		return self._oleobj_.InvokeTypes(31, LCID, 1, (3, 0), (),)

	def GlueResult(self, resultsObject=defaultNamedNotOptArg, mode=defaultNamedNotOptArg, overlap=defaultNamedOptArg):
		'method GlueResult'
		return self._oleobj_.InvokeTypes(511, LCID, 1, (24, 0), ((9, 1), (3, 1), (12, 17)),resultsObject
			, mode, overlap)

	def GroupDataObjects(self):
		'method GroupDataObjects'
		return self._oleobj_.InvokeTypes(513, LCID, 1, (24, 0), (),)

	def Initialize(self, numCycles=defaultNamedOptArg):
		'method Initialize'
		return self._oleobj_.InvokeTypes(504, LCID, 1, (24, 0), ((12, 17),),numCycles
			)

	def InterpretAsImage(self, maxXCount=defaultNamedNotOptArg, maxYCount=defaultNamedNotOptArg, image=pythoncom.Missing):
		'method InterpretAsImage'
		return self._ApplyTypes_(11, 1, (24, 0), ((3, 1), (3, 1), (16396, 2)), 'InterpretAsImage', None,maxXCount
			, maxYCount, image)

	def Load(self, FileName=defaultNamedNotOptArg):
		'method Load'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	# Result is of type IJYResultsObject
	def MakeCopy(self):
		'method MakeCopy'
		ret = self._oleobj_.InvokeTypes(15, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'MakeCopy', '{3948DB1C-95F8-4F57-AE15-2A5FC0B04CF1}')
		return ret

	def MakeFakeResult(self, DataFormat=defaultNamedNotOptArg, numDataObjects=defaultNamedNotOptArg, dimsPerDataObject=defaultNamedNotOptArg, dataObjectDims=defaultNamedNotOptArg):
		'method MakeFakeResult'
		return self._oleobj_.InvokeTypes(506, LCID, 1, (24, 0), ((3, 1), (3, 1), (3, 1), (16387, 1)),DataFormat
			, numDataObjects, dimsPerDataObject, dataObjectDims)

	def Save(self, FileName=defaultNamedNotOptArg):
		'method Save'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	def SetProperty(self, whichProperty=defaultNamedNotOptArg, value=defaultNamedNotOptArg):
		'method SetProperty'
		return self._oleobj_.InvokeTypes(507, LCID, 1, (24, 0), ((3, 1), (12, 1)),whichProperty
			, value)

	def WriteExperimentInfo(self, FileName=defaultNamedNotOptArg):
		'method WriteExperimentInfo'
		return self._oleobj_.InvokeTypes(503, LCID, 1, (24, 0), ((8, 1),),FileName
			)

	_prop_map_get_ = {
		"CurrentCycle": (14, 2, (3, 0), (), "CurrentCycle", None),
		"CycleCount": (510, 2, (3, 0), (), "CycleCount", None),
		"DataObjectCount": (10, 2, (3, 0), (), "DataObjectCount", None),
		"Description": (7, 2, (8, 0), (), "Description", None),
		"FileType": (6, 2, (3, 0), (), "FileType", None),
	}
	_prop_map_put_ = {
		"CurrentCycle": ((509, LCID, 4, 0),()),
		"Description": ((7, LCID, 4, 0),()),
		"FileType": ((6, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

from win32com.client import CoClassBaseClass
# This CoClass is known by the name 'JYCommonObjects.JYAnalysis.1'
class JYAnalysis(CoClassBaseClass): # A CoClass
	# JYAnalysis Class
	CLSID = IID('{921802FD-513B-482F-A635-1CA0479BEB35}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IJYAnalysisReqd,
	]
	default_interface = IJYAnalysisReqd

# This CoClass is known by the name 'JYCommonObjects.JYAxisInterface.1'
class JYAxisInterface(CoClassBaseClass): # A CoClass
	# JYAxisInterface Class
	CLSID = IID('{9ADFE718-3F8F-40A8-8B65-51CAA3229BA9}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IJYAxis,
	]
	default_interface = IJYAxis

# This CoClass is known by the name 'JYCommonObjects.JYConverterInterface.1'
class JYConverterInterface(CoClassBaseClass): # A CoClass
	# JYConverterInterface Class
	CLSID = IID('{8EE4ADE9-81D7-4970-82FD-13BD5807172D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IJYConverter,
	]
	default_interface = IJYConverter

# This CoClass is known by the name 'JYCommonObjects.JYDataInterface.1'
class JYDataInterface(CoClassBaseClass): # A CoClass
	# JYDataInterface Class
	CLSID = IID('{9C30FF28-6E5F-46BF-A402-54BD8252C9C1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IJYDataObject,
		IJYDataProvider,
	]
	default_interface = IJYDataObject

# This CoClass is known by the name 'JYCommonObjects.JYEventInfo.1'
class JYEventInfo(CoClassBaseClass): # A CoClass
	# JYEventInfo Class
	CLSID = IID('{81697F83-4E1C-45E2-985E-373BA254BD60}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IJYEventInfo,
	]
	default_interface = IJYEventInfo

class JYLoggerInterface(CoClassBaseClass): # A CoClass
	# JYLoggerInterface Class
	CLSID = IID('{D4CE928C-6ED8-4A73-B406-92AF84B69C1F}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IJYLogger,
	]
	default_interface = IJYLogger

# This CoClass is known by the name 'JYCommonObjects.JYResultsInterface.1'
class JYResultsInterface(CoClassBaseClass): # A CoClass
	# JYResultsInterface Class
	CLSID = IID('{F58ACFF4-2B84-4755-A967-38DA7202D6DE}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IJYResultsObject,
		IJYResultsProvider,
	]
	default_interface = IJYResultsObject

IJYAnalysisReqd_vtables_dispatch_ = 1
IJYAnalysisReqd_vtables_ = [
	(( 'RandomMultiplier' , 'pVal' , ), 2201, (2201, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'RandomMultiplier' , 'pVal' , ), 2201, (2201, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'CalculationType' , 'pVal' , ), 2202, (2202, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'CalculationType' , 'pVal' , ), 2202, (2202, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ClockMultiplier' , 'numChannel' , 'pVal' , ), 2203, (2203, (), [ (3, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ClockMultiplier' , 'numChannel' , 'pVal' , ), 2203, (2203, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'OverSamplingRate' , 'pVal' , ), 2204, (2204, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'OverSamplingRate' , 'pVal' , ), 2204, (2204, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'FreqRangeType' , 'pVal' , ), 2205, (2205, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'FreqRangeType' , 'pVal' , ), 2205, (2205, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'ScaleFactor' , 'numChannel' , 'pVal' , ), 2206, (2206, (), [ (3, 1, None, None) , 
			 (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'ScaleFactor' , 'numChannel' , 'pVal' , ), 2206, (2206, (), [ (3, 1, None, None) , 
			 (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'FilterState' , 'numChannel' , 'pVal' , ), 2207, (2207, (), [ (3, 1, None, None) , 
			 (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'FilterState' , 'numChannel' , 'pVal' , ), 2207, (2207, (), [ (3, 1, None, None) , 
			 (2, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'CalibrationFactor' , 'pVal' , ), 2208, (2208, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'CalibrationFactor' , 'pVal' , ), 2208, (2208, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'ChannelFrequency' , 'numChannel' , 'pVal' , ), 2209, (2209, (), [ (3, 1, None, None) , 
			 (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ChannelFrequency' , 'numChannel' , 'pVal' , ), 2209, (2209, (), [ (3, 1, None, None) , 
			 (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'PhaseOffset' , 'numChannel' , 'pVal' , ), 2210, (2210, (), [ (3, 1, None, None) , 
			 (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'PhaseOffset' , 'numChannel' , 'pVal' , ), 2210, (2210, (), [ (3, 1, None, None) , 
			 (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Amplitude' , 'numChannel' , 'pVal' , ), 2211, (2211, (), [ (3, 1, None, None) , 
			 (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Amplitude' , 'numChannel' , 'pVal' , ), 2211, (2211, (), [ (3, 1, None, None) , 
			 (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'FreqOrder' , 'pVal' , ), 2212, (2212, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'FreqOrder' , 'pVal' , ), 2212, (2212, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'MBClockMultiplier' , 'numChannel' , 'pVal' , ), 2213, (2213, (), [ (3, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'MBClockMultiplier' , 'numChannel' , 'pVal' , ), 2213, (2213, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'CrossCorrelationInc' , 'pVal' , ), 2214, (2214, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'CrossCorrelationInc' , 'pVal' , ), 2214, (2214, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'SetChannelNumber' , 'pVal' , ), 2215, (2215, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'CalculateFrequency' , 'startFreq' , 'endFreq' , 'numFreq' , 'incFreq' , 
			 'mValue' , ), 2216, (2216, (), [ (5, 1, None, None) , (5, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (2, 1, None, None) , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'CalculateScale' , 'startFreq' , 'endFreq' , 'numFreq' , 'hiScale' , 
			 'loScale' , 'isSetA' , 'scaleType' , ), 2217, (2217, (), [ (5, 1, None, None) , 
			 (5, 1, None, None) , (3, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , (11, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'SetLifetimeProperty' , 'mffProperty' , 'pVal' , ), 2218, (2218, (), [ (3, 1, None, None) , 
			 (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'GetLifetimeProperty' , 'mffProperty' , 'pVal' , ), 2219, (2219, (), [ (3, 1, None, None) , 
			 (16389, 2, None, None) , ], 1 , 1 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'CalculateCZTransform' , 'pData' , 'sampleIndex' , ), 2220, (2220, (), [ (16396, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'CalculateMFFDisplayData' , 'sampleIndex' , 'pData' , ), 2221, (2221, (), [ (3, 1, None, None) , 
			 (16396, 2, None, None) , ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'CalculateStdDevs' , 'pData' , ), 2222, (2222, (), [ (16396, 2, None, None) , ], 1 , 1 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'CalculateLTParameters' , 'stdSampleNum' , 'unkSampleNum' , 'pData' , ), 2223, (2223, (), [ 
			 (3, 0, None, None) , (3, 0, None, None) , (16396, 2, None, None) , ], 1 , 1 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'CalculateClockFrequency' , 'numFreq' , 'incFreq' , 'mValue' , ), 2224, (2224, (), [ 
			 (3, 1, None, None) , (5, 1, None, None) , (2, 1, None, None) , ], 1 , 1 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'CalculateDSPParameters' , 'numFreq' , 'startFreq' , 'intTime' , 'totalTime' , 
			 ), 2225, (2225, (), [ (3, 1, None, None) , (16389, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'CalculateFinalLTParameters' , 'pData' , ), 2226, (2226, (), [ (16396, 2, None, None) , ], 1 , 1 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'CalculateSampleParameters' , 'sampleIndex' , ), 2227, (2227, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'CalculateFFT' , 'pData' , 'sampleIndex' , ), 2228, (2228, (), [ (16396, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'CalculateSampleDataObject' , 'sampleIndex' , 'pData' , ), 2229, (2229, (), [ (3, 1, None, None) , 
			 (16396, 2, None, None) , ], 1 , 1 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'GetFinalLTKineticsData' , 'pData' , ), 2230, (2230, (), [ (16396, 2, None, None) , ], 1 , 1 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'GetFinalLTAvgKineticsData' , 'pData' , ), 2231, (2231, (), [ (16396, 2, None, None) , ], 1 , 1 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'GetFilterValues' , 'taVal' , 'outVal' , ), 2232, (2232, (), [ (16386, 2, None, None) , 
			 (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'ResetSampleParameters' , ), 2233, (2233, (), [ ], 1 , 1 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'ResetLTParameters' , ), 2234, (2234, (), [ ], 1 , 1 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'GetNonZeroFreqCount' , 'freqCount' , ), 2235, (2235, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'CalculateSamplePolParameters' , 'sampleIndex' , 'polPosition' , 'sampleNumber' , 'iKinetics' , 
			 ), 2236, (2236, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'CalculateLTPolParameters' , 'stdSampleNum' , 'unkSampleNum' , 'isKinetics' , 'pData' , 
			 ), 2237, (2237, (), [ (3, 0, None, None) , (3, 0, None, None) , (3, 1, None, None) , (16396, 2, None, None) , ], 1 , 1 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'CalculateSamplePolDataObject' , 'sampleIndex' , 'polPosition' , 'pData' , ), 2238, (2238, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16396, 2, None, None) , ], 1 , 1 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'CalculateFinalLTADParameters' , 'pData' , ), 2239, (2239, (), [ (16396, 2, None, None) , ], 1 , 1 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'GetFinalLTADKineticsData' , 'pData' , ), 2240, (2240, (), [ (16396, 2, None, None) , ], 1 , 1 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
]

IJYAxis_vtables_dispatch_ = 1
IJYAxis_vtables_ = [
	(( 'SetLimits' , 'min' , 'max' , ), 1, (1, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'GetLimits' , 'min' , 'max' , ), 2, (2, (), [ (16387, 2, None, None) , 
			 (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'SetValue' , 'index' , 'value' , ), 3, (3, (), [ (3, 1, None, None) , 
			 (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'GetValue' , 'index' , 'value' , ), 4, (4, (), [ (3, 1, None, None) , 
			 (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'SetValuesByArray' , 'value' , ), 5, (5, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'GetValuesByArray' , 'value' , ), 6, (6, (), [ (16396, 2, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'GetIndexNearestValue' , 'value' , 'index' , ), 7, (7, (), [ (12, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Label' , 'Label' , ), 8, (8, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Label' , 'Label' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Units' , 'type' , ), 9, (9, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Units' , 'type' , ), 9, (9, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'DumpToFile' , 'FileName' , ), 10, (10, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
]

IJYConverter_vtables_dispatch_ = 1
IJYConverter_vtables_ = [
	(( 'Convert' , 'sourceVal' , 'convertFrom' , 'convertTo' , 'convertedVal' , 
			 ), 1, (1, (), [ (12, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'SetHardwareProperty' , 'jyProperty' , 'newVal' , ), 2, (2, (), [ (3, 1, None, None) , 
			 (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'GetHardwareProperty' , 'jyProperty' , 'pVal' , ), 3, (3, (), [ (3, 1, None, None) , 
			 (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'GetUnitsFromString' , 'unitsString' , 'pVal' , ), 4, (4, (), [ (8, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'GetStringFromUnits' , 'curUnits' , 'pVal' , ), 5, (5, (), [ (3, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstJYUnits' , 'pVal' , 'unitsString' , ), 6, (6, (), [ (16387, 2, None, None) , 
			 (16396, 2, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'GetNextJYUnits' , 'pVal' , 'unitsString' , ), 7, (7, (), [ (16387, 2, None, None) , 
			 (16396, 2, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'SetHardwarePropertySlits' , 'jyProperty' , 'whichSlit' , 'newVal' , ), 8, (8, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'GetHardwarePropertySlits' , 'jyProperty' , 'whichSlit' , 'pVal' , ), 9, (9, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ValidateHardwareProperty' , 'devType' , 'subDevType' , 'subDevIndex' , 'targetVal' , 
			 'targetUnits' , 'pVal' , ), 10, (10, (), [ (3, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (12, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'GetStringFromUnitsType' , 'unitsType' , 'pVal' , ), 11, (11, (), [ (3, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'ConvertToBaseGrating' , 'posInCurrentGrating' , 'workingUnits' , 'baseGratingValue' , ), 12, (12, (), [ 
			 (12, 1, None, None) , (3, 1, None, None) , (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'RoundOff' , 'unitsType' , 'curUnits' , 'curVal' , 'numDigits' , 
			 'whichSlit' , 'pVal' , ), 13, (13, (), [ (3, 1, None, None) , (3, 1, None, None) , 
			 (5, 1, None, None) , (3, 1, None, None) , (12, 17, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 1 , 152 , (3, 0, None, None) , 0 , )),
]

IJYDataObject_vtables_dispatch_ = 1
IJYDataObject_vtables_ = [
	(( 'Save' , 'FileName' , ), 1, (1, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Load' , 'FileName' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'FileType' , 'FileType' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'FileType' , 'FileType' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Dimensions' , 'Dimensions' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'GetDimension' , 'whichDimension' , 'dimensionValue' , ), 5, (5, (), [ (3, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'GetOffset' , 'whichDimension' , 'offsetValue' , ), 6, (6, (), [ (3, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'GetAxis' , 'whichDimension' , 'axis' , ), 7, (7, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{75F30081-BED4-4B0A-AB8B-5D3DFEC775D2}')") , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'GetRawData' , 'rawData' , ), 8, (8, (), [ (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'DataLayout' , 'DataLayout' , ), 9, (9, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'DoOperation' , 'operation' , 'operand1' , 'operand2' , ), 10, (10, (), [ 
			 (3, 1, None, None) , (12, 1, None, None) , (12, 17, None, None) , ], 1 , 1 , 4 , 1 , 136 , (3, 0, None, None) , 0 , )),
	(( 'MakeEven' , 'makeEvenBasedOn' , ), 11, (11, (), [ (12, 17, None, None) , ], 1 , 1 , 4 , 1 , 144 , (3, 0, None, None) , 0 , )),
	(( 'DataFormat' , 'DataFormat' , ), 12, (12, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'GetElement' , 'numDims' , 'elementDims' , 'data' , ), 13, (13, (), [ 
			 (3, 1, None, None) , (16387, 1, None, None) , (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'DumpToFile' , 'FileName' , ), 14, (14, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfDimensions' , 'numDims' , ), 15, (15, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Description' , 'Description' , ), 16, (16, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Description' , 'Description' , ), 16, (16, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'PerformAnalysis' , '__MIDL__IJYDataObject0000' , 'result' , ), 17, (17, (), [ (3, 1, None, None) , 
			 (16396, 2, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'GetDataAsArray' , 'dataAsSafeArray' , 'copy' , 'accumulation' , ), 18, (18, (), [ 
			 (16396, 2, None, None) , (12, 17, None, None) , (12, 17, None, None) , ], 1 , 1 , 4 , 2 , 208 , (3, 0, None, None) , 0 , )),
	(( 'GetDataBinned' , 'xBin' , 'yBin' , 'binnedDataAsSafeArray' , ), 19, (19, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16396, 2, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'GetPropertyValue' , 'property' , 'value' , ), 20, (20, (), [ (3, 1, None, None) , 
			 (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'GetCycle' , 'pVal' , ), 21, (21, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'MakeCopy' , 'dataObjCopy' , ), 22, (22, (), [ (16393, 10, None, "IID('{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')") , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'SetElement' , 'numDims' , 'elementDims' , 'data' , ), 23, (23, (), [ 
			 (3, 1, None, None) , (16387, 1, None, None) , (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'GetSubRegionAsArray' , 'newXStart' , 'newXSize' , 'newYStart' , 'newYSize' , 
			 'newXBin' , 'newYBin' , 'subRegionAsArray' , ), 24, (24, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			 (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'GetSubRegionAsDataObject' , 'newXStart' , 'newXSize' , 'newYStart' , 'newYSize' , 
			 'newXBin' , 'newYBin' , 'subRegionAsDataObject' , ), 25, (25, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			 (16393, 10, None, "IID('{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')") , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'GetBinnedAsDataObject' , 'newXBin' , 'newYBin' , 'subRegionAsDataObject' , ), 26, (26, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')") , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'GetDataForAxisValue' , 'axisValue' , 'dataValue' , ), 27, (27, (), [ (12, 1, None, None) , 
			 (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'OnAbort' , ), 28, (28, (), [ ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'ConvertToDouble' , ), 29, (29, (), [ ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'LoadSPCSubfile' , 'FileName' , 'iSubFile' , ), 30, (30, (), [ (8, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstProperty' , 'dataItemProp' , 'dataItemVal' , 'dataItemPropText' , ), 31, (31, (), [ 
			 (16387, 2, None, None) , (16396, 2, None, None) , (16396, 18, None, None) , ], 1 , 1 , 4 , 1 , 312 , (3, 0, None, None) , 0 , )),
	(( 'GetNextProperty' , 'dataItemProp' , 'dataItemVal' , 'dataItemPropText' , ), 32, (32, (), [ 
			 (16387, 2, None, None) , (16396, 2, None, None) , (16396, 18, None, None) , ], 1 , 1 , 4 , 1 , 320 , (3, 0, None, None) , 0 , )),
	(( 'ClearRleaseSafeDataArray' , 'dataAsSafeArray' , ), 33, (33, (), [ (16396, 2, None, None) , ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'GetCCDDataAppendMode' , 'mode' , ), 34, (34, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
]

IJYDataProvider_vtables_dispatch_ = 1
IJYDataProvider_vtables_ = [
	(( 'Initialize' , 'format' , 'numDims' , 'dims' , 'accumMode' , 
			 'numAccumulations' , ), 500, (500, (), [ (3, 1, None, None) , (3, 1, None, None) , (16387, 1, None, None) , 
			 (12, 17, None, None) , (12, 17, None, None) , ], 1 , 1 , 4 , 2 , 344 , (3, 0, None, None) , 0 , )),
	(( 'SetOffset' , 'whichDimension' , 'offsetValue' , ), 501, (501, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'SetAxis' , 'whichDimension' , 'axis' , 'IsDefaultAxis' , ), 502, (502, (), [ 
			 (3, 1, None, None) , (9, 1, None, "IID('{75F30081-BED4-4B0A-AB8B-5D3DFEC775D2}')") , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'SetRawData' , 'rawData' , ), 503, (503, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'MakeFakeData' , 'functionType' , ), 504, (504, (), [ (12, 17, None, None) , ], 1 , 1 , 4 , 1 , 376 , (3, 0, None, None) , 0 , )),
	(( 'Clear' , ), 505, (505, (), [ ], 1 , 1 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'AppendDataPoint' , 'dataPoint' , ), 506, (506, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'CurrentDataPointIndex' , 'dataPointIndex' , ), 507, (507, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'CurrentDataPointIndex' , 'dataPointIndex' , ), 507, (507, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'GetDataPtr' , 'dataPtr' , ), 508, (508, (), [ (16396, 2, None, None) , ], 1 , 1 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'SignalIndex' , 'SignalIndex' , ), 509, (509, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'SignalIndex' , 'SignalIndex' , ), 509, (509, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'AppendDataObject' , 'dataObject' , ), 510, (510, (), [ (9, 1, None, "IID('{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')") , ], 1 , 1 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'AppendMode' , 'mode' , ), 511, (511, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'AppendMode' , 'mode' , ), 511, (511, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'GetCurrentIndexByDimension' , 'index' , 'dim' , ), 512, (512, (), [ (16387, 2, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'SetPropertyValue' , 'property' , 'value' , ), 513, (513, (), [ (3, 1, None, None) , 
			 (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'CommitOperation' , ), 514, (514, (), [ ], 1 , 1 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'AccumulationIndex' , 'pVal' , ), 515, (515, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'AccumulationIndex' , 'pVal' , ), 515, (515, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'Cycle' , ), 516, (516, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'AccumulationCount' , 'count' , ), 517, (517, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'AccumulationCount' , 'count' , ), 517, (517, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstProperty' , 'property' , 'value' , ), 518, (518, (), [ (16387, 2, None, None) , 
			 (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'GetNextProperty' , 'property' , 'value' , ), 519, (519, (), [ (16387, 2, None, None) , 
			 (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'MakeMirror' , 'dataObjCopy' , ), 520, (520, (), [ (16393, 10, None, "IID('{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')") , ], 1 , 1 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'GlueDataObject' , 'dataObject' , 'mode' , 'overlap' , ), 521, (521, (), [ 
			 (9, 1, None, "IID('{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')") , (3, 1, None, None) , (12, 17, None, None) , ], 1 , 1 , 4 , 1 , 552 , (3, 0, None, None) , 0 , )),
	(( 'FlipX' , ), 522, (522, (), [ ], 1 , 1 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'GetCurrentAccumulationIndex' , 'currentIndex' , ), 523, (523, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstEventMarker' , 'eventInfo' , 'dataPointIndex' , 'accumluation' , ), 524, (524, (), [ 
			 (16396, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( 'GetNextEventMarker' , 'eventInfo' , 'dataPointIndex' , 'accumluation' , ), 525, (525, (), [ 
			 (16396, 2, None, None) , (16387, 2, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
	(( 'SetEventMarker' , 'eventInfo' , ), 526, (526, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 592 , (3, 0, None, None) , 0 , )),
	(( 'GetEventMarker' , 'eventInfo' , 'dataIndex' , 'accumulation' , ), 527, (527, (), [ 
			 (16396, 2, None, None) , (3, 17, None, None) , (3, 17, None, None) , ], 1 , 1 , 4 , 0 , 600 , (3, 0, None, None) , 0 , )),
	(( 'AppendDataPointAsArray' , 'dataPoint' , ), 528, (528, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 608 , (3, 0, None, None) , 0 , )),
	(( 'GroupDataObjects' , 'dataObject' , ), 529, (529, (), [ (9, 1, None, "IID('{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')") , ], 1 , 1 , 4 , 0 , 616 , (3, 0, None, None) , 0 , )),
	(( 'ClearEventMarkers' , ), 530, (530, (), [ ], 1 , 1 , 4 , 0 , 624 , (3, 0, None, None) , 0 , )),
]

IJYEventInfo_vtables_dispatch_ = 1
IJYEventInfo_vtables_ = [
	(( 'Source' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{7C269B67-FABB-4998-B00F-A43043E6F86C}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Source' , 'pVal' , ), 1, (1, (), [ (9, 1, None, "IID('{7C269B67-FABB-4998-B00F-A43043E6F86C}')") , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Description' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Description' , 'pVal' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Val' , 'pVal' , ), 3, (3, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Val' , 'pVal' , ), 3, (3, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'AttachData' , 'dataObject' , ), 4, (4, (), [ (9, 1, None, "IID('{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')") , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'AttachResults' , 'resultsObject' , ), 5, (5, (), [ (9, 1, None, "IID('{3948DB1C-95F8-4F57-AE15-2A5FC0B04CF1}')") , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'GetResult' , 'resultsObjectPtr' , ), 8, (8, (), [ (16393, 10, None, "IID('{3948DB1C-95F8-4F57-AE15-2A5FC0B04CF1}')") , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

IJYLogger_vtables_dispatch_ = 1
IJYLogger_vtables_ = [
	(( 'Log' , 'level' , 'formatString' , 'functionName' , 'vt1' , 
			 'vt2' , 'vt3' , 'vt4' , 'vt5' , ), 1, (1, (), [ 
			 (3, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (12, 17, None, None) , (12, 17, None, None) , 
			 (12, 17, None, None) , (12, 17, None, None) , (12, 17, None, None) , ], 1 , 1 , 4 , 5 , 56 , (3, 0, None, None) , 0 , )),
	(( 'FileName' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'FileName' , 'pVal' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'FilePath' , 'pVal' , ), 3, (3, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'FilePath' , 'pVal' , ), 3, (3, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'LoggingLevel' , 'pVal' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'LoggingLevel' , 'pVal' , ), 4, (4, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'MaxBackupFiles' , 'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'MaxBackupFiles' , 'pVal' , ), 5, (5, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'MaxFileSizeKB' , 'pVal' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'MaxFileSizeKB' , 'pVal' , ), 6, (6, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

IJYResultsObject_vtables_dispatch_ = 1
IJYResultsObject_vtables_ = [
	(( 'Save' , 'FileName' , ), 1, (1, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Load' , 'FileName' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstDataObject' , 'dataObj' , ), 3, (3, (), [ (16393, 10, None, "IID('{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')") , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'GetNextDataObject' , 'dataObj' , ), 4, (4, (), [ (16393, 10, None, "IID('{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'FileType' , 'FileType' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'FileType' , 'FileType' , ), 6, (6, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Description' , 'Description' , ), 7, (7, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Description' , 'Description' , ), 7, (7, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'DumpToFile' , 'FileName' , ), 8, (8, (), [ (8, 0, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'DoOperation' , 'operation' , 'operand1' , 'operand2' , ), 9, (9, (), [ 
			 (3, 1, None, None) , (12, 1, None, None) , (12, 17, None, None) , ], 1 , 1 , 4 , 1 , 128 , (3, 0, None, None) , 0 , )),
	(( 'DataObjectCount' , 'count' , ), 10, (10, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'InterpretAsImage' , 'maxXCount' , 'maxYCount' , 'image' , ), 11, (11, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16396, 2, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'GetDataObjectByIndex' , 'dataObjectIndex' , 'dataObj' , ), 12, (12, (), [ (3, 1, None, None) , 
			 (16393, 2, None, "IID('{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')") , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'GetProperty' , 'whichProperty' , 'propValue' , ), 13, (13, (), [ (3, 1, None, None) , 
			 (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'CurrentCycle' , 'Cycle' , ), 14, (14, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'MakeCopy' , 'resultObject' , ), 15, (15, (), [ (16393, 10, None, "IID('{3948DB1C-95F8-4F57-AE15-2A5FC0B04CF1}')") , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'AppendOverlayFile' , 'FileName' , 'identifier' , ), 16, (16, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstOverlay' , 'identifier' , 'dataObj' , ), 17, (17, (), [ (16396, 2, None, None) , 
			 (16393, 10, None, "IID('{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')") , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'GetNextOverlay' , 'identifier' , 'dataObj' , ), 18, (18, (), [ (16396, 2, None, None) , 
			 (16393, 10, None, "IID('{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')") , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstDataObjectFromDataSet' , 'dataSetIdx' , 'dataObj' , ), 19, (19, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')") , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'GetNextDataObjectFromDataSet' , 'dataSetIdx' , 'dataObj' , ), 20, (20, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')") , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'GetDataSetName' , 'dataSetIdx' , 'dsname' , ), 21, (21, (), [ (3, 1, None, None) , 
			 (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstRawDataObject' , 'dataObj' , ), 22, (22, (), [ (16393, 10, None, "IID('{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')") , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'GetNextRawDataObject' , 'dataObj' , ), 23, (23, (), [ (16393, 10, None, "IID('{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')") , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstDataObjectByCycle' , 'cycleNumber' , 'dataObj' , ), 24, (24, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')") , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'GetNextDataObjectByCycle' , 'cycleNumber' , 'dataObj' , ), 25, (25, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')") , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'FinalizeResult' , ), 26, (26, (), [ ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstDataSource' , 'dataSource' , ), 27, (27, (), [ (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'GetNextDataSource' , 'dataSource' , ), 28, (28, (), [ (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstDataObjectBySource' , 'dataSource' , 'dataObj' , ), 29, (29, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')") , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'GetNextDataObjectBySource' , 'dataSource' , 'dataObj' , ), 30, (30, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')") , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'GetSourceCount' , 'uniqueSourceCount' , ), 31, (31, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstDarkDataObject' , 'dataObj' , ), 32, (32, (), [ (16393, 10, None, "IID('{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')") , ], 1 , 1 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'GetNextDarkDataObject' , 'dataObj' , ), 33, (33, (), [ (16393, 10, None, "IID('{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')") , ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstPreAcqDataObject' , 'dataObj' , ), 34, (34, (), [ (16393, 10, None, "IID('{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')") , ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'GetNextPreAcqDataObject' , 'dataObj' , ), 35, (35, (), [ (16393, 10, None, "IID('{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')") , ], 1 , 1 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
]

IJYResultsProvider_vtables_dispatch_ = 1
IJYResultsProvider_vtables_ = [
	(( 'AppendResult' , 'resultInterface' , ), 500, (500, (), [ (9, 1, None, "IID('{3948DB1C-95F8-4F57-AE15-2A5FC0B04CF1}')") , ], 1 , 1 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'AppendDataObject' , 'dataObj' , 'dataObjId' , ), 501, (501, (), [ (9, 1, None, "IID('{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')") , 
			 (12, 17, None, None) , ], 1 , 1 , 4 , 1 , 352 , (3, 0, None, None) , 0 , )),
	(( 'GetDataObjectById' , 'dataObjId' , 'dataObj' , 'Cycle' , ), 502, (502, (), [ 
			 (12, 1, None, None) , (16393, 2, None, "IID('{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')") , (12, 17, None, None) , ], 1 , 1 , 4 , 1 , 360 , (3, 0, None, None) , 0 , )),
	(( 'WriteExperimentInfo' , 'FileName' , ), 503, (503, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'Initialize' , 'numCycles' , ), 504, (504, (), [ (12, 17, None, None) , ], 1 , 1 , 4 , 1 , 376 , (3, 0, None, None) , 0 , )),
	(( 'Clear' , ), 505, (505, (), [ ], 1 , 1 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'MakeFakeResult' , 'DataFormat' , 'numDataObjects' , 'dimsPerDataObject' , 'dataObjectDims' , 
			 ), 506, (506, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16387, 1, None, None) , ], 1 , 1 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'SetProperty' , 'whichProperty' , 'value' , ), 507, (507, (), [ (3, 1, None, None) , 
			 (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'AppendUpdate' , 'resultInterface' , ), 508, (508, (), [ (9, 1, None, "IID('{3948DB1C-95F8-4F57-AE15-2A5FC0B04CF1}')") , ], 1 , 1 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'CurrentCycle' , ), 509, (509, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'CycleCount' , 'count' , ), 510, (510, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'GlueResult' , 'resultsObject' , 'mode' , 'overlap' , ), 511, (511, (), [ 
			 (9, 1, None, "IID('{3948DB1C-95F8-4F57-AE15-2A5FC0B04CF1}')") , (3, 1, None, None) , (12, 17, None, None) , ], 1 , 1 , 4 , 1 , 432 , (3, 0, None, None) , 0 , )),
	(( 'AppendRawDataObject' , 'dataObj' , 'dataObjId' , ), 512, (512, (), [ (9, 1, None, "IID('{429CB47A-B0AA-4788-B5A1-78FA15BC554B}')") , 
			 (12, 17, None, None) , ], 1 , 1 , 4 , 1 , 440 , (3, 0, None, None) , 0 , )),
	(( 'GroupDataObjects' , ), 513, (513, (), [ ], 1 , 1 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'ClearDataObjectsMap' , ), 514, (514, (), [ ], 1 , 1 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{F7D651D7-D95D-4D49-A2BD-789987BF1D22}' : IJYEventInfo,
	'{81697F83-4E1C-45E2-985E-373BA254BD60}' : JYEventInfo,
	'{429CB47A-B0AA-4788-B5A1-78FA15BC554B}' : IJYDataObject,
	'{7135B4D1-2238-44D2-B97D-0EEEB291B85A}' : IJYDataProvider,
	'{9C30FF28-6E5F-46BF-A402-54BD8252C9C1}' : JYDataInterface,
	'{75F30081-BED4-4B0A-AB8B-5D3DFEC775D2}' : IJYAxis,
	'{9ADFE718-3F8F-40A8-8B65-51CAA3229BA9}' : JYAxisInterface,
	'{3948DB1C-95F8-4F57-AE15-2A5FC0B04CF1}' : IJYResultsObject,
	'{5EF255B2-C040-4801-84FF-BD1C2679F3A8}' : IJYResultsProvider,
	'{F58ACFF4-2B84-4755-A967-38DA7202D6DE}' : JYResultsInterface,
	'{572C08BD-7991-43A9-924C-DC4C670DF2FD}' : IJYLogger,
	'{D4CE928C-6ED8-4A73-B406-92AF84B69C1F}' : JYLoggerInterface,
	'{88E3B2DB-44E7-4E37-822B-17D3F604E069}' : IJYConverter,
	'{8EE4ADE9-81D7-4970-82FD-13BD5807172D}' : JYConverterInterface,
	'{FAD86B05-955D-47D6-9061-A48D4D4A7C0D}' : IJYAnalysisReqd,
	'{921802FD-513B-482F-A635-1CA0479BEB35}' : JYAnalysis,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{F7D651D7-D95D-4D49-A2BD-789987BF1D22}' : 'IJYEventInfo',
	'{429CB47A-B0AA-4788-B5A1-78FA15BC554B}' : 'IJYDataObject',
	'{7135B4D1-2238-44D2-B97D-0EEEB291B85A}' : 'IJYDataProvider',
	'{75F30081-BED4-4B0A-AB8B-5D3DFEC775D2}' : 'IJYAxis',
	'{3948DB1C-95F8-4F57-AE15-2A5FC0B04CF1}' : 'IJYResultsObject',
	'{5EF255B2-C040-4801-84FF-BD1C2679F3A8}' : 'IJYResultsProvider',
	'{572C08BD-7991-43A9-924C-DC4C670DF2FD}' : 'IJYLogger',
	'{88E3B2DB-44E7-4E37-822B-17D3F604E069}' : 'IJYConverter',
	'{FAD86B05-955D-47D6-9061-A48D4D4A7C0D}' : 'IJYAnalysisReqd',
}


NamesToIIDMap = {
	'IJYEventInfo' : '{F7D651D7-D95D-4D49-A2BD-789987BF1D22}',
	'IJYDataObject' : '{429CB47A-B0AA-4788-B5A1-78FA15BC554B}',
	'IJYDataProvider' : '{7135B4D1-2238-44D2-B97D-0EEEB291B85A}',
	'IJYAxis' : '{75F30081-BED4-4B0A-AB8B-5D3DFEC775D2}',
	'IJYResultsObject' : '{3948DB1C-95F8-4F57-AE15-2A5FC0B04CF1}',
	'IJYResultsProvider' : '{5EF255B2-C040-4801-84FF-BD1C2679F3A8}',
	'IJYLogger' : '{572C08BD-7991-43A9-924C-DC4C670DF2FD}',
	'IJYConverter' : '{88E3B2DB-44E7-4E37-822B-17D3F604E069}',
	'IJYAnalysisReqd' : '{FAD86B05-955D-47D6-9061-A48D4D4A7C0D}',
}


