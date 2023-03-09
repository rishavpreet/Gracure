from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel


class SecurityPolicyBase(BaseModel):
    security_id: int
    min_pass_length: int
    pass_expiry_days: int
    prompt_user_days: int
    lock_in_attempt: int
    pass_dup_count: int
    auto_log_duration: int
    upper_case: bool
    lower_case: bool
    numeric_num: bool
    symbol: bool


class SecurityPolicyCreate(SecurityPolicyBase):
    pass


# class SecurityPolicyUpadate(BaseModel):
#     SecurityId: int


class SecurityPolicy(SecurityPolicyBase):
    SecurityId: int

    class Config:
        orm_mode = True


# ......................................................................................................................

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


# ....................................................................................................................
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


# .........................................................................................................................
class AuditReportBase(BaseModel):
    act_time: str
    parameter: str
    old_value: str
    new_value: str
    user_: str


class AuditReportCreate(AuditReportBase):
    pass


class AuditReport(AuditReportBase):
    pass

    class Config:
        orm_mode = True
