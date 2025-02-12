import sys
from win32com.client import makepy

outputFile = r"./horiba_iHR320_config_man.py"
comTypeLibraryOrDLL = r"C:\Program Files\HORIBA Scientific\Common\JY Components\JYSupport\JYConfigBrowserComponent.dll"
sys.argv = ["makepy", "-o", outputFile, comTypeLibraryOrDLL]
makepy.main()

outputFile = r"./horiba_ccd.py"
comTypeLibraryOrDLL = r"C:\Program Files\HORIBA Scientific\Common\JY Components\Detectors\JYMCD\JYCCD.dll"
sys.argv = ["makepy", "-o", outputFile, comTypeLibraryOrDLL]
makepy.main()

outputFile = r"./horiba_common_objects.py"
comTypeLibraryOrDLL = r"C:\Program Files\HORIBA Scientific\Common\JY Components\JYSupport\JYCommonObjects.dll"
sys.argv = ["makepy", "-o", outputFile, comTypeLibraryOrDLL]
makepy.main()

outputFile = r"./horiba_system_lib.py"
comTypeLibraryOrDLL = r"C:\Program Files\HORIBA Scientific\Common\JY Components\JYSupport\JYSystemLib.dll"
sys.argv = ["makepy", "-o", outputFile, comTypeLibraryOrDLL]
makepy.main()