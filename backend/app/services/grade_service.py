from sqlalchemy.orm import Session
from ..models.grade import Grade
from ..schemas.grade import GradeCreate, GradeUpdate

class GradeService:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: GradeCreate) -> Grade:
        grd = Grade(**data.dict())
        self.db.add(grd)
        self.db.commit()
        self.db.refresh(grd)
        return grd

    def list_all(self):
        return self.db.query(Grade).all()

    def get(self, grade_id: int) -> Grade:
        grd = self.db.query(Grade).filter(Grade.id == grade_id).first()
        if not grd:
            raise Exception("Grade not found")
        return grd

    def update(self, grade_id: int, data: GradeUpdate) -> Grade:
        grd = self.get(grade_id)
        for key, value in data.dict(exclude_unset=True).items():
            setattr(grd, key, value)
        self.db.commit()
        self.db.refresh(grd)
        return grd

    def delete(self, grade_id: int):
        grd = self.get(grade_id)
        self.db.delete(grd)
        self.db.commit()
