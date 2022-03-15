from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from models.database import Base


class Feedback(Base):
    __tablename__ = "feedbacks"

    id = Column(Integer, primary_key=True, index=True)
    department = Column(String)
    satisfaction = Column(String)
    reportType = Column(String)
    frequency = Column(String)
    comments = Column(String)
    

