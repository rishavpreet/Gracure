from datetime import date, datetime
import sqlalchemy
from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
import logging
import collections

log = logging.getLogger("uvicorn")
log.setLevel(logging.DEBUG)