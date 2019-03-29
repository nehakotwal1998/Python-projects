import csv
with open('file.csv','a',newline="") as myfile:
	wr = csv.writer(myfile, dialect='excel')#dialect tells where to store the file in which format and w is write mode means we are writing and a is for append
	wr.writerow(['shiro','pepo'])#always close the csv file while changing
	wr.writerow(['shiro','pepo'])
	wr.writerow(['shiro','pepo'])
	wr.writerow(['shiro','pepo'])

	#to view values in file and write in a file