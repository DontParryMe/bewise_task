from pydantic import BaseModel


class QuestionsRequest(BaseModel):
    questions_num: int
