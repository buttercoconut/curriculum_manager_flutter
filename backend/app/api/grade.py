from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.grade import Grade as GradeModel
from ..services.grade_service import GradeService
from ..schemas.grade import GradeCreate, GradeRead, GradeUpdate

router = APIRouter()

@router.post("/", response_model=GradeRead, status_code=status.HTTP_201_CREATED)
def create_grade(grade: GradeCreate, db: Session = Depends(get_db)):
    service = GradeService(db)
    return service.create(grade)

@router.get("/", response_model=list[GradeRead])
def list_grades(db: Session = Depends(get_db)):
    service = GradeService(db)
    return service.list_all()

@router.get("/{grade_id}", response_model=GradeRead)
def get_grade(grade_id: int, db: Session = Depends(get_db)):
    service = GradeService(db)
    return service.get(grade_id)

@router.put("/{grade_id}", response_model=GradeRead)
def update_grade(grade_id: int, grade: GradeUpdate, db: Session = Depends(get_db)):
    service = GradeService(db)
    return service.update(grade_id, grade)

@router.delete("/{grade_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_grade(grade_id: int, db: Session = Depends(get_db)):
    service = GradeService(db)
    service.delete(grade_id)
    return None
