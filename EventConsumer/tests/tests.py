# Test file for Birthday Reminder Application
# Created by Aurimas A. Nausedas on 07/25/22.
# Updated by Aurimas A. Nausedas on 07/26/22.


import json
import sys

def test_correct_request_code(client):
    '''
    Testing if the correct response code is returned by taking a request as a client.
    :param client:
    :return:
    '''
    sys.stdout.write(f'{client}\n')
    response = client.post("/event", data=json.dumps({
        "event_type": "user_left",
        "event_payload": "Cosmo"
    }))
    assert response.status_code == 200


def test_correct_request_output(client):
    '''
    Testing if the correct response output is returned by taking a request as client
    :param client:
    :return:
    '''
    response = client.post("/event", data=json.dumps({
        "event_type": "user_left",
        "event_payload": "Cosmo"
    }))
    assert response.get_json() == {"event_type": 'user_left', "event_payload": "Cosmo"}


def test_incorrect_response_code(client):
    '''
    Testing if the incorrect response code is returned for `event_payload` by taking a request as client
    :param client:
    :return:
    '''
    response = client.post("/event", data=json.dumps({
        "event_type": "user_left",
        "event_payload": 1
    }))
    assert response.status_code == 400


def test_incorrect_response_code_two(client):
    '''
    Testing if the incorrect response code is returned for `event_type` by taking a request as client.
    :param client:
    :return:
    '''
    response = client.post("/event", data=json.dumps({
        "event_type": 2,
        "event_payload": "hello"
    }))
    assert response.status_code == 400


def test_incorrect_response_for_event_payload(client):
    '''
    Testing if the incorrect response output is returned for `event_payload` by taking a request as client.
    :param client:
    :return:
    '''
    response = client.post("/event", data=json.dumps({
        "event_type": "message",
        "event_payload": 2
    }))
    assert response.get_json() == {"error": "Validation error - {'event_payload': ['Not a valid string.']}"}


def test_incorrect_response_for_event_type(client):
    '''
    Testing if the incorrect response output is returned for `event_type` by taking a request as client.
    :param client:
    :return:
    '''
    response = client.post("/event", data=json.dumps({
        "event_type": 2,
        "event_payload": "Thomas"
    }))
    assert response.get_json() == {"error": "Validation error - {'event_type': ['Not a valid string.']}"}
