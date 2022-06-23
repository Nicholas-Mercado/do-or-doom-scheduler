# from urllib import response
from schedule import every, repeat, run_pending
import time
import requests
import datetime
import os
from twilio.rest import Client
# from dotenv import load_dotenv



set_sleep = 1
@repeat(every(1).seconds)
def job():
    global set_sleep
    response = requests.get("https://do-or-doom-api.herokuapp.com/api/v1/tasks/")
    data = response.json()
    print("Hitting tasks api")
    current_datetime = datetime.datetime.now()
    for x in range(len(data)):

        if data[x].get("completed")is False:

            print("found a task that was not completed")

            datetime_object = datetime.datetime.strptime(data[x].get("due"), "%Y-%m-%dT%H:%M:%SZ" )

            if current_datetime > datetime_object:

                print("task past due! oh NO!!!!!!!!")
                time.sleep(1)
                print("DOOM!")
                set_sleep = 50
                print("sleeping for: ", set_sleep)


                account_sid = os.getenv('TWILIO_ACCOUNT_SID')
                auth_token = os.getenv('TWILIO_AUTH_TOKEN')
                client = Client(account_sid, auth_token)


                message = client.messages.create(
                    messaging_service_sid = os.getenv('MESSAGE_SID'),
                    body='hello again',
                    to=os.getenv('PHONE_NUMBER')
                    )

                print("sent doom msg")

                break
            else:
                print("You've still got time!")
# job(data)



while True:
    run_pending()
    time.sleep(set_sleep)
    print("happening")




