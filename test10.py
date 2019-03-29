list=[]
num=int(input("enter length:"))
for i in range (num):
	numbers=int(input("enter the numbers in the list:"))
	list.append(numbers)
print("sum of elements in a list:",sum(list))