import os
import sys
import shutil
import math
import time
import threading
from cmd_pkg import Commands
from subprocess import Popen,PIPE 	 

command_history = [] #list to hold all commands
flag=0

"""
	@Name: runShell
	@Description:
		Loop that drives the shell environment
	@Params: None
	@Returns: None
"""
flag=0
def runShell(part,flag,nf):
		if flag==1:
				inp=part
			# append
		elif flag==2:
				inp=part
			# pipe
		elif flag==3: 
				inp=part
		elif flag=="!":
				inp=part
				flag=0
		else:
				inp=part
				inp1=part
				pass
		parts=inp.split(" ")
	

		
	
# if ! symbol is found when user enters input then this function will cals and displays the corresponding output of displays the particular command output.
		if '!' in inp:
			# inp=Commands.lph.lph(inp)
			# parts = inp.split(" ") 
			parts=inp.split("!")
			l=int(parts[1])
			ctr=1
			f=open('list.txt','r')
			for line in f:
				if (l==ctr):
					new_cmd= line.strip()
					break
				else :
					ctr=ctr+1
			runShell(new_cmd,"!","")	
# if > symbol is found when user enters input then this function will cals and displays the corresponding output of redirecting into file.
		if '>>' in inp:
			# parts=Commands.append.append(inp)
			# f=open('sample.txt','w+')
			# f.write("helloworld")
			# #for l in f:
			# print(f)
			flag=2
			main_command = inp.split(">>")
			filename = main_command[1].strip()
			runShell(main_command[0].strip(),2,filename)
		elif '>' in inp:
			flag=1
			main_command = inp.split(">")
			filename = main_command[1].strip()
			runShell(main_command[0].strip(),1,filename)
# if >> symbol is found when user enters input then this function will cals and displays the corresponding output of appending data into a file.
		
# if | symbol is found when user enters input then this function will sends the output of first command to the input tothe second command.
		elif '|' in inp:
			main_command = inp.split("|")
			flag=3
			for i in range(len(main_command)):
				if i==0:
					runShell(main_command[i].strip(),flag,"")
				else:
					Commands.mv.move("op.txt","op1.txt")
					runShell(main_command[i].strip()+ " op1.txt",flag,"")
			# flag=0
			op=open("op.txt",'r')
			print op.read()
			op.close()
		elif '<' in inp:
			inp1=inp.split("<")
			cmd=inp1[0]+ " " + inp1[1]
			runShell(cmd,0,"")
			

			
# Prints the history of the user of every session when he login into the shell.
		else:
			if parts[0] == "history":
				t=threading.Thread(target=Commands.history.history(command_history),args=(command_history,))
				t.start()
				t.join()
				op=open("op.txt",'r')
				if flag==1:
					ow=open(nf,'w')
					for l in op:
						ow.write(l)
					ow.close()
					flag=0
				elif flag==2:
						ow=open(nf,'a')
						for l in op:
							ow.write(l)
						ow.close()
						flag=0
				else:
					print(op.read())
				op.close()

	# This function will calls when user needs to copy one file data into other file.
			elif parts[0] == "cp":
				if len(parts)==3:
					f1=parts[1]
					f2=parts[2] 
					t=threading.Thread(target=Commands.cp.copy(f1,f2),args=(f1,f2,))
					t.start()
					t.join()
				else:     #to detect error
				   print("Needs 3 arguments")
	# This function will calls when user needs to move one file data into other file.
			elif parts[0]=="mv":
				if len(parts)==3:
					p1=parts[1]
					p2=parts[2]
					t=threading.Thread(target=Commands.mv.move(p1,p2),args=(p1,p2))
					t.start()
					t.join()			  

				else:
					print("Needs 3 arguments")
	# This function will calls when user needs to remove the file.
			elif parts[0]=="rm":
				if len(parts)==2:
					a1=parts[1]		   
					t=threading.Thread(target=Commands.rm.remove(a1),args=(a1,))
					t.start()
					t.join()			  
				else:
					print("Needs 2 arguments")
	# This function will calls when user needs to remove the directory.
			elif parts[0]=="rmdir":
				if len(parts)==2:
					z1=parts[1]
					t=threading.Thread(target=Commands.rmdir.rmdir(z1),args=(z1,))
					t.start()
					t.join()			  
				else:
					print("Needs 2 arguments")
	# This function will calls when user needs to show the entire content of the file on the screen.
			elif parts[0]=="cat":
					t=threading.Thread(target=Commands.cat.cat(parts),args=(parts,))			  
					t.start()
					t.join()
					op=open("op.txt",'r')
					if flag==1:
						ow=open(nf,'w')
						for l in op:
							ow.write(l)
						ow.close()
						flag=0
					elif flag==2:
						ow=open(nf,'a')
						for l in op:
							ow.write(l)
						ow.close()
						flag=0
					elif flag==3:
						pass
					else:
						print(op.read())
					op.close()
					return
				# else:
					# print("Needs 2 arguments! a ")
	# This function will calls when user needs to show the entire content of the file on the screen page by page.
			elif parts[0]=="less":
				#if len(parts)==2:
					c1=parts[1]
					t=threading.Thread(target=Commands.less.less(c1),args=(c1,))
					t.start()
					t.join()			 
					op=open("op.txt",'r')
					if flag==1:
						ow=open(nf,'w')
						for l in op:
							ow.write(l)
						ow.close()
						flag=0
					elif flag==2:
						ow=open(nf,'a')
						for l in op:
							ow.write(l)
						ow.close()
						flag=0
					elif flag==3:
						pass
					else:
						print(op.read())
					op.close()
					return
				#else:
					#print("Needs 2 arguments")
	# This function will calls when user needs to show the head of the file on the screen.
			elif parts[0]=="head":
				# if len(parts)==2:
					c1=parts[1]
					t=threading.Thread(target=Commands.head.head(c1),args=(c1,))
					t.start()
					t.join()
					op=open("op.txt",'r')
					if flag==1:
						ow=open(nf,'w')
						for l in op:
							ow.write(l)
						ow.close()
						flag=0
					elif flag==2:
						ow=open(nf,'a')
						for l in op:
							ow.write(l)
						ow.close()
						flag=0
					elif flag==3:
						pass
					else:
						print(op.read())
					op.close()
					return
				# else:
					# print("Needs 2 arguments")
	# This function will calls when user tries to find some particular keyword in a file and needs to display that entire line.
			elif parts[0]=="grep":
					#if len(parts)==3:
					t=threading.Thread(target=Commands.grep.grep(parts),args=(parts,))
					t.start()
					t.join()
					op=open("op.txt",'r')
					if flag==1:
						ow=open(nf,'w')
						for l in op:
							ow.write(l)
						ow.close()
						flag=0
					elif flag==2:
						ow=open(nf,'a')
						for l in op:
							ow.write(l)
						ow.close()
						flag=0
					elif flag==3:
						pass
					else:
						print(op.read())
					op.close()
					return
				#else:
					#print("Needs 2 arguments")
	# This function will calls when user needs to show the last page of the file on the screen.
			elif parts[0]=="tail":
				#if len(parts)==2:
					c1=parts[1]
					t=threading.Thread(target=Commands.tail.tail(c1),args=(c1,))
					t.start()
					t.join()
					op=open("op.txt",'r')
					if flag==1:
						ow=open(nf,'w')
						for l in op:
							ow.write(l)
						ow.close()
						flag=0
					elif flag==2:
						ow=open(nf,'a')
						for l in op:
							ow.write(l)
						ow.close()
						flag=0
					else:
						print(op.read())
					op.close()
				#else:
					#print("Needs 2 arguments")			   
	# This function will calls when user needs to change the permissions of a particular file. 
			elif parts[0]=="chmod":
				if len(parts)==3:
					d1=parts[1]
					d2=parts[2]			   
					t=threading.Thread(target=Commands.chmod.changeModify(d1,d2),args=(d1,d2,))
					t.start()
					t.join()			   
				else:
					print("Needs 3 arguments")
	# This function will calls when user needs to go back to the previous path (or) before directory.
			elif parts[0]=="cd":
				if len(parts)==2:
					e1=parts[1]
					t=threading.Thread(target=Commands.cd.cd(e1),args=(e1,))
					t.start()
					t.join()				
				else :
					print("Needs 2 arguments")
	# This Command will calls when the user needs to count the total words in a file. 
			elif parts[0]=="wc":
				#if len(parts) > 1:
				h1=parts[1] 
				t=threading.Thread(target=Commands.wc.wc(parts),args=(parts,))
				t.start()
				t.join()
				op=open("op.txt",'r')
				if flag==1:
					ow=open(nf,'w')
					for l in op:
						ow.write(l)
					ow.close()
					flag=0
				elif flag==2:
						ow=open(nf,'a')
						for l in op:
							ow.write(l)
						ow.close()
						flag=0
				elif flag==3:
						pass
				else:
					print(op.read())
				op.close()
				return
				#else:
					#print("Needs more than 1 argument")
	# This Command will calls when user needs to quit out from the shell.
			elif parts[0]=="quit":
				t=threading.Thread(target=quit())
				t.start()
				t.join()
	# This Command will shows who is the current user login into the shell.
			elif parts[0]=="who":
				t=threading.Thread(target=Commands.who.who())
				t.start()
				t.join()			
	# This Command will calls when user needs to find the present working directory.
			elif parts[0]=="pwd":
				t=threading.Thread(target=Commands.pwds.pwds())
				t.start()
				t.join()
				op=open("op.txt",'r')
				if flag==1:
					ow=open(nf,'w')
					for l in op:
						ow.write(l)
					ow.close()
					flag=0
				elif flag==2:
						ow=open(nf,'a')
						for l in op:
							ow.write(l)
						ow.close()
						flag=0
				elif flag==3:
						pass
				else:
					print(op.read())
				op.close()
				return
	# This Command will calls when user needs to sort the entire data in a particular file.
			elif parts[0]=="sort":
				if len(parts)>1:
					f1=parts[1]
					t=threading.Thread(target=Commands.sort.sort(f1),args=(f1,))
					t.start()
					t.join()
				op=open("op.txt",'r')
				if flag==1:
					ow=open(nf,'w')
					for l in op:
						ow.write(l)
					ow.close()
					flag=0
				elif flag==2:
						ow=open(nf,'a')
						for l in op:
							ow.write(l)
						ow.close()
						flag=0
				elif flag==3:
						pass
				else:
					print(op.read())
				op.close()
				return
				   
				#else:
					#print("Needs the directory name.")			 
	# This Command will calls when user needs to create a new directory.
			elif parts[0]=="mkdir":
				if len(parts)>1:
					f1=parts[1]
					t=threading.Thread(target=Commands.mkdir.makeDir(f1),args=(f1,))
					t.start()
					t.join()			   
				   
				else:
					print("Needs the directory name.")			
	# This Command will calls when user to find the list of all files present in that particular path.
			elif parts[0]=="ls":
				if len(parts)==1:
					# print "hai"
					f=0
				else:
					# print "hello"
					f=parts[1]
				t=threading.Thread(target=Commands.ls.ls(parts[0],f),args=(parts[0],f,))
				t.start()
				t.join()
				op=open("op.txt",'r')
				if flag==1:
					ow=open(nf,'w')
					for l in op:
						ow.write(l)
					ow.close()
					flag=0
				elif flag==2:
					ow=open(nf,'a')
					for l in op:
						ow.write(l)
					ow.close()
					flag=0
				elif flag==3:
					pass
					#op.close()
					#Commands.mv.move("op.txt","op1.txt")
					#cmd=pipe+" op1.txt"
					# print cmd
					# op.close()
					# runShell(cmd,3,"","")
				else:
					print(op.read())
				op.close()
				return
        
"""
@Name: Main
@Description:
	When  user runs the program the pointer will comes directly here .
@Methods:
	push_command - add command to history
	get_commands - get all commands from history
	number_commands - get number of commands in history
"""

if __name__=='__main__':
	flag=0
	while True:
		
		if flag==1:
			inp=part
		# append
		elif flag==2:
			inp=part
		# pipe
		elif flag==3: 
			inp=part
		elif flag=="!":
			inp=part
			flag=0
		else :
# % symbol will appears every time while user runs the shell
			inp= raw_input('% ')
		# parts = inp.split(" ")
		hfile=open("list.txt",'a')
		hfile.write(inp)
		hfile.write("\n")
		hfile.close()
		runShell(inp,0,"")
	
	