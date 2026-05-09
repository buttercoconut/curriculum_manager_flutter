"""
Pydantic schemas for Curriculum.
"""
from typing import List, Optional
from pydantic import BaseModel

class CurriculumBase(BaseModel):
    title: str
    description: Optional[str] = None
    grade_level: int
    subjects: List[str]

class CurriculumCreate(CurriculumBase):
    pass

class CurriculumUpdate(CurriculumBase):
    pass

class Curriculum(CurriculumBase):
    id: int

    class Config:
        orm_mode = True
