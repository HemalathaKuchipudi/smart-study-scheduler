from sqlalchemy.orm import Session
from models import StudyLog
from schemas import StudyLogCreate
from spaced_repetition import calculate_next_review_date

def create_study_log(db: Session, log: StudyLogCreate):
    next_review = calculate_next_review_date(log.date_studied)
    new_log = StudyLog(
        topic=log.topic,
        date_studied=log.date_studied,
        next_review_date=next_review
    )
    db.add(new_log)
    db.commit()
    db.refresh(new_log)
    return new_log

def get_study_logs(db: Session):
    return db.query(StudyLog).all()
