from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Curriculum(Base):
    __tablename__ = "curriculums"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    grade_level = Column(Integer, nullable=False)
    subjects = Column(String)  # comma separated

    students = relationship("Student", back_populates="curriculum")

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String, unique=True, index=True)
    name = Column(String, nullable=False)
    grade = Column(Integer)
    class_name = Column(String)
    curriculum_id = Column(Integer, ForeignKey("curriculums.id"))

    curriculum = relationship("Curriculum", back_populates="students")
    grades = relationship("Grade", back_populates="student")

class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    subject = Column(String, nullable=False)
    score = Column(Float)

    student = relationship("Student", back_populates="grades")
