#find word in diction to searc word speck 

dictio={1:'speckbit',2:'world',3:'quiet'}
search=input("enter the word to search")
if search not in dictio.values():
	print(False)
else:
	print(True)
	

