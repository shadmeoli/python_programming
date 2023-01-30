# schema library
from dataclasses import dataclass

@dataclass
class UserRegistration:

    name: str
    email: str
    password: str
    confirm_password: str


    @classmethod
    def passwords_check(cls, value):
        pass


class Account:

    def registration(self, user_entry: UserRegistration):

        pass