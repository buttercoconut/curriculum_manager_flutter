from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.student import Student as StudentModel
from ..services.student_service import StudentService
from ..schemas.student import StudentCreate, StudentRead, StudentUpdate

router = APIRouter()

@router.post("/", response_model=StudentRead, status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    service = StudentService(db)
    return service.create(student)

@router.get("/", response_model=list[StudentRead])
def list_students(db: Session = Depends(get_db)):
    service = StudentService(db)
    return service.list_all()

@router.get("/{student_id}", response_model=StudentRead)
def get_student(student_id: int, db: Session = Depends(get_db)):
    service = StudentService(db)
    return service.get(student_id)

@router.put("/{student_id}", response_model=StudentRead)
def update_student(student_id: int, student: StudentUpdate, db: Session = Depends(get_db)):
    service = StudentService(db)
    return service.update(student_id, student)

@router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    service = StudentService(db)
    service.delete(student_id)
    return None
