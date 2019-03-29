list1=[1,12,14,13,2,4,7,9]
list2=[]
list3=[]
for number in list1:
	if number<10:
		list2.append(number)
for numbers in list1:
	if numbers>10:
		list3.append(numbers)
print(list2+list3)