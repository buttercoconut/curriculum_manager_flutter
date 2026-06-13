"""FastAPI router for Grade endpoints."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..models.grade import Grade, GradeCreate, GradeUpdate
from ..services.grade_service import GradeService
from ..database import get_db

router = APIRouter(prefix="/grades", tags=["grades"])

@router.get("/", response_model=List[Grade])
async def read_grades(db: Session = Depends(get_db)):
    service = GradeService(db)
    return service.get_all()

@router.get("/{grade_id}", response_model=Grade)
async def read_grade(grade_id: int, db: Session = Depends(get_db)):
    service = GradeService(db)
    grade = service.get_by_id(grade_id)
    if not grade:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Grade not found")
    return grade

@router.post("/", response_model=Grade, status_code=status.HTTP_201_CREATED)
async def create_grade(grade_in: GradeCreate, db: Session = Depends(get_db)):
    service = GradeService(db)
    return service.create(grade_in)

@router.put("/{grade_id}", response_model=Grade)
async def update_grade(grade_id: int, grade_in: GradeUpdate, db: Session = Depends(get_db)):
    service = GradeService(db)
    updated = service.update(grade_id, grade_in)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Grade not found")
    return updated

@router.delete("/{grade_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_grade(grade_id: int, db: Session = Depends(get_db)):
    service = GradeService(db)
    success = service.delete(grade_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Grade not found")
    return None
