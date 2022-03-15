from sqlalchemy.orm import Session

#import models, schemas
from schemas import feedbackSchema as fbs
from models import feedbackModel as fbm




def get_feedbacks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(fbm.Feedback).offset(skip).limit(limit).all()


def create_feedback(db: Session, feedback: fbs.FeedbackCreate):

    db_item = fbm.Feedback(department=feedback.department,
                              satisfaction=feedback.satisfaction,
                              frequency=feedback.frequency,
                              reportType=feedback.reportType,
                              comments=feedback.comments)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete(db: Session,id:int):
        db_feedback= db.query(fbm.Feedback).filter_by(id=id).first()
        db.delete(db_feedback)
        db.commit()
        
        
def update(db: Session,store_data):
        db.merge(store_data)
        db.commit()  

def get_feedback_by_id(db: Session, id: int):
    return db.query(fbm.Feedback).filter(fbm.Feedback.id == id).first()

'''
def update_feed(id: int,comments:str,db: Session):
    db_item = get_feedback_by_id(db, id)
    db_item.comments = comments  
'''

def update(db: Session,id:int,feedback:fbs.Feedback):
        db_item = get_feedback_by_id(db, id)
        if db_item is None:
                print('Not found')
        db_item.comments = feedback.comments 
        db.commit()
        db.refresh(db_item)  
        return db_item        


          

    
