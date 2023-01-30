# simple agrument - passed into the funtion
# *args - used to tell the function to accept mulitple agruments
# **kwargs - key word argument

# anonymous function - single line functions
add_age = lambda age: age + 1
# print(add_age(22))


# I/O(input - output ) function - they dont mutate values passed in
def bodmas(x, y, z) -> int:
	return (x+y)*z

# without declaring the arguments
# print(bodmas(z=5,x=2,y=6))
# with declaring the arguments
# print(bodmas(z=5,x=2,y=6))

# computational functions
def user_data(username, email, password):
	return username, email, password

def intrests(*args: list):
	return args

def friends(**kwargs):
	return kwargs


# user registraion
# print(user_data("shad", "emails@example.com", '!@#$ABcd'))
food = {
	"foods" : ["pizza", 'burger', 'chicken nuggets', 'hot dog']
}
places = {
	"location" : ['lamu', 'kericho', 'naivasha', 'amboseli']
}

hobbies = {
	"hobbies" : ['movies', 'music', 'dancing', 'yoga', 'gym']
}
data = intrests([food], [places], [hobbies])
# print(data[0][0]['foods'])

user_friends = friends(
	tech="joma",
	home="Alex",
	work="Edd",
	school="Stacy"
	)


# try and exceptions try, except, finally

# sign = user_data()
def database_check():
	
	try:
		print(user_data())
	except Exception as typeError:
		1+1
		# print("User you details for account creation")
	except:
		2+2
		# print(user_data("shad", "emails@example.com", '!@#$ABcd'))
	finally:
		print(True)

if database_check:
	print("check done")