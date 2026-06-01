from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Grade(Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    subject = Column(String(255), nullable=False)
    score = Column(Float, nullable=False)
    comments = Column(String(255), nullable=True)

    student = relationship("Student", back_populates="grades")
