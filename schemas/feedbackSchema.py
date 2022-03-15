from typing import Optional
from pydantic import BaseModel

#create pydantic models that have common attributes

class FeedbackBase(BaseModel):
    #id:int
    department:str
    satisfaction:str
    reportType:str
    frequency:str
    comments:str

    #pydantic model used to read or return data to API
class FeedbackCreate(FeedbackBase):
    pass
class Feedback(FeedbackBase):
     id:int   

     class Config:
        orm_model = True

        #allows the app to take ORM objects and translate them into responses automatically.
