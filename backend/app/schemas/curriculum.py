from pydantic import BaseModel, Field
from typing import List, Optional

class CurriculumBase(BaseModel):
    title: str
    description: Optional[str] = None
    grade_level: int
    subjects: List[str]

class CurriculumCreate(CurriculumBase):
    pass

class CurriculumUpdate(CurriculumBase):
    pass

class CurriculumRead(CurriculumBase):
    id: int

    class Config:
        orm_mode = True
