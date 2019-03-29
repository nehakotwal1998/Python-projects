import csv
with open('file.csv','r',newline="") as myfile:#to read from a file 'r' mode
	rd=csv.reader(myfile)
	for i in rd:
 		print(i)#here the index tells u the 1st colu or second column
