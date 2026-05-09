"""
Service layer for Curriculum.
"""
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound

from ..models.curriculum import Curriculum as CurriculumModel
from ..schemas.curriculum import CurriculumCreate, CurriculumUpdate, Curriculum

class CurriculumService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self) -> List[Curriculum]:
        result = await self.db.execute(select(CurriculumModel))
        return result.scalars().all()

    async def get(self, curriculum_id: int) -> Curriculum:
        result = await self.db.execute(select(CurriculumModel).where(CurriculumModel.id == curriculum_id))
        curriculum = result.scalar_one_or_none()
        if not curriculum:
            raise NoResultFound
        return curriculum

    async def create(self, payload: CurriculumCreate) -> Curriculum:
        new = CurriculumModel(**payload.dict())
        self.db.add(new)
        await self.db.commit()
        await self.db.refresh(new)
        return new

    async def update(self, curriculum_id: int, payload: CurriculumUpdate) -> Curriculum:
        curriculum = await self.get(curriculum_id)
        for key, value in payload.dict(exclude_unset=True).items():
            setattr(curriculum, key, value)
        await self.db.commit()
        await self.db.refresh(curriculum)
        return curriculum

    async def delete(self, curriculum_id: int) -> None:
        curriculum = await self.get(curriculum_id)
        await self.db.delete(curriculum)
        await self.db.commit()
