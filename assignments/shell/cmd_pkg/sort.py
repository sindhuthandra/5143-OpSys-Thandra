import os
import sys
import shutil
import math
import time
import threading
"""
	@Name: sort
	@Description:
		sorts the data in a given file 
	@Params: 
		first (string) - Name of the file that needs to read
	@Returns: None
"""

def sort(first):
	if len(first)<=1:
		print("Needs 2 arguments")
	else:
		op=open("op.txt",'w')
		with open(first) as f:
			for data in sorted(f):
				op.write(data)
	op.close()
