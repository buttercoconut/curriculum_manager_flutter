from pydantic import BaseModel, Field
from typing import Optional

class StudentBase(BaseModel):
    name: str
    email: str
    curriculum_id: Optional[int] = None

class StudentCreate(StudentBase):
    pass

class StudentUpdate(StudentBase):
    pass

class StudentRead(StudentBase):
    id: int

    class Config:
        orm_mode = True
