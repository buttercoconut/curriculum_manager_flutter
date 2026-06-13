"""Service layer for Curriculum operations."""

from typing import List
from sqlalchemy.orm import Session
from ..models.curriculum import Curriculum, CurriculumCreate, CurriculumUpdate
from ..models import curriculum as curriculum_model

class CurriculumService:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Curriculum]:
        return self.db.query(curriculum_model.Curriculum).all()

    def get_by_id(self, curriculum_id: int) -> Curriculum | None:
        return self.db.query(curriculum_model.Curriculum).filter_by(id=curriculum_id).first()

    def create(self, curriculum_in: CurriculumCreate) -> Curriculum:
        db_curriculum = curriculum_model.Curriculum(**curriculum_in.dict())
        self.db.add(db_curriculum)
        self.db.commit()
        self.db.refresh(db_curriculum)
        return db_curriculum

    def update(self, curriculum_id: int, curriculum_in: CurriculumUpdate) -> Curriculum | None:
        db_curriculum = self.get_by_id(curriculum_id)
        if not db_curriculum:
            return None
        for field, value in curriculum_in.dict(exclude_unset=True).items():
            setattr(db_curriculum, field, value)
        self.db.commit()
        self.db.refresh(db_curriculum)
        return db_curriculum

    def delete(self, curriculum_id: int) -> bool:
        db_curriculum = self.get_by_id(curriculum_id)
        if not db_curriculum:
            return False
        self.db.delete(db_curriculum)
        self.db.commit()
        return True
