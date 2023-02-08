from pprint import pprint

def signup(name, email, password, confirm_password):


    # excepton handler
    try:

        # continuing 
        if len(name) > 3:
            
            if confirm_password == password:
                
                if len(password) < 8:
                    pprint("Password is too short")
                else:
                    
                    if email.endswith("@gmail.com"):
                        pprint({"username":name, "email":email, "password":password})
                    else:
                        pprint({"Error" : "Invalid mail"})
            
            else:
                pprint({"Error" : "Passwords do not match"})
        else:
            pprint({"Error" : "Username too short"})
    
    except Exception as e:
        pprint({"Error" : e})


signup(
    "Shad",
    "examplemail@gmail.com",
    "examplepassword",
    "examplepassword"
)