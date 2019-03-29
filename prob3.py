#write a program that lists out all the elements of the ist that are less than 5

list1=[1,1,2,3,5,8,13,21,34,55,89]
list2=[]
for number in list1:
	if number<5:
		list2.append(number)
print(list2)