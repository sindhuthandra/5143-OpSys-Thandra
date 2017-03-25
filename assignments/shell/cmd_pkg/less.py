import os
import sys
import shutil
import math
import time
import threading
"""
	@Name: less
	@Description:
		Prints a first a page of a file with 25 lines at a time and then user needs to enter keyboard input to get next data
	@Params: 
		first (string) - Name of the file that needs to read
	@Returns: None
"""

def less(first):
	if os.path.isfile(first):
		if len(first)<=1:
			print("Needs 2 arguments")
		else:
			op=open("op.txt",'w')
			recorder=0
			f = open(first,'r')
			var=f.readline()
			for data in f:
				if recorder==25:
					user=raw_input("press y to continue")
					if user == "y":
						recorder=0
						continue
					else:
						break
				else:
					op.write(data)
					print data
					recorder+=1
			op.close()
			f.close()
	else:
		print "No file"
