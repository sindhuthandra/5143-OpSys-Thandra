import os
import sys
import shutil
import math
import time
import threading
import string
"""
	@Name: wc
	@Description:
		Does wordcount in  a file
	@Params: 
		file (string) - Name of the file that needs the words counted
	@Returns: None
"""

def wc(parts):
	str =" "
	if len(parts) < 1:
		print("@ arguemnets")
	else:
		op=open("op.txt",'w')
		lines=0
		words=0
		chars=0
		f=open(parts[1],'r')
		data = f.read()
		chars = len(data)
		words = len(data.split())
		lines = len(data.split('\n'))

		# output="Num of words in "+ file + " are " +str(numWords)
		k=lines.__str__()+"  "+words.__str__()+ " "+ chars.__str__()+" "+ parts[1].__str__()
		
		# +str(words)+" " +str(chars)+" "+str(parts[1])
		op.write(k)
		op.close()
