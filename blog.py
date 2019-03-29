#parentclass

class BlogManager:
	def __init__(self,profile_no,profile_name,email_id,delivery_address):
		self.profile_no=profile_no
		self.profile_name=profile_name
		self.email_id=email_id
		self.delivery_address=delivery_address

	def access(self,profile_no,profile_name,email_id):
		pass

	def receivecopy(self,profile_name,profile_no,delivery_address):
		pass

	def deliverdish(self,profile_name,profile_no,delivery_address):
	    pass


#childclasses

class Milkshakes(BlogManager):
	def __init__(self,profile_name,email_id):
		pass

class Sandwiches(BlogManager):
	def __init__(self,profile_name,email_id):
		pass
