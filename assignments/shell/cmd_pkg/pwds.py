import os
import sys
import shutil
import math
import time
import threading
"""
	@Name: pwd
	@Description:
		Prints the present working directory
	@Returns: None
"""

def pwds():

	try:
		op=open("op.txt",'w')
		dir = os.getcwd()
		op.write(dir) 
		op.close()
	except:
		return dir
