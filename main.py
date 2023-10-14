import os

from dotenv import load_dotenv
from fastapi import FastAPI
from typing import List
from helpers import get_random_questions_from_api
from question_item_response import QuestionItemResponse
from questions_request import QuestionsRequest
from quiz_database import QuizDatabase


app = FastAPI()
load_dotenv()
postgres_user = os.getenv("POSTGRES_USER")
postgres_password = os.getenv("POSTGRES_PASSWORD")
postgres_db = os.getenv("POSTGRES_DB")
connection_string = f"postgresql://{postgres_user}:{postgres_password}@localhost/{postgres_db}"
db = QuizDatabase(connection_string)


@app.post("/quiz/", response_model=List[QuestionItemResponse])
async def get_quiz_questions(request: QuestionsRequest) -> List[QuestionItemResponse]:
    db_session = db.get_session()
    unique_questions = set()

    while len(unique_questions) < request.questions_num:
        api_questions = get_random_questions_from_api(request.questions_num - len(unique_questions))
        for question_data in api_questions:
            existing_question = db.check_existing_question(db_session, question_data)
            if not existing_question:
                question_item = db.save_question(db_session, question_data)
                question_response = QuestionItemResponse(
                    id=question_item.id,
                    answer=question_item.answer,
                    question=question_item.question,
                    created_at=question_item.created_at
                )
                unique_questions.add(question_response)

        if len(unique_questions) < request.questions_num:
            continue
        break

    db_session.close()
    return list(unique_questions)


