from addpart import addparti
from addpart import seeparti

while True:
	todo=input("enter your choice: \n\
		1. add participants\n\
		2. seecparticipants")

	if todo=='1':
		addparti()
	elif todo=='2':
		seeparti()
	else:
		break


