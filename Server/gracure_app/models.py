from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, DateTime, Float, UniqueConstraint
from sqlalchemy.orm import relationship

from .database import Base


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
