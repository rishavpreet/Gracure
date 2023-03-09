from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./cremica_app.db"

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Cybershot#903@localhost/gracure_db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL  # ,{"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


