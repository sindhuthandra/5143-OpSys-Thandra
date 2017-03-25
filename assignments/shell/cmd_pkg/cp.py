import os
import sys
import shutil
import math
import time
import threading
"""
	@Name: copy
	@Description:
		Copies filenames
	@Params: 
		first (string) - Name of the first file
		second (string) - Name of the second file
	@Returns: None
"""
def copy(first,second):
	if os.path.isfile(first):
		shutil.copyfile(first,second) 
	else :
		print "No such file"

