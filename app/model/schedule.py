from functions import to_json
import requests

def post():
    data = to_json()
    request = requests.post("http://127.0.0.1:8000/data/", data=data)
    return request, request.json()

post()