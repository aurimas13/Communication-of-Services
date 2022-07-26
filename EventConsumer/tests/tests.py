# Test file for Birthday Reminder Application
# Created by Aurimas A. Nausedas on 07/25/22.
# Updated by Aurimas A. Nausedas on 07/26/22.

import json

def test_correct_request_code(client):
    response = client.post("/event", data=json.dumps({
        "event_type": "user_left",
        "event_payload": "Cosmo"
    }))
    assert response.status_code == 200


def test_correct_request_output(client):
    response = client.post("/event", data=json.dumps({
        "event_type": "user_left",
        "event_payload": "Cosmo"
    }))
    assert response.get_json() == {"event_type": 'user_left', "event_payload": "Cosmo"}


def test_incorrect_response_code(client):
    response = client.post("/event", data=json.dumps({
        "event_type": "user_left",
        "event_payload": 1
    }))
    assert response.status_code == 400


def test_incorrect_response_code_two(client):
    response = client.post("/event", data=json.dumps({
        "event_type": 2,
        "event_payload": "hello"
    }))
    assert response.status_code == 400


def test_incorrect_response_for_event_payload(client):
    response = client.post("/event", data=json.dumps({
        "event_type": "message",
        "event_payload": 2
    }))
    assert response.get_json() == {"error": "Validation error - {'event_payload': ['Not a valid string.']}"}


def test_incorrect_response_for_event_type(client):
    response = client.post("/event", data=json.dumps({
        "event_type": 2,
        "event_payload": "Thomas"
    }))
    assert response.get_json() == {"error": "Validation error - {'event_type': ['Not a valid string.']}"}
