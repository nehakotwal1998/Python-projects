#{} flower brackets create dictionary
fruits={'apple':'sour','mango':'sweet'}
key1=input("enter a key")
value1=input("enter the value")
if key1 not in fruits.keys():
	fruits[key1]=value1
print(fruits)

