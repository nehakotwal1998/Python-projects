from models import *

def  add_events():
	event_name = input("Enter the name of the event you want to add:")

	EventsList.create(event_name=event_name)

def see_events():
	events=EventsList.select()

	for event in events:
		print(event.id,event.event_name,sep=" - ")

def add_participants():
	participants_name = input("Enter the name of the participant:")
	events=EventsList.select()
	for event in events:
		print(event.id,event.event_name,sep=" - ")
	event_id = int(input("Select the event in which the participant whant to participate in: \n"))

	ParticipantList.create(participant_name=participant_name,event_name=event_id)

def see_participants():
	for participant in ParticipantsList.select():
		print(participant.id,participant.participant_name,EventsList.get(participant.event_name_id).event_name ,sep=" - ")

	



while True:
	choice = input("Enter the action that ypu want to do : \n 1.Add Event\n 2.See Event \n 3.Add participant\n 4.See participant \n 5.Exit")
	if choice=='1':
		add_events()
	elif choice=='2':
		see_events()
	elif choice=='3':
		add_participants()
	elif choice=='4':
		see_participants()
	else:
		break
