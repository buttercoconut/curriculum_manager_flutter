from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.curriculum import Curriculum as CurriculumModel
from ..services.curriculum_service import CurriculumService
from ..schemas.curriculum import CurriculumCreate, CurriculumRead, CurriculumUpdate

router = APIRouter()

@router.post("/", response_model=CurriculumRead, status_code=status.HTTP_201_CREATED)
def create_curriculum(curriculum: CurriculumCreate, db: Session = Depends(get_db)):
    service = CurriculumService(db)
    return service.create(curriculum)

@router.get("/", response_model=list[CurriculumRead])
def list_curriculums(db: Session = Depends(get_db)):
    service = CurriculumService(db)
    return service.list_all()

@router.get("/{curriculum_id}", response_model=CurriculumRead)
def get_curriculum(curriculum_id: int, db: Session = Depends(get_db)):
    service = CurriculumService(db)
    return service.get(curriculum_id)

@router.put("/{curriculum_id}", response_model=CurriculumRead)
def update_curriculum(curriculum_id: int, curriculum: CurriculumUpdate, db: Session = Depends(get_db)):
    service = CurriculumService(db)
    return service.update(curriculum_id, curriculum)

@router.delete("/{curriculum_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_curriculum(curriculum_id: int, db: Session = Depends(get_db)):
    service = CurriculumService(db)
    service.delete(curriculum_id)
    return None
