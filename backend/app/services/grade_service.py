"""Service layer for Grade operations."""

from typing import List
from sqlalchemy.orm import Session
from ..models.grade import Grade, GradeCreate, GradeUpdate
from ..models import grade as grade_model

class GradeService:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Grade]:
        return self.db.query(grade_model.Grade).all()

    def get_by_id(self, grade_id: int) -> Grade | None:
        return self.db.query(grade_model.Grade).filter_by(id=grade_id).first()

    def create(self, grade_in: GradeCreate) -> Grade:
        db_grade = grade_model.Grade(**grade_in.dict())
        self.db.add(db_grade)
        self.db.commit()
        self.db.refresh(db_grade)
        return db_grade

    def update(self, grade_id: int, grade_in: GradeUpdate) -> Grade | None:
        db_grade = self.get_by_id(grade_id)
        if not db_grade:
            return None
        for field, value in grade_in.dict(exclude_unset=True).items():
            setattr(db_grade, field, value)
        self.db.commit()
        self.db.refresh(db_grade)
        return db_grade

    def delete(self, grade_id: int) -> bool:
        db_grade = self.get_by_id(grade_id)
        if not db_grade:
            return False
        self.db.delete(db_grade)
        self.db.commit()
        return True
