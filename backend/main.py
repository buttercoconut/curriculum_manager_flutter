"""
FastAPI application entry point for Curriculum Manager backend.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import curriculum, student, grade

app = FastAPI(title="Curriculum Manager API", version="1.0.0")

# CORS for Flutter mobile app (localhost:3000 for dev)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict to specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(curriculum.router, prefix="/curriculum", tags=["Curriculum"])
app.include_router(student.router, prefix="/student", tags=["Student"])
app.include_router(grade.router, prefix="/grade", tags=["Grade"])

@app.get("/health")
async def health_check():
    return {"status": "ok"}
