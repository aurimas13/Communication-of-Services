from queue import Queue
import random
import threading
import multiprocessing as mp

MAX_QSIZE = 10  # max queue size
BUFF_SIZE = 100  # total number of iterations/items to process


class Producer:
    def __init__(self, queue, buff_size=BUFF_SIZE):
        self.queue = queue
        self.buff_size = buff_size

    def run(self):
        for _ in range(self.buff_size):
            self.queue.put(random.randint(0, 100))


class Consumer:
    def __init__(self, queue):
        self.queue = queue

    def run(self):
        while not self.queue.empty():
            item = self.queue.get()
            self.queue.task_done()
            print(item)


def main():
    q = Queue(maxsize=MAX_QSIZE)

    producer = Producer(q)
    producer_thread = threading.Thread(target=producer.run)

    consumer = Consumer(q)
    consumer_thread = threading.Thread(target=consumer.run)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()

    q.join()

if __name__ == "__main__":
    main()


# routes.py:
# import json
# import logging
# from data_validation import Event
# from marshmallow import ValidationError
# from flask import Blueprint
# from flask import request, Response, jsonify
# from pprint import pprint
#
#
# routes = Blueprint("routes", __name__)


# @routes.route("/event", methods=["POST"])
# def get_json():
#     try:
#         # Event().load(event_data)
#         # pprint(event_data)
#         # request_json = {"event_type":"user_left", "event_payload":"Thomas"}
#         request_json = request.get_json(force=True)
#         pprint(request_json)
#         Event().load(request_json)
#         # dictToReturn = {
#         #     "event_type" : request_json["event_type"],
#         #     "event_payload" : request_json["event_payload"]
#         # }
#         # pprint(dictToReturn)
#         # return jsonify(dictToReturn)
#         return jsonify(request_json)
#         # return jsonify(
#         #     event_type=g.user.username,
#         #     event_payload=g.user.email,
#         #     id=g.user.id
#         # )
#     # input_json = request.get_json(force=True)
#     # dictToReturn = {
#     #     "event_type": input_json["event_type"],
#     #     "event_payload": input_json["event_payload"]
#     # }
#     # return jsonify(dictToReturn)
#
#     except ValidationError as err:
#         logging.error(f"Bad request was sent with {err}")
#         res_str = json.dumps({
#             "error": f"Validation error: {err}",
#         })
#         resp = Response(
#             response=res_str, status=400, mimetype="application/json")
#         # pprint(err.messages)
#         return resp

# Python program INFINITELY
import json
import ast
import random
import requests
from requests.structures import CaseInsensitiveDict

url="http://127.0.0.1:4444/event"
payload = json.dumps({
    "event_type": "message",
    "event_payload": "Anna"
})
# headers = requests.utils.default_headers()
headers = {
    "Content-Type" : "text/plain",
    "Content-Length" : "0"
}
# print(headers)
# headers['User-Agent'] = 'python-requests/2.25.0'
# headers["User-Agent"] = "keep-alive"
# r = requests.post(url, data=payload, headers=headers)
# print(r.status_code, r.text)

# Opening JSON file
f = open('events.json')

# Data load
data = json.load(f)
l = json.dumps(random.choice(data))
r = requests.post(url, data=l, headers=headers)
print(r.status_code, r.text)
# for i in data:
#     print(i)

# api-endpoint
URL = 'http://127.0.0.1:4444/event'

# # sending post request and saving the response as response object
# r = requests.post(URL, l)
#
# # # extracting data in json format
# # data = r.json()
# print(r.text)
# Closing file
f.close()


# with open('events.json') as f:
#     data = ast.literal_eval(f.read())
#     l = random.choice(data)
    # print(l)
    # for i in data:
    #     # result = {k: random.choice(v) for k, v in i.items()}
    #     print(i)