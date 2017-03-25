import os
import sys
import shutil
import math
import time
import threading
import stat
from pwd import getpwuid
from os import stat
def binary(p):
	#if os.path.isdir:
		if p==777:
			return "rwxrwxrwx"
		if p==456:
			return "r--r-xrw-"
		if p==555:
			return "r-xr-xr-x"
		if p==666:
			return "rw-rw-rw-"
		if p==765:
			return "rwxrw-r-x"
		if p==755:
			return "rwxr-xr-x"
		if p==756:
			return "rwxr-xrw-"
		if p==644:
			return "rw-r--r--"
def size_convert(size):
	suffixes=['B','KB','MB','GB','TB']
	precision=3
	suffixIndex = 0
	while size > 1024 and suffixIndex < 4:
		suffixIndex += 1 #increment the index of the suffix
		size = size/1024.0 #apply the division
	return "%.*f%s"%(precision,size,suffixes[suffixIndex])

def ls(part,flag):
	op=open("op.txt",'w')
	if flag==0:
		list=os.listdir(os.getcwd())
		list.sort()
		for i in list:
			if i.startswith('.'):
				list.remove(i)
		for i in list:
			op.write(i)
			op.write("   ") 
	elif flag=='-a':
			list=os.listdir(os.getcwd())
			list.sort()
			for i in list:
				op.write(i)
				op.write("\t") 
	elif flag=='-h':
			list=os.listdir(os.getcwd())
			list.sort()
			for i in list:
				if i.startswith('.'):
					list.remove(i)
			for i in list:
				op.write(i)
				op.write("\t") 
	elif flag=='-l':
			list=os.listdir(os.getcwd())
			list.sort()
			for i in list:
				if i.startswith('.'):
					list.remove(i)
			for i in range(len(list)):
				info=os.stat(list[i])
				atime=time.asctime(time.localtime(info.st_atime))
				name=getpwuid(stat(list[i]).st_uid).pw_name
				permissions = os.stat(list[i]).st_mode
				p=int(oct(permissions & 0777))
				p1=binary(p)
				#if os.path.isdir(i):
					#if os.path.isdir(list(i))==True:
						#isdir(i)==True
						#p2="d"+p1
				#else :
					#p2="d"+p1
				str=p1.__str__()+"\t"+name.__str__()+"\t"+ name.__str__() +"\t"+info.st_size.__str__()+"\t"+atime.__str__()+"\t"+list[i].__str__()
				op.write(str)
				op.write("\n") 
	
	elif flag=="-la":
		list=os.listdir(os.getcwd())
		list.sort()
		for i in range(len(list)):
			info=os.stat(list[i])
			# print info
			# atime=info.st_atime
			atime=time.asctime(time.localtime(info.st_atime))
			name=getpwuid(stat(list[i]).st_uid).pw_name
			permissions = os.stat(list[i]).st_mode
			p=int(oct(permissions & 0777))
			p1=binary(p)
			str=p1.__str__()+"\t"+name.__str__()+"\t"+ name.__str__() +"\t"+info.st_size.__str__()+"\t"+atime.__str__()+"\t"+list[i].__str__()
			op.write(str)
			op.write("\n") 
		
	elif flag=="-ah":
		list=os.listdir(os.getcwd())
		list.sort()
		for i in list:
			op.write(i)
			op.write("\t") 

	elif flag=='-lh':
		list=os.listdir(os.getcwd())
		list.sort()
		for i in list:
			if i.startswith('.'):
				list.remove(i)
		for i in range(len(list)):
			info=os.stat(list[i])
			# print info
			# atime=info.st_atime
			atime=time.asctime(time.localtime(info.st_atime))
			name=getpwuid(stat(list[i]).st_uid).pw_name
			permissions = os.stat(list[i]).st_mode
			p=int(oct(permissions & 0777))
			p1=binary(p)
			k=size_convert(info.st_size)
			str=p1.__str__()+"\t"+name.__str__()+"\t"+ name.__str__() +"\t"+k.__str__()+"\t\t"+atime.__str__()+"\t"+list[i].__str__()
			op.write(str)
			op.write("\n") 
	elif flag=='-lah':
		list=os.listdir(os.getcwd())
		list.sort()
		for i in range(len(list)):
			info=os.stat(list[i])
			# print info
			# atime=info.st_atime
			atime=time.asctime(time.localtime(info.st_atime))
			name=getpwuid(stat(list[i]).st_uid).pw_name
			permissions = os.stat(list[i]).st_mode
			p=int(oct(permissions & 0777))
			p1=binary(p)
			k=size_convert(info.st_size)
			str=p1.__str__()+"\t"+name.__str__()+"\t"+ name.__str__() +"\t"+k.__str__()+"\t\t"+atime.__str__()+"\t"+list[i].__str__()
			op.write(str)
			op.write("\n") 
	op.close()