from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    curriculum_id = Column(Integer, ForeignKey("curriculums.id"))

    curriculum = relationship("Curriculum", back_populates="students")
    grades = relationship("Grade", back_populates="student")
