from rich.console import Console

console = Console()


def signup(name, email, password, confirm_password):


    # excepton handler
    try:

        # continuing 
        if len(name) > 3:
            
            if confirm_password == password:
                
                if len(password) < 8:
                    console.log("Password is too short")
                else:
                    
                    if email.endswith("@gmail.com"):
                        console.log({"username":name, "email":email, "password":password})
                    else:
                        console.log({"Error" : "Invalid mail"})
            
            else:
                console.log({"Error" : "Passwords do not match"})
        else:
            console.log({"Error" : "Username too short"})
    
    except Exception as e:
        console.log({"Error" : e})


signup(
    "Shk",
    "examplemail@gmail.com",
    "examplepassword",
    "examplepassword"
)