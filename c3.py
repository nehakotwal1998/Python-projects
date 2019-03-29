#given an element search in list return the indices
#input=[1,2,3,2,0,,65,21,4,2,10]
#element=2

list1=[1,2,3,2,0,65,21,4,2,10]
list2=[]
search=int(input("enter search element:"))
for (i,val) in enumerate(list1):
	if val is search:
		list2.append(i)
		print(list2)

