import os
import sys
import shutil
import math
import time
import threading
"""
	@Name: cat
	@Description:
		Prints the data in the file
	@Params: 
		first (string) - Name of the file that needs to read
	@Returns: None
"""


def cat(parts):
	if os.path.isfile(parts[1]):
		if len(parts)==2:
			f = open(parts[1],'r')
			op=open("op.txt",'w')
			for line in f:
				op.writelines(line)
			f.close()
			op.close()
		else :
			 print("Needs 2 arguments!")
	else:
		print "No file"

