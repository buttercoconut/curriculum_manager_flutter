"""Pydantic models for Student entity."""

from pydantic import BaseModel, Field
from typing import Optional

class StudentBase(BaseModel):
    student_id: str = Field(..., example="S12345")
    name: str = Field(..., example="홍길동")
    grade: int = Field(..., example=10)
    class_name: str = Field(..., example="1반")

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    grade: Optional[int] = None
    class_name: Optional[str] = None

class Student(StudentBase):
    id: int

    class Config:
        orm_mode = True
