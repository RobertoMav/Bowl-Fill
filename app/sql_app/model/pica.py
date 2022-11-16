from functions import to_json
import schedule
import requests
import time

def post():
    data = to_json()
    request = requests.post("http://127.0.0.1:8000/data/", data=data)
    return request, request.json()

post()

# a = to_json()
# print(a)

schedule.every(1).minutes.do(post)


while True:
    schedule.run_pending()
    time.sleep(1)
