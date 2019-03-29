class AccountManager:

	 def __init__(self,name,account_no,balance):
	 	self.name=name
	 	self.account_no=account_no
	 	self.balance=balance
	 	

	 def deposit(self,amount):
	 	if amount > 10000:
	 		print("u cant add")
	 	elif amount < 0:
	 		print("bankrupt")
	 	else:
	 		self.balance += amount


	 def withdraw(self,amount):
	 	if amount >  self.balance:
	 		print("insufficient balance")
	 	else:
	 		self.balance -= amount

	 def show_balance(self):
	 	print(f"the balance is {self.balance}")