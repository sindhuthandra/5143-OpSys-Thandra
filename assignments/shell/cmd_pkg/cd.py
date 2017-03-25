import os
import sys
import shutil
import math
import time
import threading
"""
	@Name: cd
	@Description:
		Does a directory change
	@Params: 
		newDir (string) - Opens the folder specified in the shell.
	@Returns: None
"""

def cd(newDir):
	try:
		os.chdir(newDir) #given directory
		if newDir[0]=="..":
			os.chdir(os.newDir.oldpwd(newDir))
		elif newDir[0]=="~":
			os.chdir(os.newDir.expanduser(newDir)) # open home directory

	except:
	   print("could find the folder entered")
	 #previous directory
	