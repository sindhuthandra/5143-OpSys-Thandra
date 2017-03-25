import os
import sys
import shutil
import math
import time
import threading
"""
	@Name: grep 
	@Description:
		searches for the given keyword in given file and will returns the entire line that has with keyword 
	@Params: 
		first (string) - Name of the keyword that needs to find in given file.
		second (String) - Name of the given file 
	@Returns: None
"""

def grep(parts):
	if os.path.isfile(parts[2]):
		recorder=0
		if len(parts)<=2:
			print("Needs 3 arguments")
		else:
			first=parts[1]
			second=parts[2]
			op=open("op.txt",'w')
			f = open(second,'r')
			for line in f:
				# var=f.readline()
				if first in line:
					recorder=1
					op.write (line)
			if recorder==0:
				op.write ("No matches found")
			op.close()
	else:
		print "No file"
