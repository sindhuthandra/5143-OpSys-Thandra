import os
import sys
import shutil
import math
import time
import threading
"""
	@Name: changeModify
	@Description:
		Does a directory listing
	@Params: 
		num (integer) - Levels of permission to be set to the file
		second (String) - Name of the file that needs the permission change
	@Returns: None
"""

def changeModify(num,second):
	print("in chmod func")
	permission=int(num,8)
	os.chmod(second,permission)
	