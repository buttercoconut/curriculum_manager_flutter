from sqlalchemy.orm import Session
from ..models.student import Student
from ..schemas.student import StudentCreate, StudentUpdate

class StudentService:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: StudentCreate) -> Student:
        stu = Student(**data.dict())
        self.db.add(stu)
        self.db.commit()
        self.db.refresh(stu)
        return stu

    def list_all(self):
        return self.db.query(Student).all()

    def get(self, student_id: int) -> Student:
        stu = self.db.query(Student).filter(Student.id == student_id).first()
        if not stu:
            raise Exception("Student not found")
        return stu

    def update(self, student_id: int, data: StudentUpdate) -> Student:
        stu = self.get(student_id)
        for key, value in data.dict(exclude_unset=True).items():
            setattr(stu, key, value)
        self.db.commit()
        self.db.refresh(stu)
        return stu

    def delete(self, student_id: int):
        stu = self.get(student_id)
        self.db.delete(stu)
        self.db.commit()
