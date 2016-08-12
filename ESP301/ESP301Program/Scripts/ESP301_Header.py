#=========================================================================
# Newport Proprietary and Confidential    Newport Corporation 2012
#
# No part of this file in any format, with or without modification 
# shall be used, copied or distributed without the express written 
# consent of Newport Corporation.
# 
# Description: This is a Python Script to access ESP301 library
#==========================================================================

#==========================================================================
#Initialization Start
#The script within Initialization Start and Initialization End is needed for properly 
#initializing IOPortClientLib and Command Interface DLL for ESP301 instrument.
#The user should copy this code as is and specify correct paths here.
import sys
#IOPortClientLib and Command Interface DLL can be found here.
print "Adding location of IOPortClientLib.dll & Newport.ESP301.CommandInterface.dll to sys.path"
sys.path.append(r'C:\Program Files\Newport\MotionControl\ESP301\Bin')
sys.path.append(r'C:\Program Files (x86)\Newport\MotionControl\ESP301\Bin')

# The CLR module provide functions for interacting with the underlying 
# .NET runtime
import clr
# Add reference to assembly and import names from namespace
clr.AddReferenceToFile("Newport.ESP301.CommandInterface.dll")
from CommandInterfaceESP301 import *

import System
#==========================================================================