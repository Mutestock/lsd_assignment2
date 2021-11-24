
from dataclasses import dataclass


@dataclass
class User():
    username: str
    password: str
    is_teacher: bool


class CurrentUser():
    _instance: User = None

    def __init__(self):
        if not self._instance:
            self._instance = User(None, None, None)

    def replace(self, usr: str, pwd: str, is_teacher: bool):
        self._instance = User(usr, pwd, is_teacher)

    def get_username(self):
        return self._instance.username
