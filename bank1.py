class AccountManager:

	def __init__(self, account_name, account_number, balance, pin):
		self.account_name = account_name
		self.account_no = account_no
		self.balance = float(balance)
		self.pin = pin
		self.transactions = []

	def deposit(self, amount = 0.0):
		pass
	
	def withdraw(self, amount=0.0):
		if (self.balance - amount) < 0:
			print("Insufficient Balance")
			
		else:
			self.balance -= amount
			transaction = ('-'+str(amount), self.balance)
			self.transactions.append(transaction)

	def show_balance(self):
		pass

	def account_statement(self):
             pass


class SavingsAccount(AccountManager):
	
	def __init__(self, account_name, account_number, balance, pin):
		pass


class CurrentAccount(AccountManager):
	
	def __init__(self, account_name, account_number, balance, pin):
		pass

	def withdraw(self, amount=0.0):
		pass