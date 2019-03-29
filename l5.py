def sub(a,b):
	c=a-b
	print(c)

a=int(input("enter the num1:"))
b=int(input("enter the num2:"))
sub(a,b)


#if we want to do the above sum in another way where we need to define the actual subtraction without c in print statement

def sub(a,b):
	print(a-b)

a=int(input("enter the num1:"))
b=int(input("enter the num2:"))
sub(a,b)