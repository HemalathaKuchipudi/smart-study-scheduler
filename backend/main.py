import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine
from models import StudyLog
from schemas import StudyLogCreate
from crud import create_study_log

# Create DB tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Enable CORS so frontend can talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Home route (just for testing)
@app.get("/")
def read_root():
    return {"message": "Hello"}

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST /studylogs/
@app.post("/studylogs/", response_model=schemas.StudyLogResponse)
def create_study_log(log: schemas.StudyLogCreate, db: Session = Depends(get_db)):
    return crud.create_study_log(db, log)

# GET /studylogs/
@app.get("/studylogs/", response_model=list[schemas.StudyLogResponse])
def get_all_logs(db: Session = Depends(get_db)):
    return crud.get_study_logs(db)
