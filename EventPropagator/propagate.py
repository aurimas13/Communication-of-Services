#!/usr/bin/env python
# Program to run INFINITELY
import json
import ast
import random
import requests
import threading
import sys
from config import WAIT_SECONDS, INPUT_FILE_LOCATION, ENDPOINT


def send_events():
    with open(INPUT_FILE_LOCATION) as f:
        data = ast.literal_eval(f.read())
        random_data = json.dumps(random.choice(data))
        response = requests.post(url=ENDPOINT, data=random_data)
        print(response.text)
    threading.Timer(int(WAIT_SECONDS), send_events).start()


# send_events()
if __name__ == '__main__':
    try:
        send_events()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)