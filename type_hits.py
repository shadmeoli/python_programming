from dataclasses import dataclass

# pip install pydantic "pydantic[email]"    
from pydantic import BaseModel, EmailStr

# using type hints str, int, float, bool
username: str = None
email: str = None
phone: int = None
password: str = None


def user_details(
    username: str,
    email: str,
    phone: int,
    password: str
    ):

    return {
        "username" :username, 
        "email" : email,
        "phone" : phone,
        "password" : password
    }



@dataclass
class UserDetails:

    # using type hints
    username: str
    email: str
    phone: int
    password: str


username = None
email = None
phone = None
password = None

users_entry: UserDetails= {
    "name" : username, 
    "email" : email, 
    "phone" : phone, 
    "password" : password
    }

def user_detail(users_entry: UserDetails):
    return users_entry


class NewUserDetails(BaseModel):
    
    username: str
    email: EmailStr
    phone: int
    password: str

def user_detail(users_entry: NewUserDetails):
    return users_entry.password