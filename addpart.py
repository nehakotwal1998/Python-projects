events_dict={'1':'CS','2':'google it','3':'treasure hunt'}
participant_details={}

def addparti():
	name=input("enter the name of the participant:")
	event=input("enter the number event participating :")
	participant_details[name]=events_dict[event]
	return participant_details


def seeparti():
	for key,value in participant_details.items():
		print(key,value,sep='-')


if __name__ == '__main__':
	addparti()
	print(participant_details)
	seeparti()

