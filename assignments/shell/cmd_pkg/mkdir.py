import os
import sys
import shutil
import math
import time
import threading
"""
	@Name: mkdir
	@Description:
		Creates a folder with the name given in the parameter
	@Returns: None
"""

def makeDir(dir):
	if dir != "":
		os.mkdir(dir)
	else:
		print ("Enter a file name and run command again")
