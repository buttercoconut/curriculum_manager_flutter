"""
Curriculum model.
"""
from sqlalchemy import Column, Integer, String, JSON
from .base import Base

class Curriculum(Base):
    __tablename__ = "curriculums"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    grade_level = Column(Integer, nullable=False)
    subjects = Column(JSON, nullable=False)  # list of subject names
