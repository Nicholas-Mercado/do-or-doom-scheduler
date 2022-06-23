# from urllib import response
from schedule import every, repeat, run_pending
import time
import requests
import datetime

data = [{'id': 15, 'title': 'change 15', 'description': 'plase help', 'completed': False, 'due': '1220-05-21T00:00:00Z', 'created_at': '2022-06-22T21:35:51.782434Z', 'updated_at': '2022-06-23T00:29:00.601553Z', 'owner': 1}, {'id': 12, 'title': 'test', 'description': '', 'completed': True, 'due': '2220-05-21T00:00:00Z', 'created_at': '2022-06-22T18:24:49.828285Z', 'updated_at': '2022-06-23T00:29:09.470164Z', 'owner': 1}]

# @repeat(every(1).seconds)
def job(data):
    print("this is job")
    # response = requests.get("https://do-or-doom-api.herokuapp.com/api/v1/tasks/")
    # data = response.json()
    current_datetime = datetime.datetime.now()
    print("current time--->",current_datetime)
    for x in range(len(data)):
        if data[x].get("completed")is False:
            datetime_object = datetime.datetime.strptime(data[x].get("due"), "%Y-%m-%dT%H:%M:%SZ" )
            # print("current_datetime --->", current_datetime)
            # print("datetime_object --->", datetime_object)
            if current_datetime > datetime_object:
                print("woopsiedoodle")
job(data)



# while True:
#     run_pending()
#     time.sleep(1)



