# Python program INFINITELY
import json
import ast
import random
import requests
import time
from datetime import datetime, timedelta
from requests.structures import CaseInsensitiveDict
import time, threading

# Defining URL
url="http://127.0.0.1:4444/event"
# Defining headers
headers = {
    "Content-Type" : "text/plain",
    "Content-Length" : "0"
}

WAIT_SECONDS = 5

def send_events():
    with open('events.json') as f:
        data = ast.literal_eval(f.read())
        l = json.dumps(random.choice(data))
        r = requests.post(url, data=l, headers=headers)
        print(r.status_code, r.text)
    threading.Timer(WAIT_SECONDS, foo).start()


send_events()


if __name__ == '__main__':
    arg_path = sys.argv[1]
    if len(sys.argv) < 3:
        input = '0'
    else:
        input = sys.argv[2]

    run(arg_path,input)
# # Opening JSON file
# f = open('events.json')
#
# # Data load
# data = json.load(f)
# # Randomly select
# l = json.dumps(random.choice(data))
# # Sending post request and saving the response as response object
# r = requests.post(url, data=l, headers=headers)
# print(r.status_code, r.text)
#
# f.close()


# while 1:
#     dt = datetime.now() + timedelta(seconds=15)
#     dt = dt.replace(second=5)
#     with open('events.json') as f:
#         data = ast.literal_eval(f.read())
#         l = json.dumps(random.choice(data))
#         r = requests.post(url, data=l, headers=headers)
#         print(r.status_code, r.text)
#     while datetime.now() < dt:
#         time.sleep(1)
