from sqlalchemy import Column, Integer, String, Date
from database import Base

class StudyLog(Base):
    __tablename__ = "studylogs"

    id = Column(Integer, primary_key=True, index=True)
    topic = Column(String, index=True)
    date_studied = Column(Date)
    next_review_date = Column(Date)
