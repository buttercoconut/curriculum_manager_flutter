"""Service layer for Student operations."""

from typing import List
from sqlalchemy.orm import Session
from ..models.student import Student, StudentCreate, StudentUpdate
from ..models import student as student_model

class StudentService:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Student]:
        return self.db.query(student_model.Student).all()

    def get_by_id(self, student_id: int) -> Student | None:
        return self.db.query(student_model.Student).filter_by(id=student_id).first()

    def create(self, student_in: StudentCreate) -> Student:
        db_student = student_model.Student(**student_in.dict())
        self.db.add(db_student)
        self.db.commit()
        self.db.refresh(db_student)
        return db_student

    def update(self, student_id: int, student_in: StudentUpdate) -> Student | None:
        db_student = self.get_by_id(student_id)
        if not db_student:
            return None
        for field, value in student_in.dict(exclude_unset=True).items():
            setattr(db_student, field, value)
        self.db.commit()
        self.db.refresh(db_student)
        return db_student

    def delete(self, student_id: int) -> bool:
        db_student = self.get_by_id(student_id)
        if not db_student:
            return False
        self.db.delete(db_student)
        self.db.commit()
        return True
