"""
Student model.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    grade = Column(Integer, nullable=False)
    class_name = Column(String, nullable=False)
    # relationships
    grades = relationship("Grade", back_populates="student")
