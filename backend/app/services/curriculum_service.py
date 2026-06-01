from sqlalchemy.orm import Session
from ..models.curriculum import Curriculum
from ..schemas.curriculum import CurriculumCreate, CurriculumUpdate

class CurriculumService:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: CurriculumCreate) -> Curriculum:
        curr = Curriculum(**data.dict())
        self.db.add(curr)
        self.db.commit()
        self.db.refresh(curr)
        return curr

    def list_all(self):
        return self.db.query(Curriculum).all()

    def get(self, curriculum_id: int) -> Curriculum:
        curr = self.db.query(Curriculum).filter(Curriculum.id == curriculum_id).first()
        if not curr:
            raise Exception("Curriculum not found")
        return curr

    def update(self, curriculum_id: int, data: CurriculumUpdate) -> Curriculum:
        curr = self.get(curriculum_id)
        for key, value in data.dict(exclude_unset=True).items():
            setattr(curr, key, value)
        self.db.commit()
        self.db.refresh(curr)
        return curr

    def delete(self, curriculum_id: int):
        curr = self.get(curriculum_id)
        self.db.delete(curr)
        self.db.commit()
