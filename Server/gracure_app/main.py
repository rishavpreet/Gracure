from datetime import date, timedelta
from fastapi import Depends
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import datetime
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
import logging
from fastapi.responses import FileResponse

log = logging.getLogger("uvicorn")
log.setLevel(logging.DEBUG)

app = FastAPI()

origins = [
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/user_data/")
async def create_user_data(data: schemas.UserDataCreate, db: Session = Depends(get_db)):
    return await crud.create_user_data(db=db, data=data)


# ...................................................................................................

@app.post("/duplicate_password/")
async def create_duplicate_password(data: schemas.DuplicatePasswordCreate, db: Session = Depends(get_db)):
    return await crud.create_duplicate_password(db=db, data=data)
