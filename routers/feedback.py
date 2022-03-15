from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
#import crud, models, schemas
from controllers import feedbackController as crud
from models import feedbackModel as models
from schemas import feedbackSchema as schemas

from models.database import SessionLocal, engine

from fastapi import APIRouter

models.Base.metadata.create_all(bind=engine)


router = APIRouter(
    # prefix="/feedbacks",
    # tags=["Feedback"],
    # responses={404: {"description": "Not found"}},
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/feedbacks")
def create_user_feedback(
   feedback: schemas.FeedbackCreate, db: Session = Depends(get_db)
):
    return crud.create_feedback(db=db, feedback=feedback)


@router.get("/feedbacks")
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_feedbacks(db, skip=skip, limit=limit)
    return items

@router.delete('/feedbacks/{id}')
def delete_feedback(id: int,db: Session = Depends(get_db)):
 
    crud.delete(db,id)
    return "Feedback Message deleted successfully!"   

@router.put('/feedbacks/{id}')
def update_feedback(id: int, new_info: schemas.Feedback, db: Session = Depends(get_db)):

   
        db_item = crud.update(db, id, new_info)
        return db_item
  



