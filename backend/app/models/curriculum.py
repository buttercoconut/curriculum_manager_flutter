"""Pydantic models for Curriculum entity."""

from pydantic import BaseModel, Field
from typing import List

class CurriculumBase(BaseModel):
    title: str = Field(..., example="Mathematics 10th Grade")
    description: str | None = Field(None, example="Basic algebra and geometry")
    grade_level: int = Field(..., example=10)
    subjects: List[str] = Field(..., example=["Algebra", "Geometry", "Trigonometry"])

class CurriculumCreate(CurriculumBase):
    pass

class CurriculumUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    grade_level: int | None = None
    subjects: List[str] | None = None

class Curriculum(CurriculumBase):
    id: int

    class Config:
        orm_mode = True
