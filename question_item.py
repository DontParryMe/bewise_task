from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from helpers import Base


class QuestionItem(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    answer = Column(String, index=True)
    question = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)