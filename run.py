from app.model.functions import predict_pipeline
from schedule import every, repeat, run_pending
import requests
import time

@repeat(every(1).minutes)
def post():
    na = True
    request = requests.post("http://127.0.0.1:8000/data/", data=predict_pipeline())
    if request.status_code != 200:
        na = False
    return request, request.json(), na

_, _, na = post()

while na == True:
    run_pending()
    time.sleep(1)