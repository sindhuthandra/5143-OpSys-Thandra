import os
import sys
import shutil
import math
import time
import threading
"""
	@Name: remove file 
	@Description:
		Removes the mentioned file
	@Params: 
		first (string) - Name of the file that needs to be removed
	@Returns: None
"""

def remove(first):
	if os.path.isfile(first):
		os.remove(first)
		print("file removed")
	else:
		print "No file"
