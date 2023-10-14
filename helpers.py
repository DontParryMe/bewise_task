import requests
from sqlalchemy.orm import declarative_base


Base = declarative_base()


def get_random_questions_from_api(count: int):
    response = requests.get(f"https://jservice.io/api/random?count={count}")
    return response.json()