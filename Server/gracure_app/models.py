from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, DateTime, Float, UniqueConstraint
from sqlalchemy.orm import relationship

from .database import Base


class SecurityPolicy(Base):
    __tablename__ = "security_policy"

    id = Column(Integer, index=True, primary_key=True)
    security_id = Column(Integer)
    min_pass_length = Column(Integer)
    pass_expiry_days = Column(Integer)
    prompt_user_days = Column(Integer)
    lock_in_attempt = Column(Integer)
    pass_dup_count = Column(Integer)
    auto_log_duration = Column(Integer)
    upper_case = Column(Boolean)
    lower_case = Column(Boolean)
    numeric_num = Column(Boolean)
    symbol = Column(Boolean)


class UserData(Base):
    __tablename__ = "user_data"

    id = Column(Integer, primary_key=True, index=True)
    group_level = Column(String)
    username = Column(String, unique=True)
    password = Column(String)
    create_date = Column(DateTime)
    user_status = Column(String)
    password_attempt = Column(Integer)
    department = Column(String)
    new_user = Column(Boolean)


class DuplicatePassword(Base):
    __tablename__ = "duplicate_password"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    create_date = Column(DateTime)


class AuditReport(Base):
    __tablename__ = "audit_report"

    id = Column(Integer, primary_key=True, index=True)
    act_time = Column(DateTime)
    parameter = Column(String)
    old_value = Column(String)
    new_value = Column(String)
    user_ = Column(String)


class AccessRights(Base):
    __tablename__ = "access_rights"

    id = Column(Integer, primary_key=True, index=True)
    parameter = Column(String)
    manager = Column(Boolean)
    supervisor = Column(Boolean)
    operator = Column(Boolean)


class LoginData(Base):
    __tablename__ = "login_data"

    id = Column(Integer, primary_key=True, index=True)
    date_ = Column(Date)
    username = Column(String)
    login_time = Column(DateTime)
    logout_time = Column(DateTime, nullable=True)
