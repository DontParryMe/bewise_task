from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from helpers import Base
from question_item import QuestionItem


class QuizDatabase:
    def __init__(self, database_url: str):
        self.engine = create_engine(database_url)
        Base.metadata.create_all(bind=self.engine)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def get_session(self):
        return self.SessionLocal()

    def save_question(self, session: Session, question_data: dict) -> QuestionItem:
        question_item = QuestionItem(
            id=question_data["id"],
            answer=question_data["answer"],
            question=question_data["question"],
            created_at=datetime.fromisoformat(question_data["created_at"].replace("Z", "+00:00"))
        )

        session.add(question_item)
        session.commit()
        return question_item

    def check_existing_question(self, session: Session, question_data: dict) -> bool:
        existing_question = session.query(QuestionItem).filter_by(question=question_data["question"]).first()
        return existing_question is not None
