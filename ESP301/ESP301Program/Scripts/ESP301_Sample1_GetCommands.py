#=========================================================================
# Newport Proprietary and Confidential    Newport Corporation 2012
#
# No part of this file in any format, with or without modification 
# shall be used, copied or distributed without the express written 
# consent of Newport Corporation.
#==========================================================================

import sys
sys.path.append(r'C:\Program Files\Newport\MotionControl\ESP301\Scripts')
sys.path.append(r'C:\Program Files (x86)\Newport\MotionControl\ESP301\Scripts')
from ESP301_Functions import *

#*************************************************
# Main program
#*************************************************
# Instrument Initialization
instrument="COM20"
BAUDRATE = 921600
AXIS = 1
displayFlag = 1

print 'Instrument Key=>', instrument

# Create ESP301 object
esp301 = ESP301()

# Get list of devices
ESP301_GetDeviceList(esp301)

# Open communication
ret = esp301.OpenInstrument(instrument, BAUDRATE);

# Get controller revision information
result, version = ESP301_GetControllerVersion(esp301, displayFlag) 

# Get positive software limit
result, rightlimit = ESP301_GetPositiveSoftwareLimit(esp301, AXIS, displayFlag)

# Get negative software limit
result, leftlimit = ESP301_GetNegativeSoftwareLimit(esp301, AXIS, displayFlag)

# Get current position
result, position = ESP301_GetCurrentPosition(esp301, AXIS, displayFlag)
	
# Close communication
esp301.CloseInstrument();

print 'End of script'