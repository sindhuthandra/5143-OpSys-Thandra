import os
import sys
import shutil
import math
import time
import threading
"""
	@Name: remove directory
	@Description:
		Removes the mentioned directory
	@Params: 
		first (string) - Name of the directory that needs to be removed
	@Returns: None
"""

def rmdir(first):
	if os.path.isdir(first):
		shutil.rmtree(first)
	#print("directory removed")
	else:
		print "No directory"
