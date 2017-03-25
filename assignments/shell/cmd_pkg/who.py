import os
import sys
import shutil
import math
import time
import threading
"""
	@Name: who
	@Description:
		Lists Users who are currently logged in 
	@Params: 
		
	@Returns: None
"""

def who():
	print(os.popen('who').read())
