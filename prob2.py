string="neha kotwal"
str2=''
for letter in string:
	if letter.isupper():
		str2=str2+letter.lower()
	elif letter.islower():
		str2=str2+letter.upper()
	else:
		str2=str2+letter
print(str2)