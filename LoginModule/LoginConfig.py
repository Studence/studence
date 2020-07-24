from enum import Enum


class LoginConfig(Enum):
    MILLISECONDS = 'Milliseconds'
    USER_ID = 'UserId'
    USER_TYPE = 'UserType'
    USER_EMAIL = 'UserEmail'
    USER_PASSWORD = "UserPassword"

    @staticmethod
    def list():
        return list(map(lambda c: c.value, LoginConfig))
