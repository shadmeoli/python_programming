from pprint import pprint
"""
DATA TYPES IN PYTHON

starting simple data types
""" 

# int
age: int = 22
print(int(20.56))

# float
bank_statment: float = 1500
print(float(bank_statment))

# string
name: str = "Shadrack"

# bool
married: float = False 

"""
Complex data types
"""
# tuple () -> a datatype that is hold in brackets
user_details = ("my_name", 25, True, 25000.68)
# print(type(user_details))
username = "name_2"
user_details2 = tuple(username)
# print(type(user_details2))

# list
user_details = [
	("username", "Shadrack"),
	("age", 21),
	("married", False),
	("bank_statment", 58000.93)
]
user = ["my_name", 22, False, 125563.333]

print(user_details)

# CRUD - create, read, update, delete
# create/ update
user_details.append(("loan_limit", 2000))
# read
print(user_details)
# update
user_details[1] = ("age", 22)
print(user_details)
# delete
user_details.pop(2)
del user_details[-1]
print(user_details)


# dictionary {} -> hash map containing key, value pairs
user_details = {
	
	"user_1" : [{
		"username":"Shadrack",
		"age" :17,
		"married" : False,
		"bank_statment" : 58000.93,
		"loan_record" : [200, 1000, 500, 7000]
		}],

	"user_2" : [{
		"username":"New_user",
		"age" : 23,
		"married" : True,
		"bank_statment" : 587000.93,
		"loan_record" : [250, 100, 5000, 7000]
		}]
		
}
# print(user_details)
# CRUD
# create
user_details["loan_limit"] = 2000
# read
print(user_details)
# update
user_details['married'] = True
print(user_details)
# delete
del user_details['age']
print(user_details)
user_details.pop('loan_limit')
print(user_details)
user_details.popitem()
print(user_details)
pprint(user_details['user_2'][0]['username'])


# set -> a data type used to display only unique values | cannot hold duplicate values
# immutable by index
user_ids = {2, 5, 4, 2, 6, 8, 7}
update = [21, 13, 4, 7, 9, 3]
set(user_ids)
# CRUD 
# create
user_ids.add(3)
# read
print(user_ids)
# update
user_ids.update(update)
print(user_ids)
# delete
user_ids.pop()
del user_ids[3]
print(user_ids)


"""
CONTROL FLOW 
"""

# conditional statments
# if elif else
users_age = user_details['user_1'][0]['age']

if users_age >= 18 and users_age < 60:
	print("Account is being created for this user")
elif users_age < 18:
	print("Cannot create account")
else:
	print("Redirect to retiment account")



# loops  < for loop > & < while loop >
for key, value in user_details.items():

	if users_age >= 18 and users_age < 60:
		value[0]['age'] = value[0]['age']+1
	elif users_age < 18:
		value[0]['age'] = value[0]['age']+1
		if users_age == 18:
			print("Now legal")
		else:
			print("wait for legality")
	else:
		print("Redirect to retiment account")

for key, value in user_details.items():

	records = user_details[key][0]['loan_record']

	for record in records:
		print(record)
pprint(user_details)


# while
# giving voucher to users for a limited time
time_limit = 5
voucher = 200
timer = 0
print(user_details)
while timer != time_limit:
	for key, value in user_details.items():
		user_details[key][0]["bank_statment"] = user_details[key][0]["bank_statment"] + voucher
		print("voucher added")
	timer = timer+1

	break
print(user_details)