import os
import sys
import shutil
import math
import time
import threading
"""
	@Name: head
	@Description:
		Prints a first page of a file  at a time
	@Params: 
		first (string) - Name of the file that needs to read
	@Returns: None
"""

def head(first):
	if os.path.isfile(first):
		if len(first)<=1:
			print("Needs 2 arguments")
		else:
			op=open("op.txt",'w')
			recorder=0
			f = open(first,'r')
			var=f.readline()
			for data in f:
				if recorder==15:
				   break;  
								  
				else:
					recorder+=1
					op.write(data)
			op.close()
	else:
		print "no file"
