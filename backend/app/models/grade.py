"""Pydantic models for Grade entity."""

from pydantic import BaseModel, Field
from typing import Optional

class GradeBase(BaseModel):
    student_id: int = Field(..., example=1)
    curriculum_id: int = Field(..., example=1)
    subject: str = Field(..., example="Algebra")
    score: float = Field(..., example=85.5)

class GradeCreate(GradeBase):
    pass

class GradeUpdate(BaseModel):
    score: Optional[float] = None

class Grade(GradeBase):
    id: int

    class Config:
        orm_mode = True
