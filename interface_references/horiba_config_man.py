# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.10.4 | packaged by conda-forge | (main, Mar 30 2022, 08:38:02) [MSC v.1916 64 bit (AMD64)]
# From type library 'JYConfigBrowserComponent.dll'
# On Fri Aug 12 15:10:53 2022
'JYConfigBrowserComponent 1.0 Type Library'
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

CLSID = IID('{6996861C-23A5-43B3-B89A-F65CA06E4D13}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

from win32com.client import DispatchBaseClass
class IJYConfigBrowerInterface(DispatchBaseClass):
	'IJYConfigBrowerInterface Interface'
	CLSID = IID('{FCAC56F8-B378-42AB-8C6C-A41596864D4D}')
	coclass_clsid = IID('{3A457ACC-F1FB-4D7D-9AB4-EE427CE33385}')

	def DeleteDeviceById(self, devID=defaultNamedNotOptArg):
		'method DeleteDeviceById'
		return self._oleobj_.InvokeTypes(51, LCID, 1, (24, 0), ((8, 1),),devID
			)

	def DisplayCurrentConfiguration(self):
		'method DisplayCurrentConfiguration'
		return self._oleobj_.InvokeTypes(50, LCID, 1, (24, 0), (),)

	def GatherCCDInfo(self):
		'method GatherCCDInfo'
		return self._oleobj_.InvokeTypes(41, LCID, 1, (24, 0), (),)

	def GatherDatabaseInfo(self):
		'method GatherDatabaseInfo'
		return self._oleobj_.InvokeTypes(42, LCID, 1, (24, 0), (),)

	def GatherLogInfo(self):
		'method GatherLogInfo'
		return self._oleobj_.InvokeTypes(45, LCID, 1, (24, 0), (),)

	def GatherOriginInfo(self):
		'method GatherOriginInfo'
		return self._oleobj_.InvokeTypes(40, LCID, 1, (24, 0), (),)

	def GatherRegistryInfo(self):
		'method GatherRegistryInfo'
		return self._oleobj_.InvokeTypes(44, LCID, 1, (24, 0), (),)

	def GatherVersionInfo(self):
		'method GatherVersionInfo'
		return self._oleobj_.InvokeTypes(43, LCID, 1, (24, 0), (),)

	def GetDataExperimentPathsByConfig(self, configID=defaultNamedNotOptArg, pathData=pythoncom.Missing, pathExp=pythoncom.Missing):
		'method GetDataExperimentPathsByConfig'
		return self._ApplyTypes_(76, 1, (24, 0), ((8, 1), (16392, 2), (16392, 2)), 'GetDataExperimentPathsByConfig', None,configID
			, pathData, pathExp)

	def GetDefaultApplicationType(self, appType=pythoncom.Missing):
		'method GetDefaultApplicationType'
		return self._ApplyTypes_(77, 1, (24, 0), ((16387, 2),), 'GetDefaultApplicationType', None,appType
			)

	def GetDefaultConfig(self, name=pythoncom.Missing):
		'method GetDefaultConfig'
		return self._ApplyTypes_(75, 1, (24, 0), ((16392, 2),), 'GetDefaultConfig', None,name
			)

	def GetDevIdByConfig(self, configID=defaultNamedNotOptArg, cdc=defaultNamedNotOptArg, devClass=defaultNamedNotOptArg):
		'method GetDevIdByConfig'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(52, LCID, 1, (8, 0), ((8, 1), (3, 1), (3, 1)),configID
			, cdc, devClass)

	def GetDevIdFromDevName(self, devName=defaultNamedNotOptArg, devID=pythoncom.Missing):
		'method GetDevIdFromDevName'
		return self._ApplyTypes_(49, 1, (24, 0), ((8, 1), (16392, 2)), 'GetDevIdFromDevName', None,devName
			, devID)

	def GetFirstAccessory(self, accType=defaultNamedNotOptArg, name=pythoncom.Missing):
		'method GetFirstAccessory'
		return self._ApplyTypes_(14, 1, (8, 0), ((3, 1), (16392, 2)), 'GetFirstAccessory', None,accType
			, name)

	def GetFirstAccessoryByConfig(self, configID=defaultNamedNotOptArg, devName=pythoncom.Missing):
		'method GetFirstAccessoryByConfig'
		return self._ApplyTypes_(71, 1, (8, 0), ((8, 1), (16392, 2)), 'GetFirstAccessoryByConfig', None,configID
			, devName)

	def GetFirstCCD(self, name=pythoncom.Missing):
		'method GetFirstCCD'
		return self._ApplyTypes_(10, 1, (8, 0), ((16392, 2),), 'GetFirstCCD', None,name
			)

	def GetFirstCCDByConfig(self, configID=defaultNamedNotOptArg, devName=pythoncom.Missing):
		'method GetFirstCCDByConfig'
		return self._ApplyTypes_(69, 1, (8, 0), ((8, 1), (16392, 2)), 'GetFirstCCDByConfig', None,configID
			, devName)

	def GetFirstComponent(self, name=pythoncom.Missing, creationDate=pythoncom.Missing):
		'method GetFirstComponent'
		return self._ApplyTypes_(36, 1, (8, 0), ((16392, 2), (16392, 2)), 'GetFirstComponent', None,name
			, creationDate)

	def GetFirstConfig(self, name=pythoncom.Missing):
		'method GetFirstConfig'
		return self._ApplyTypes_(2, 1, (8, 0), ((16392, 2),), 'GetFirstConfig', None,name
			)

	def GetFirstDetector(self, name=pythoncom.Missing):
		'method GetFirstDetector'
		return self._ApplyTypes_(8, 1, (8, 0), ((16392, 2),), 'GetFirstDetector', None,name
			)

	def GetFirstDevNode(self, devID=defaultNamedNotOptArg, nodeName=pythoncom.Missing):
		'method GetFirstDevNode'
		return self._ApplyTypes_(22, 1, (24, 0), ((8, 1), (16392, 2)), 'GetFirstDevNode', None,devID
			, nodeName)

	def GetFirstDevNodeChild(self, nodeName=defaultNamedNotOptArg, childNodeName=pythoncom.Missing):
		'method GetFirstDevNodeChild'
		return self._ApplyTypes_(26, 1, (24, 0), ((8, 1), (16392, 2)), 'GetFirstDevNodeChild', None,nodeName
			, childNodeName)

	def GetFirstDevValue(self, devID=defaultNamedNotOptArg, valueName=pythoncom.Missing):
		'method GetFirstDevValue'
		return self._ApplyTypes_(20, 1, (12, 0), ((8, 1), (16392, 2)), 'GetFirstDevValue', None,devID
			, valueName)

	def GetFirstDevice(self, name=pythoncom.Missing):
		'method GetFirstDevice'
		return self._ApplyTypes_(6, 1, (8, 0), ((16392, 2),), 'GetFirstDevice', None,name
			)

	def GetFirstDeviceByConfig(self, configID=defaultNamedNotOptArg, devName=pythoncom.Missing):
		'method GetFirstDeviceByConfig'
		return self._ApplyTypes_(4, 1, (8, 0), ((8, 1), (16392, 2)), 'GetFirstDeviceByConfig', None,configID
			, devName)

	def GetFirstFilterWheel(self, name=pythoncom.Missing):
		'method GetFirstFilterWheel'
		return self._ApplyTypes_(16, 1, (8, 0), ((16392, 2),), 'GetFirstFilterWheel', None,name
			)

	def GetFirstFocusMount(self, name=pythoncom.Missing):
		'method GetFirstFocusMount'
		return self._ApplyTypes_(61, 1, (8, 0), ((16392, 2),), 'GetFirstFocusMount', None,name
			)

	def GetFirstHVController(self, name=pythoncom.Missing):
		'method GetFirstHVController'
		return self._ApplyTypes_(63, 1, (8, 0), ((16392, 2),), 'GetFirstHVController', None,name
			)

	def GetFirstLaser(self, name=pythoncom.Missing):
		'method GetFirstLaser'
		return self._ApplyTypes_(82, 1, (8, 0), ((16392, 2),), 'GetFirstLaser', None,name
			)

	def GetFirstLightSource(self, name=pythoncom.Missing):
		'method GetFirstLightSource'
		return self._ApplyTypes_(47, 1, (8, 0), ((16392, 2),), 'GetFirstLightSource', None,name
			)

	def GetFirstMono(self, name=pythoncom.Missing):
		'method GetFirstMono'
		return self._ApplyTypes_(31, 1, (8, 0), ((16392, 2),), 'GetFirstMono', None,name
			)

	def GetFirstMonoByConfig(self, configID=defaultNamedNotOptArg, devName=pythoncom.Missing):
		'method GetFirstMonoByConfig'
		return self._ApplyTypes_(65, 1, (8, 0), ((8, 1), (16392, 2)), 'GetFirstMonoByConfig', None,configID
			, devName)

	def GetFirstNodeValue(self, nodeName=defaultNamedNotOptArg, valueName=pythoncom.Missing):
		'method GetFirstNodeValue'
		return self._ApplyTypes_(24, 1, (12, 0), ((8, 1), (16392, 2)), 'GetFirstNodeValue', None,nodeName
			, valueName)

	def GetFirstPolarizer(self, name=pythoncom.Missing):
		'method GetFirstPolarizer'
		return self._ApplyTypes_(18, 1, (8, 0), ((16392, 2),), 'GetFirstPolarizer', None,name
			)

	def GetFirstRelatedComponent(self, name=pythoncom.Missing, creationDate=pythoncom.Missing):
		'method GetFirstRelatedComponent'
		return self._ApplyTypes_(38, 1, (8, 0), ((16392, 2), (16392, 2)), 'GetFirstRelatedComponent', None,name
			, creationDate)

	def GetFirstSCD(self, name=pythoncom.Missing):
		'method GetFirstSCD'
		return self._ApplyTypes_(12, 1, (8, 0), ((16392, 2),), 'GetFirstSCD', None,name
			)

	def GetFirstSCDByConfig(self, configID=defaultNamedNotOptArg, devName=pythoncom.Missing):
		'method GetFirstSCDByConfig'
		return self._ApplyTypes_(67, 1, (8, 0), ((8, 1), (16392, 2)), 'GetFirstSCDByConfig', None,configID
			, devName)

	def GetFirstSampleChanger(self, name=pythoncom.Missing):
		'method GetFirstSampleChanger'
		return self._ApplyTypes_(59, 1, (8, 0), ((16392, 2),), 'GetFirstSampleChanger', None,name
			)

	def GetFirstSampleChangerByConfig(self, configID=defaultNamedNotOptArg, devName=pythoncom.Missing):
		'method GetFirstSampleChangerByConfig'
		return self._ApplyTypes_(73, 1, (8, 0), ((8, 1), (16392, 2)), 'GetFirstSampleChangerByConfig', None,configID
			, devName)

	def GetFirstStirrer(self, name=pythoncom.Missing):
		'method GetFirstStirrer'
		return self._ApplyTypes_(57, 1, (8, 0), ((16392, 2),), 'GetFirstStirrer', None,name
			)

	def GetFirstTCSPC(self, name=pythoncom.Missing):
		'method GetFirstTCSPC'
		return self._ApplyTypes_(55, 1, (8, 0), ((16392, 2),), 'GetFirstTCSPC', None,name
			)

	def GetFirstTCSPCdata(self, name=pythoncom.Missing):
		'method GetFirstTCSPCdata'
		return self._ApplyTypes_(53, 1, (8, 0), ((16392, 2),), 'GetFirstTCSPCdata', None,name
			)

	def GetFirstTemperatureControl(self, name=pythoncom.Missing):
		'method GetFirstTemperatureControl'
		return self._ApplyTypes_(34, 1, (8, 0), ((16392, 2),), 'GetFirstTemperatureControl', None,name
			)

	def GetFirstTemperatureControllerByConfig(self, configID=defaultNamedNotOptArg, devName=pythoncom.Missing):
		'method GetFirstTemperatureControllerByConfig'
		return self._ApplyTypes_(78, 1, (8, 0), ((8, 1), (16392, 2)), 'GetFirstTemperatureControllerByConfig', None,configID
			, devName)

	def GetFirstXYStageByConfig(self, configID=defaultNamedNotOptArg, devName=pythoncom.Missing):
		'method GetFirstXYStageByConfig'
		return self._ApplyTypes_(80, 1, (8, 0), ((8, 1), (16392, 2)), 'GetFirstXYStageByConfig', None,configID
			, devName)

	def GetNextAccessory(self, accType=defaultNamedNotOptArg, name=pythoncom.Missing):
		'method GetNextAccessory'
		return self._ApplyTypes_(15, 1, (8, 0), ((3, 1), (16392, 2)), 'GetNextAccessory', None,accType
			, name)

	def GetNextAccessoryByConfig(self, configID=defaultNamedNotOptArg, devName=pythoncom.Missing):
		'method GetNextAccessoryByConfig'
		return self._ApplyTypes_(72, 1, (8, 0), ((8, 1), (16392, 2)), 'GetNextAccessoryByConfig', None,configID
			, devName)

	def GetNextAvailableID(self, jyDevClass=defaultNamedNotOptArg, jyDevType=defaultNamedNotOptArg):
		'method GetNextAvailableID'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(30, LCID, 1, (8, 0), ((3, 1), (3, 1)),jyDevClass
			, jyDevType)

	def GetNextCCD(self, name=pythoncom.Missing):
		'method GetNextCCD'
		return self._ApplyTypes_(11, 1, (8, 0), ((16392, 2),), 'GetNextCCD', None,name
			)

	def GetNextCCDByConfig(self, configID=defaultNamedNotOptArg, devName=pythoncom.Missing):
		'method GetNextCCDByConfig'
		return self._ApplyTypes_(70, 1, (8, 0), ((8, 1), (16392, 2)), 'GetNextCCDByConfig', None,configID
			, devName)

	def GetNextComponent(self, name=pythoncom.Missing, creationDate=pythoncom.Missing):
		'method GetNextComponent'
		return self._ApplyTypes_(37, 1, (8, 0), ((16392, 2), (16392, 2)), 'GetNextComponent', None,name
			, creationDate)

	def GetNextConfig(self, name=pythoncom.Missing):
		'method GetNextConfig'
		return self._ApplyTypes_(3, 1, (8, 0), ((16392, 2),), 'GetNextConfig', None,name
			)

	def GetNextDetector(self, name=pythoncom.Missing):
		'method GetNextDetector'
		return self._ApplyTypes_(9, 1, (8, 0), ((16392, 2),), 'GetNextDetector', None,name
			)

	def GetNextDevNode(self, devID=defaultNamedNotOptArg, nodeName=pythoncom.Missing):
		'method GetNextDevNode'
		return self._ApplyTypes_(23, 1, (24, 0), ((8, 1), (16392, 2)), 'GetNextDevNode', None,devID
			, nodeName)

	def GetNextDevNodeChild(self, nodeName=defaultNamedNotOptArg, childNodeName=pythoncom.Missing):
		'method GetNextDevNodeChild'
		return self._ApplyTypes_(27, 1, (24, 0), ((8, 1), (16392, 2)), 'GetNextDevNodeChild', None,nodeName
			, childNodeName)

	def GetNextDevValue(self, devID=defaultNamedNotOptArg, valueName=pythoncom.Missing):
		'method GetNextDevValue'
		return self._ApplyTypes_(21, 1, (12, 0), ((8, 1), (16392, 2)), 'GetNextDevValue', None,devID
			, valueName)

	def GetNextDevice(self, name=pythoncom.Missing):
		'method GetNextDevice'
		return self._ApplyTypes_(7, 1, (8, 0), ((16392, 2),), 'GetNextDevice', None,name
			)

	def GetNextDeviceByConfig(self, configID=defaultNamedNotOptArg, devName=pythoncom.Missing):
		'method GetNextDeviceByConfig'
		return self._ApplyTypes_(5, 1, (8, 0), ((8, 1), (16392, 2)), 'GetNextDeviceByConfig', None,configID
			, devName)

	def GetNextFilterWheel(self, name=pythoncom.Missing):
		'method GetNextFilterWheel'
		return self._ApplyTypes_(17, 1, (8, 0), ((16392, 2),), 'GetNextFilterWheel', None,name
			)

	def GetNextFocusMount(self, name=pythoncom.Missing):
		'method GetNextFocusMount'
		return self._ApplyTypes_(62, 1, (8, 0), ((16392, 2),), 'GetNextFocusMount', None,name
			)

	def GetNextHVController(self, name=pythoncom.Missing):
		'method GetNextHVController'
		return self._ApplyTypes_(64, 1, (8, 0), ((16392, 2),), 'GetNextHVController', None,name
			)

	def GetNextLaser(self, name=pythoncom.Missing):
		'method GetNextLaser'
		return self._ApplyTypes_(83, 1, (8, 0), ((16392, 2),), 'GetNextLaser', None,name
			)

	def GetNextLightSource(self, name=pythoncom.Missing):
		'method GetNextLightSource'
		return self._ApplyTypes_(48, 1, (8, 0), ((16392, 2),), 'GetNextLightSource', None,name
			)

	def GetNextMono(self, name=pythoncom.Missing):
		'method GetNextMono'
		return self._ApplyTypes_(32, 1, (8, 0), ((16392, 2),), 'GetNextMono', None,name
			)

	def GetNextMonoByConfig(self, configID=defaultNamedNotOptArg, devName=pythoncom.Missing):
		'method GetNextMonoByConfig'
		return self._ApplyTypes_(66, 1, (8, 0), ((8, 1), (16392, 2)), 'GetNextMonoByConfig', None,configID
			, devName)

	def GetNextNodeValue(self, nodeName=defaultNamedNotOptArg, valueName=pythoncom.Missing):
		'method GetNextNodeValue'
		return self._ApplyTypes_(25, 1, (12, 0), ((8, 1), (16392, 2)), 'GetNextNodeValue', None,nodeName
			, valueName)

	def GetNextPolarizer(self, name=pythoncom.Missing):
		'method GetNextPolarizer'
		return self._ApplyTypes_(19, 1, (8, 0), ((16392, 2),), 'GetNextPolarizer', None,name
			)

	def GetNextRelatedComponent(self, name=pythoncom.Missing, creationDate=pythoncom.Missing):
		'method GetNextRelatedComponent'
		return self._ApplyTypes_(39, 1, (8, 0), ((16392, 2), (16392, 2)), 'GetNextRelatedComponent', None,name
			, creationDate)

	def GetNextSCD(self, name=pythoncom.Missing):
		'method GetNextSCD'
		return self._ApplyTypes_(13, 1, (8, 0), ((16392, 2),), 'GetNextSCD', None,name
			)

	def GetNextSCDByConfig(self, configID=defaultNamedNotOptArg, devName=pythoncom.Missing):
		'method GetNextSCDByConfig'
		return self._ApplyTypes_(68, 1, (8, 0), ((8, 1), (16392, 2)), 'GetNextSCDByConfig', None,configID
			, devName)

	def GetNextSampleChanger(self, name=pythoncom.Missing):
		'method GetNextSampleChanger'
		return self._ApplyTypes_(60, 1, (8, 0), ((16392, 2),), 'GetNextSampleChanger', None,name
			)

	def GetNextSampleChangerByConfig(self, configID=defaultNamedNotOptArg, devName=pythoncom.Missing):
		'method GetNextSampleChangerByConfig'
		return self._ApplyTypes_(74, 1, (8, 0), ((8, 1), (16392, 2)), 'GetNextSampleChangerByConfig', None,configID
			, devName)

	def GetNextStirrer(self, name=pythoncom.Missing):
		'method GetNextStirrer'
		return self._ApplyTypes_(58, 1, (8, 0), ((16392, 2),), 'GetNextStirrer', None,name
			)

	def GetNextTCSPC(self, name=pythoncom.Missing):
		'method GetNextTCSPC'
		return self._ApplyTypes_(56, 1, (8, 0), ((16392, 2),), 'GetNextTCSPC', None,name
			)

	def GetNextTCSPCdata(self, name=pythoncom.Missing):
		'method GetNextTCSPCdata'
		return self._ApplyTypes_(54, 1, (8, 0), ((16392, 2),), 'GetNextTCSPCdata', None,name
			)

	def GetNextTemperatureControl(self, name=pythoncom.Missing):
		'method GetNextTemperatureControl'
		return self._ApplyTypes_(35, 1, (8, 0), ((16392, 2),), 'GetNextTemperatureControl', None,name
			)

	def GetNextTemperatureControllerByConfig(self, configID=defaultNamedNotOptArg, devName=pythoncom.Missing):
		'method GetNextTemperatureControllerByConfig'
		return self._ApplyTypes_(79, 1, (8, 0), ((8, 1), (16392, 2)), 'GetNextTemperatureControllerByConfig', None,configID
			, devName)

	def GetNextXYStageByConfig(self, configID=defaultNamedNotOptArg, devName=pythoncom.Missing):
		'method GetNextXYStageByConfig'
		return self._ApplyTypes_(81, 1, (8, 0), ((8, 1), (16392, 2)), 'GetNextXYStageByConfig', None,configID
			, devName)

	def Load(self):
		'method Load'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (24, 0), (),)

	def LoadFromFile(self, fullFileName=defaultNamedNotOptArg):
		'method LoadFromFile'
		return self._oleobj_.InvokeTypes(29, LCID, 1, (24, 0), ((8, 1),),fullFileName
			)

	def PackageSupportInfo(self, fullFileName=defaultNamedNotOptArg):
		'method PackageSupportInfo'
		return self._oleobj_.InvokeTypes(46, LCID, 1, (24, 0), ((8, 1),),fullFileName
			)

	def Unload(self):
		'method Unload'
		return self._oleobj_.InvokeTypes(33, LCID, 1, (24, 0), (),)

	def WriteToFile(self, fullFileName=defaultNamedNotOptArg):
		'method WriteToFile'
		return self._oleobj_.InvokeTypes(28, LCID, 1, (24, 0), ((8, 1),),fullFileName
			)

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

class _IJYConfigBrowerInterfaceEvents:
	'_IJYConfigBrowerInterfaceEvents Interface'
	CLSID = CLSID_Sink = IID('{06C073A5-AD0F-4A9C-A048-E2789C3594C9}')
	coclass_clsid = IID('{3A457ACC-F1FB-4D7D-9AB4-EE427CE33385}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
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


from win32com.client import CoClassBaseClass
# This CoClass is known by the name 'JYConfigBrowserComponent.JYConfigBrowerInterface.1'
class JYConfigBrowerInterface(CoClassBaseClass): # A CoClass
	# JYConfigBrowerInterface Class
	CLSID = IID('{3A457ACC-F1FB-4D7D-9AB4-EE427CE33385}')
	coclass_sources = [
		_IJYConfigBrowerInterfaceEvents,
	]
	default_source = _IJYConfigBrowerInterfaceEvents
	coclass_interfaces = [
		IJYConfigBrowerInterface,
	]
	default_interface = IJYConfigBrowerInterface

IJYConfigBrowerInterface_vtables_dispatch_ = 1
IJYConfigBrowerInterface_vtables_ = [
	(( 'Load' , ), 1, (1, (), [ ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstConfig' , 'name' , 'configID' , ), 2, (2, (), [ (16392, 2, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'GetNextConfig' , 'name' , 'configID' , ), 3, (3, (), [ (16392, 2, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstDeviceByConfig' , 'configID' , 'devName' , 'devID' , ), 4, (4, (), [ 
			 (8, 1, None, None) , (16392, 2, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'GetNextDeviceByConfig' , 'configID' , 'devName' , 'devID' , ), 5, (5, (), [ 
			 (8, 1, None, None) , (16392, 2, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstDevice' , 'name' , 'devID' , ), 6, (6, (), [ (16392, 2, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'GetNextDevice' , 'name' , 'devID' , ), 7, (7, (), [ (16392, 2, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstDetector' , 'name' , 'detectorID' , ), 8, (8, (), [ (16392, 2, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'GetNextDetector' , 'name' , 'detectorID' , ), 9, (9, (), [ (16392, 2, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstCCD' , 'name' , 'ccdID' , ), 10, (10, (), [ (16392, 2, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'GetNextCCD' , 'name' , 'ccdID' , ), 11, (11, (), [ (16392, 2, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstSCD' , 'name' , 'ccdID' , ), 12, (12, (), [ (16392, 2, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'GetNextSCD' , 'name' , 'ccdID' , ), 13, (13, (), [ (16392, 2, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstAccessory' , 'accType' , 'name' , 'accID' , ), 14, (14, (), [ 
			 (3, 1, None, None) , (16392, 2, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'GetNextAccessory' , 'accType' , 'name' , 'accID' , ), 15, (15, (), [ 
			 (3, 1, None, None) , (16392, 2, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstFilterWheel' , 'name' , 'accID' , ), 16, (16, (), [ (16392, 2, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'GetNextFilterWheel' , 'name' , 'accID' , ), 17, (17, (), [ (16392, 2, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstPolarizer' , 'name' , 'accID' , ), 18, (18, (), [ (16392, 2, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'GetNextPolarizer' , 'name' , 'accID' , ), 19, (19, (), [ (16392, 2, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstDevValue' , 'devID' , 'valueName' , 'value' , ), 20, (20, (), [ 
			 (8, 1, None, None) , (16392, 2, None, None) , (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'GetNextDevValue' , 'devID' , 'valueName' , 'value' , ), 21, (21, (), [ 
			 (8, 1, None, None) , (16392, 2, None, None) , (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstDevNode' , 'devID' , 'nodeName' , ), 22, (22, (), [ (8, 1, None, None) , 
			 (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'GetNextDevNode' , 'devID' , 'nodeName' , ), 23, (23, (), [ (8, 1, None, None) , 
			 (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstNodeValue' , 'nodeName' , 'valueName' , 'value' , ), 24, (24, (), [ 
			 (8, 1, None, None) , (16392, 2, None, None) , (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'GetNextNodeValue' , 'nodeName' , 'valueName' , 'value' , ), 25, (25, (), [ 
			 (8, 1, None, None) , (16392, 2, None, None) , (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstDevNodeChild' , 'nodeName' , 'childNodeName' , ), 26, (26, (), [ (8, 1, None, None) , 
			 (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'GetNextDevNodeChild' , 'nodeName' , 'childNodeName' , ), 27, (27, (), [ (8, 1, None, None) , 
			 (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'WriteToFile' , 'fullFileName' , ), 28, (28, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'LoadFromFile' , 'fullFileName' , ), 29, (29, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'GetNextAvailableID' , 'jyDevClass' , 'jyDevType' , 'newDevID' , ), 30, (30, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstMono' , 'name' , 'monoID' , ), 31, (31, (), [ (16392, 2, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'GetNextMono' , 'name' , 'monoID' , ), 32, (32, (), [ (16392, 2, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Unload' , ), 33, (33, (), [ ], 1 , 1 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstTemperatureControl' , 'name' , 'accID' , ), 34, (34, (), [ (16392, 2, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'GetNextTemperatureControl' , 'name' , 'accID' , ), 35, (35, (), [ (16392, 2, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstComponent' , 'name' , 'creationDate' , 'versionNumber' , ), 36, (36, (), [ 
			 (16392, 2, None, None) , (16392, 2, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'GetNextComponent' , 'name' , 'creationDate' , 'versionNumber' , ), 37, (37, (), [ 
			 (16392, 2, None, None) , (16392, 2, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstRelatedComponent' , 'name' , 'creationDate' , 'versionNumber' , ), 38, (38, (), [ 
			 (16392, 2, None, None) , (16392, 2, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'GetNextRelatedComponent' , 'name' , 'creationDate' , 'versionNumber' , ), 39, (39, (), [ 
			 (16392, 2, None, None) , (16392, 2, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'GatherOriginInfo' , ), 40, (40, (), [ ], 1 , 1 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'GatherCCDInfo' , ), 41, (41, (), [ ], 1 , 1 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'GatherDatabaseInfo' , ), 42, (42, (), [ ], 1 , 1 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'GatherVersionInfo' , ), 43, (43, (), [ ], 1 , 1 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'GatherRegistryInfo' , ), 44, (44, (), [ ], 1 , 1 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'GatherLogInfo' , ), 45, (45, (), [ ], 1 , 1 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'PackageSupportInfo' , 'fullFileName' , ), 46, (46, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstLightSource' , 'name' , 'accID' , ), 47, (47, (), [ (16392, 2, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'GetNextLightSource' , 'name' , 'accID' , ), 48, (48, (), [ (16392, 2, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'GetDevIdFromDevName' , 'devName' , 'devID' , ), 49, (49, (), [ (8, 1, None, None) , 
			 (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'DisplayCurrentConfiguration' , ), 50, (50, (), [ ], 1 , 1 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'DeleteDeviceById' , 'devID' , ), 51, (51, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'GetDevIdByConfig' , 'configID' , 'cdc' , 'devClass' , 'devID' , 
			 ), 52, (52, (), [ (8, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstTCSPCdata' , 'name' , 'TcspcDataID' , ), 53, (53, (), [ (16392, 2, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'GetNextTCSPCdata' , 'name' , 'TcspcDataID' , ), 54, (54, (), [ (16392, 2, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstTCSPC' , 'name' , 'tcspcID' , ), 55, (55, (), [ (16392, 2, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'GetNextTCSPC' , 'name' , 'tcspcID' , ), 56, (56, (), [ (16392, 2, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstStirrer' , 'name' , 'stirrerID' , ), 57, (57, (), [ (16392, 2, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'GetNextStirrer' , 'name' , 'stirrerID' , ), 58, (58, (), [ (16392, 2, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstSampleChanger' , 'name' , 'scID' , ), 59, (59, (), [ (16392, 2, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'GetNextSampleChanger' , 'name' , 'scID' , ), 60, (60, (), [ (16392, 2, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstFocusMount' , 'name' , 'focusID' , ), 61, (61, (), [ (16392, 2, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'GetNextFocusMount' , 'name' , 'focusID' , ), 62, (62, (), [ (16392, 2, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstHVController' , 'name' , 'HVcontrollerID' , ), 63, (63, (), [ (16392, 2, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'GetNextHVController' , 'name' , 'HVcontrollerID' , ), 64, (64, (), [ (16392, 2, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstMonoByConfig' , 'configID' , 'devName' , 'devID' , ), 65, (65, (), [ 
			 (8, 1, None, None) , (16392, 2, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'GetNextMonoByConfig' , 'configID' , 'devName' , 'devID' , ), 66, (66, (), [ 
			 (8, 1, None, None) , (16392, 2, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstSCDByConfig' , 'configID' , 'devName' , 'devID' , ), 67, (67, (), [ 
			 (8, 1, None, None) , (16392, 2, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
	(( 'GetNextSCDByConfig' , 'configID' , 'devName' , 'devID' , ), 68, (68, (), [ 
			 (8, 1, None, None) , (16392, 2, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 592 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstCCDByConfig' , 'configID' , 'devName' , 'devID' , ), 69, (69, (), [ 
			 (8, 1, None, None) , (16392, 2, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 600 , (3, 0, None, None) , 0 , )),
	(( 'GetNextCCDByConfig' , 'configID' , 'devName' , 'devID' , ), 70, (70, (), [ 
			 (8, 1, None, None) , (16392, 2, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 608 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstAccessoryByConfig' , 'configID' , 'devName' , 'devID' , ), 71, (71, (), [ 
			 (8, 1, None, None) , (16392, 2, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 616 , (3, 0, None, None) , 0 , )),
	(( 'GetNextAccessoryByConfig' , 'configID' , 'devName' , 'devID' , ), 72, (72, (), [ 
			 (8, 1, None, None) , (16392, 2, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 624 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstSampleChangerByConfig' , 'configID' , 'devName' , 'devID' , ), 73, (73, (), [ 
			 (8, 1, None, None) , (16392, 2, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 632 , (3, 0, None, None) , 0 , )),
	(( 'GetNextSampleChangerByConfig' , 'configID' , 'devName' , 'devID' , ), 74, (74, (), [ 
			 (8, 1, None, None) , (16392, 2, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 640 , (3, 0, None, None) , 0 , )),
	(( 'GetDefaultConfig' , 'name' , ), 75, (75, (), [ (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 648 , (3, 0, None, None) , 0 , )),
	(( 'GetDataExperimentPathsByConfig' , 'configID' , 'pathData' , 'pathExp' , ), 76, (76, (), [ 
			 (8, 1, None, None) , (16392, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 656 , (3, 0, None, None) , 0 , )),
	(( 'GetDefaultApplicationType' , 'appType' , ), 77, (77, (), [ (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 664 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstTemperatureControllerByConfig' , 'configID' , 'devName' , 'devID' , ), 78, (78, (), [ 
			 (8, 1, None, None) , (16392, 2, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 672 , (3, 0, None, None) , 0 , )),
	(( 'GetNextTemperatureControllerByConfig' , 'configID' , 'devName' , 'devID' , ), 79, (79, (), [ 
			 (8, 1, None, None) , (16392, 2, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 680 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstXYStageByConfig' , 'configID' , 'devName' , 'devID' , ), 80, (80, (), [ 
			 (8, 1, None, None) , (16392, 2, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 688 , (3, 0, None, None) , 0 , )),
	(( 'GetNextXYStageByConfig' , 'configID' , 'devName' , 'devID' , ), 81, (81, (), [ 
			 (8, 1, None, None) , (16392, 2, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 696 , (3, 0, None, None) , 0 , )),
	(( 'GetFirstLaser' , 'name' , 'laserID' , ), 82, (82, (), [ (16392, 2, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 704 , (3, 0, None, None) , 0 , )),
	(( 'GetNextLaser' , 'name' , 'laserID' , ), 83, (83, (), [ (16392, 2, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 712 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{06C073A5-AD0F-4A9C-A048-E2789C3594C9}' : _IJYConfigBrowerInterfaceEvents,
	'{FCAC56F8-B378-42AB-8C6C-A41596864D4D}' : IJYConfigBrowerInterface,
	'{3A457ACC-F1FB-4D7D-9AB4-EE427CE33385}' : JYConfigBrowerInterface,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{FCAC56F8-B378-42AB-8C6C-A41596864D4D}' : 'IJYConfigBrowerInterface',
}


NamesToIIDMap = {
	'_IJYConfigBrowerInterfaceEvents' : '{06C073A5-AD0F-4A9C-A048-E2789C3594C9}',
	'IJYConfigBrowerInterface' : '{FCAC56F8-B378-42AB-8C6C-A41596864D4D}',
}


