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
from ESP301_Header import *

#*************************************************
# Procedure to get the controller version
#*************************************************
def ESP301_GetControllerVersion (ESP, flag):
	result, version, errString = ESP.VE() 
	if flag == 1:	
		if result == 0:
			print 'Controller version => ',version
		else:
			print 'Error=>',errString
	return result, version

#*************************************************
# Procedure to get the current position
#*************************************************
def ESP301_GetCurrentPosition (ESP, axis, flag):	
	result, position, errString = ESP.TP(axis) 
	if flag == 1:
		if result == 0 :
			print 'current position=>', position
		else:
			print 'Error=>',errString	
	return result, position
	
#*************************************************
# Procedure to get the Right limit
#*************************************************
def ESP301_GetPositiveSoftwareLimit (ESP, axis, flag):	
	result, limit, errString = ESP.SR_Get(axis) 
	if flag == 1:
		if result == 0 :
			print 'positive software limit=>', limit
		else:
			print 'Error=>',errString
	return result, limit
		
#*************************************************
# Procedure to get the Left limit
#*************************************************
def ESP301_GetNegativeSoftwareLimit (ESP, axis, flag):	
	result, limit, errString = ESP.SL_Get(axis) 
	if flag == 1:
		if result == 0 :
			print 'negative software limit=>', limit
		else:
			print 'Error=>',errString
	return result, limit
	
#*************************************************
# Procedure to list the connected devices  
# from NSTRUCT server
#*************************************************	
def ESP301_GetDeviceList (ESP):
	print '-----------------------------------------------------------'
	# Get the list of detected devices
	strDeviceArray = ESP.GetDevices() 
	nbItems = len(strDeviceArray)
	if nbItems > 0 :
		for i in range(nbItems):
			print i+1, ') ', strDeviceArray[i]
	else:
		print 'No detected devices'
	print '-----------------------------------------------------------'
