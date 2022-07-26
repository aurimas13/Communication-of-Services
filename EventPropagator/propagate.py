#!/usr/bin/env python
# Program to run INFINITELY
import json
import ast
import random
import requests
import threading
import sys
from config import WAIT_SECONDS, INPUT_FILE_LOCATION, ENDPOINT


def send_events() -> None:
    '''
    Opening an input data file that contains JSON values, then randomly selecting an occurrence of such value
    from the data file, taking this random JSON value event as arequest and sending a response to an ENDPOINT
    :return: None
    '''
    with open(INPUT_FILE_LOCATION) as f:
        sys.stderr.write(f'INP: {INPUT_FILE_LOCATION}\n')
        data = ast.literal_eval(f.read())
        random_data = json.dumps(random.choice(data))
        response = requests.post(url=ENDPOINT, data=random_data)
        print(response.text)
    threading.Timer(int(WAIT_SECONDS), send_events).start()


if __name__ == '__main__':
    try:
        send_events()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)