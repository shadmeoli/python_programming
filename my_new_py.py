'''

    interface Userdata {
        
        }

'''



from dataclasses import dataclass

from pydantic import BaseModel

# class UserData:

#     def __init__(self, username, password):
#         self.username = username
#         self.password = password


#     def __repr__(self) -> str:
#         return {
#             "username" : self.username,
#             "password" : self.password
#                 }

@dataclass
class UserData:

    username: str
    password: str


user_data  = {
    "username": "new_user",
    "password" : "new_pass"
    }

print(user_data)


def foo():
    return 1



def bar() -> int:
    return 1




if __name__ == "__main__":
    print(foo())
    print(bar())
    print(user_data)