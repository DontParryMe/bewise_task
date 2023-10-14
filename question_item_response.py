from datetime import datetime
from pydantic import BaseModel


class QuestionItemResponse(BaseModel):
    id: int
    answer: str
    question: str
    created_at: datetime

    def __eq__(self, other):
        if not isinstance(other, QuestionItemResponse):
            return False
        return (
                self.id == other.id and
                self.answer == other.answer and
                self.question == other.question and
                self.created_at == other.created_at
        )

    def __hash__(self):
        return hash((self.id, self.answer, self.question, self.created_at))
