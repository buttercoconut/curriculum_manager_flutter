"""FastAPI application entry point."""

from fastapi import FastAPI
from .api import curriculum as curriculum_router, student as student_router, grade as grade_router

app = FastAPI(title="Curriculum Manager API")

app.include_router(curriculum_router.router)
app.include_router(student_router.router)
app.include_router(grade_router.router)

# Create tables on startup
@app.on_event("startup")
async def startup_event():
    from .database import Base, engine
    Base.metadata.create_all(bind=engine)
