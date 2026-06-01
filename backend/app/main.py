from fastapi import FastAPI
from .api import curriculum, student, grade

app = FastAPI(title="Curriculum Manager API")

app.include_router(curriculum.router, prefix="/curriculum", tags=["Curriculum"])
app.include_router(student.router, prefix="/student", tags=["Student"])
app.include_router(grade.router, prefix="/grade", tags=["Grade"])

# Health check
@app.get("/health")
async def health_check():
    return {"status": "ok"}
