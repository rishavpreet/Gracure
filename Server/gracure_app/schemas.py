from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel


class UserDataBase(BaseModel):
    group_level: str
    username: str
    password: str
    create_date: datetime
    user_status: str
    password_attempt: int
    department: str
    new_user: bool


class UserDataCreate(UserDataBase):
    pass


class UserData(UserDataBase):
    pass

    class Config:
        orm_mode = True


# .......................................................................................
class DuplicatePasswordBase(BaseModel):
    username: str
    password: str
    create_date: datetime


class DuplicatePasswordCreate(DuplicatePasswordBase):
    pass


class DuplicatePassword(DuplicatePasswordBase):
    pass

    class Config:
        orm_mode = True
