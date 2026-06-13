from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database setup
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Import models to create tables
from .models import curriculum, student, grade

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

# FastAPI app
app = FastAPI(title="Curriculum Manager API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
from .api import curriculum as curriculum_router
from .api import student as student_router
from .api import grade as grade_router

app.include_router(curriculum_router)
app.include_router(student_router)
app.include_router(grade_router)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to Curriculum Manager API"}
