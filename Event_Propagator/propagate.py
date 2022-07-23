#!/usr/bin/env python

# Python program INFINITELY
import json
import ast
import random
import requests
import time, threading
import sys
from config import WAIT_SECONDS, INPUT_FILE_LOCATION, ENDPOINT

# Defining headers
# headers = {
#     "Content-Type" : "text/plain",
#     "Content-Length" : "0"
# }

# Delete on ocassion:
print(WAIT_SECONDS)

def send_events():
    with open(INPUT_FILE_LOCATION) as f:
        data = ast.literal_eval(f.read())
        l = json.dumps(random.choice(data))
        r = requests.post(url=ENDPOINT, data=l)
        print(r.status_code, r.text)
    threading.Timer(int(WAIT_SECONDS), send_events).start()

if __name__ == '__main__':
    input = sys.argv[1]
    if input == '0':
        send_events()
    else:
        sys.exit()


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
