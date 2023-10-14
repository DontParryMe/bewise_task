import requests

json = {
    "questions_num": 10
}

response = requests.post("http://localhost:8000/quiz/", json=json)
print(response.json())
