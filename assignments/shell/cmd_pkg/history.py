"""
@Name: history
@Description:
	Maintains a history of shell commands to be used within a shell environment.
@Methods:
	push_command - add command to history
	get_commands - get all commands from history
	number_commands - get number of commands in history
"""

def history(command_history):
	l=1
	op=open("op.txt",'w')
	f=open('list.txt','r')
	for i in f: 
		text=l.__str__()+" "+i
		op.write(text)
		l=l+1
	op.close()
