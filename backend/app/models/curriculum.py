from sqlalchemy import Column, Integer, String, Text, JSON, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Curriculum(Base):
    __tablename__ = "curriculums"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    grade_level = Column(Integer, nullable=False)
    subjects = Column(JSON, nullable=False)

    students = relationship("Student", back_populates="curriculum")
    teachers = relationship("Teacher", back_populates="curriculum")
