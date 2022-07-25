#!/usr/bin/env python


# Program to run INFINITELY
import json
import ast
import random
import requests
import time, threading
import sys
from config import WAIT_SECONDS, INPUT_FILE_LOCATION, ENDPOINT


def send_events():
    with open(INPUT_FILE_LOCATION) as f:
        data = ast.literal_eval(f.read())
        l = json.dumps(random.choice(data))
        r = requests.post(url=ENDPOINT, data=l)
        print(r.text)
    threading.Timer(int(WAIT_SECONDS), send_events).start()


# send_events()
if __name__ == '__main__':
    input = sys.argv[1]
    if input == '0':
        send_events()
    else:
        sys.exit()