import hashlib
from datetime import date, datetime
import sqlalchemy
from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
import logging
import collections

log = logging.getLogger("uvicorn")
log.setLevel(logging.DEBUG)


async def create_user_data(db: Session, data: schemas.UserDataCreate):
    try:
        db_data = models.UserData(group_level=data.group_level, username=data.username,
                                    password=hashlib.md5(data.password.encode('utf-8')).hexdigest(),
                                    create_date=data.create_date, user_status=data.user_status,
                                    password_attempt=data.password_attempt, department=data.department,
                                    new_user=data.new_user)

        db.add(db_data)
        db.commit()
        db.refresh(db_data)
        return db_data
    except Exception as e:
        print(e)


# ..........................................................................................
async def create_duplicate_password(db: Session, data: schemas.DuplicatePasswordCreate):
    try:
        db_data = models.DuplicatePassword(username=data.username,
                                             password=hashlib.md5(data.password.encode('utf-8')).hexdigest(),
                                             create_date=data.create_date)
        db.add(db_data)
        db.commit()
        db.refresh(db_data)
        return db_data
    except Exception as e:
        print(e)

# .........................................................................................
