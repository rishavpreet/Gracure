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


async def create_security_policy(db: Session, sp_data: schemas.SecurityPolicyCreate):
    try:
        db_sp = models.SecurityPolicy(security_id=sp_data.security_id, min_pass_length=sp_data.min_pass_length,
                                      pass_expiry_days=sp_data.pass_expiry_days,
                                      prompt_user_days=sp_data.prompt_user_days,
                                      lock_in_attempt=sp_data.lock_in_attempt, pass_dup_count=sp_data.pass_dup_count,
                                      auto_log_duration=sp_data.auto_log_duration, upper_case=sp_data.upper_case,
                                      lower_case=sp_data.lower_case, numeric_num=sp_data.numeric_num,
                                      symbol=sp_data.symbol)

        db.add(db_sp)
        db.commit()
        db.refresh(db_sp)
        return db_sp

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")


# ....................................................................................................................
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


# ......................................................................................................................
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


# .....................................................................................................................
async def create_audit_report(db: Session, ar_data: schemas.AuditReportCreate):
    try:
        db_ar = models.AuditReport(act_time=ar_data.act_time, parameter=ar_data.parameter,
                                   old_value=ar_data.old_value, new_value=ar_data.old_value,
                                   user_=ar_data.user_)

        db.add(db_ar)
        db.commit()
        db.refresh(db_ar)
        return db_ar

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")


# ......................................................................................................................

async def create_access_rights(db: Session, ar_data: schemas.AccessRightsCreate):
    try:
        db_ar = models.AccessRights(parameter=ar_data.parameter,
                                    manager=ar_data.manager, supervisor=ar_data.supervisor,
                                    operator=ar_data.operator)

        db.add(db_ar)
        db.commit()
        db.refresh(db_ar)
        return db_ar

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")


# .....................................................................................................................

async def get_login_data_by_name(db: Session, username: str):
    try:
        return db.query(models.LoginData).filter(models.LoginData.username == username,
                                                 models.LoginData.logout_time.is_(None)).first()

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{e}")


async def create_login_data(db: Session, log_data: schemas.LoginDataBase):
    try:
        db_logged_in = await get_login_data_by_name(db, log_data.username)
        if not db_logged_in:
            db_master = models.LoginData(date_=log_data.date_, username=log_data.username,
                                         login_time=log_data.login_time)

            db.add(db_master)
            db.commit()
            db.refresh(db_master)
            return db_master
        else:
            return db_logged_in

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{e}")

async def update_login_data(db: Session, data: schemas.LoginDataUpdate):
    try:
        login_data_db = await get_login_data_by_name(db, data.username)
        mo_id = login_data_db.id
        db_mo = db.get(models.LoginData, mo_id)
        for key, value in data.dict(exclude_unset=True).items():
            setattr(db_mo, key, value)
        db.add(db_mo)
        db.commit()
        db.refresh(db_mo)
        return db_mo
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
