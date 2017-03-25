import os
import sys
import shutil
import math
import time
import threading
"""
	@Name: tail
	@Description:
		Prints last page of a file  at a time
	@Params: 
		first (string) - Name of the file that needs to read
	@Returns: None
"""

def tail(first):
	if os.path.isfile(first):
		if len(first)<=1:
			print("Needs 2 arguments")
		else:
			op=open("op.txt",'w')
			recorder=20
			num=0
			numLines=sum(1 for line in open(first))
			f = open(first,'r')
			for lines in f:
				num=num+1 
				if numLines-num<=recorder:
					op.write(lines)
	else:
		print "no file"
			

