from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models.base import Base

DATABASE_URL = "postgresql+psycopg2://user:password@localhost:5432/curriculum_db"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
Base.metadata.create_all(bind=engine)

# Dependency
from fastapi import Depends

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
