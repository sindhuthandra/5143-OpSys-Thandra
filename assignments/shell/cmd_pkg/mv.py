import os
import sys
import shutil
import math
import time
import threading
"""
	@Name: move
	@Description:
		Renames first filename with second
	@Params: 
		first (string) - Name of the first file
		second (string) - Name of the second file
	@Returns: None
"""    
	
def move(first,second):
	if os.path.isfile(first):
		os.rename(first,second)
	else:
		print "No File"
