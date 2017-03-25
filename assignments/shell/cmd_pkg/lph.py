"""
@Name: loadprevioushistory
@Description:
	Needs to give the integer value from the history list and checks display the data of particular command .
@Methods:
	push_command - add command to history
	get_commands - get all commands from history
	number_commands - get number of commands in history
"""

def lph(first):
	lineNumber=1
	cmnd=""
	num=int(first.strip('!'))
	f=open('list.txt','r')
	for l in f:
		# print(l)
		if lineNumber==num:
			cmnd=l.strip(str(lineNumber) + " ").strip('\n')
		lineNumber=lineNumber+1
	print (cmnd)
	return cmnd
	#runShell()
	