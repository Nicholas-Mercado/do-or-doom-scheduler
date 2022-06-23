from urllib import response
from schedule import every, repeat, run_pending
import time
import requests
import datetime

print("hello! form Cron!")
# @repeat(every(1).seconds)
def job():
    print("this is job")
    response = requests.get("https://do-or-doom-api.herokuapp.com/api/v1/tasks/")
    data = response.json()
    print(data)

    for x in range(len(data)):
        if data[x].get("completed")is False:
            datetime_object = datetime.strptime
            if datetime.now() > data[x].get("due"):

                print("overdue task found")
job()
while True:
    run_pending()
    time.sleep(1)


# [{'id': 15, 'title': 'change 15', 'description': 'plase help', 'completed': False, 'due': '2220-05-21T00:00:00Z', 'created_at'
#  => => # : '2022-06-22T21:35:51.782434Z', 'updated_at': '2022-06-23T00:29:00.601553Z', 'owner': 1}, {'id': 12, 'title': 'test', 'descri
#  => => # ption': '', 'completed': True, 'due': '2220-05-21T00:00:00Z', 'created_at': '2022-06-22T18:24:49.828285Z', 'updated_at': '2022
#  => => # -06-23T00:29:09.470164Z', 'owner': 1}]
