"""FastAPI router for Student endpoints."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..models.student import Student, StudentCreate, StudentUpdate
from ..services.student_service import StudentService
from ..database import get_db

router = APIRouter(prefix="/students", tags=["students"])

@router.get("/", response_model=List[Student])
async def read_students(db: Session = Depends(get_db)):
    service = StudentService(db)
    return service.get_all()

@router.get("/{student_id}", response_model=Student)
async def read_student(student_id: int, db: Session = Depends(get_db)):
    service = StudentService(db)
    student = service.get_by_id(student_id)
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return student

@router.post("/", response_model=Student, status_code=status.HTTP_201_CREATED)
async def create_student(student_in: StudentCreate, db: Session = Depends(get_db)):
    service = StudentService(db)
    return service.create(student_in)

@router.put("/{student_id}", response_model=Student)
async def update_student(student_id: int, student_in: StudentUpdate, db: Session = Depends(get_db)):
    service = StudentService(db)
    updated = service.update(student_id, student_in)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return updated

@router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_student(student_id: int, db: Session = Depends(get_db)):
    service = StudentService(db)
    success = service.delete(student_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return None
