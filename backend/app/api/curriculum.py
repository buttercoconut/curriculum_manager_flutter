"""FastAPI router for Curriculum endpoints."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..models.curriculum import Curriculum, CurriculumCreate, CurriculumUpdate
from ..services.curriculum_service import CurriculumService
from ..database import get_db

router = APIRouter(prefix="/curriculums", tags=["curriculums"])

@router.get("/", response_model=List[Curriculum])
async def read_curriculums(db: Session = Depends(get_db)):
    service = CurriculumService(db)
    return service.get_all()

@router.get("/{curriculum_id}", response_model=Curriculum)
async def read_curriculum(curriculum_id: int, db: Session = Depends(get_db)):
    service = CurriculumService(db)
    curriculum = service.get_by_id(curriculum_id)
    if not curriculum:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curriculum not found")
    return curriculum

@router.post("/", response_model=Curriculum, status_code=status.HTTP_201_CREATED)
async def create_curriculum(curriculum_in: CurriculumCreate, db: Session = Depends(get_db)):
    service = CurriculumService(db)
    return service.create(curriculum_in)

@router.put("/{curriculum_id}", response_model=Curriculum)
async def update_curriculum(curriculum_id: int, curriculum_in: CurriculumUpdate, db: Session = Depends(get_db)):
    service = CurriculumService(db)
    updated = service.update(curriculum_id, curriculum_in)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curriculum not found")
    return updated

@router.delete("/{curriculum_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_curriculum(curriculum_id: int, db: Session = Depends(get_db)):
    service = CurriculumService(db)
    success = service.delete(curriculum_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curriculum not found")
    return None
