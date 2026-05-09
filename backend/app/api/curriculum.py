"""
API router for Curriculum.
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import async_session
from ..services.curriculum_service import CurriculumService
from ..schemas.curriculum import CurriculumCreate, CurriculumUpdate, Curriculum

router = APIRouter()

async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session

@router.get("/", response_model=list[Curriculum])
async def read_curriculums(db: AsyncSession = Depends(get_db)):
    service = CurriculumService(db)
    return await service.get_all()

@router.get("/{curriculum_id}", response_model=Curriculum)
async def read_curriculum(curriculum_id: int, db: AsyncSession = Depends(get_db)):
    service = CurriculumService(db)
    try:
        return await service.get(curriculum_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curriculum not found")

@router.post("/", response_model=Curriculum, status_code=status.HTTP_201_CREATED)
async def create_curriculum(payload: CurriculumCreate, db: AsyncSession = Depends(get_db)):
    service = CurriculumService(db)
    return await service.create(payload)

@router.put("/{curriculum_id}", response_model=Curriculum)
async def update_curriculum(curriculum_id: int, payload: CurriculumUpdate, db: AsyncSession = Depends(get_db)):
    service = CurriculumService(db)
    try:
        return await service.update(curriculum_id, payload)
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curriculum not found")

@router.delete("/{curriculum_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_curriculum(curriculum_id: int, db: AsyncSession = Depends(get_db)):
    service = CurriculumService(db)
    try:
        await service.delete(curriculum_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curriculum not found")
