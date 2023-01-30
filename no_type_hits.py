# not using type hints
def user_details(username, email, phone, password):
    
    
    return {
        "username" :username, 
        "email" : email,
        "phone" : phone,
        "password" : password
    }


print(user_details(
    username = input("Username: "),
    email = input("Email: "),
    phone = input("Phone: "),
    password = input("Password: ")
))