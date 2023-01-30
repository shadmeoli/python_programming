
from pprint import pprint
"""
	Create a bank system from the terminal to manage people's funds
	and also life savings

	key features:
		- Allow transcations (use I/O function to make transaction )
		- create account (use a function with arguments)
		- add funds to account (use I/O function to make transaction )
		- withdraw money (use computational function to make transaction )
		- delete account  (use computational function)


	what to use:
		- for loops
		- anounymous functons
		- I/O functions
		- Computational functions(regualr argumentargs, **kwargs)
		- conditional if statements
		- try catch

	The two other sides of the app:
		- login
		- signup

"""
our_bank = {
	1234 : [
	{
	"username" : "user_1",
	"email" : "example@mail.com",
	"phone" : 254712345678,
	"password" : "ABcd12#$",
	"Account_balance" : 205020
	}
	],
	5678 : [
	{
	"username" : "user_2",
	"email" : "example2@mail.com",
	"phone" : 25471233678,
	"password" : "ABcd12#$",
	"Account_balance" : 2020
	}
	],
	91011 : [
	{
	"username" : "user_3",
	"email" : "example3@mail.com",
	"phone" : 254712345678,
	"password" : "ABcd12#$",
	"Account_balance" : 2050
	}
	]
}

# to get uers input
id_number: int = input("Enter your id number --> ")
username: str = input("Enter your username --> ")
email: str = input("Enter your email --> ")
password: int = input("Enter your password --> ")


def signup(id_number, username, email, password):

	our_bank[id_number] = {
	"username" : username,
	"email" : email,
	"password" : password 
	}

	print("Account created")
	print(our_bank)


signup(id_number, username, email, password)