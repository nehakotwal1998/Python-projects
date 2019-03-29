from blog import BlogManager

accounts={}
account_no=01
print("Welcome to Orenilla")


while True:
	print("Hi there! What plans for today ?\n\n\
		   1.Create Profile\n\
		   2.Access Recipes\n\
		   3.Receive Copy\n\
		   4.Delivery of Dish\n\
		   5.Exit\n")

	choice = int(input("Enter your option: "))

	if choice==1:
		profile_name=input("Enter a Profile name:")
		email_id=input("Enter a gmail id")

		profiles[profile_no] = BlogManager(profile_name, profile_no,email_id)
		print(profiles)

		print(f"Profile created successfully! Your Profile number is {profile_no}")

		profile_no += 1

	elif choice==2:
		profile_no=input("Enter profile_no:")

		print("What would you like to cook today ?\n\n\
			1.Milkshakes\n\
			2.Sandwiches\n")

		choice1 = int(input("Enter your option: "))

		if choice1 == 1
			print("blahblah")

		else choice1 == 2
			print("blahblah")


	elif choice == 3:
		print("Do you want a copy of our Recipes ? Cool cuz you just have to pay Rs.100 to the delivery guy :) ")
		delivery_address=input("Enter the delivery address:")
		print("Enjoy!!you will receive the copy in 42 working hours")

	elif choice == 4:
		print("Wohoo we are ready for serving orders now ")
		print("Choose what would you like to have today from below options : \n\n\
			1Mocha Oreo Milkshake\n\
			2.Apple Carrot Milkshake\n\
			3.Mint Brownie Milkshake\n\
			4.Classic Vanillla Milkshake\n\
			5.Capsicum Cabbage Sandwich\n\
			6.Carrot Sandwich\n\
			7.Grilled Tomato Cheese Sandwich\n\
			8.PBJ Sandwich")

		choice2=int(input("Enter your choice:"))

		if choice2 ==

