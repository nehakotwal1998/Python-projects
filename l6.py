def mul():
	a=int(input("enter the num1:"))
	b=int(input("enter the num2:"))
	c=a*b
	print(c)
	
mul()

# taking input within functions

# or we can do it another way

def mul(a,b):
	c=a*b
	print(c)

a=int(input("enter the num1:"))
b=int(input("enter the num2:"))
	
mul(a,b)

#to understannd the code the way it works given below

def mul(a,b):
	print("inside the function")
	print(a)
	print(b)
	print('='*20)
	c=a*b
	print(c)

a=int(input("enter the num1:"))
b=int(input("enter the num2:"))

print(a)
print(b)
print("outside the function")	
mul(a,b)



