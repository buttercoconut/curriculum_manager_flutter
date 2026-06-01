from pydantic import BaseModel
from typing import Optional

class GradeBase(BaseModel):
    student_id: int
    subject: str
    score: float
    comments: Optional[str] = None

class GradeCreate(GradeBase):
    pass

class GradeUpdate(GradeBase):
    pass

class GradeRead(GradeBase):
    id: int

    class Config:
        orm_mode = True
