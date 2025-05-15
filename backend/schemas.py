from pydantic import BaseModel
from datetime import date

class StudyLogCreate(BaseModel):
    topic: str
    date_studied: date

class StudyLogResponse(BaseModel):
    id: int
    topic: str
    date_studied: date
    next_review_date: date

    class Config:
        orm_mode = True
