# Test file for Birthday Reminder Application
# Created by Aurimas A. Nausedas on 07/23/22.


import sys
sys.path.insert(0, '/Users/aurimasnausedas/Documents/Python/ServicesCommunication/Event_Propagator')
from Event_Propagator.propagate import send_events
# sys.path.insert(0, '/Users/aurimasnausedas/Documents/Python/ServicesCommunication/Event_Consumer')
# from Event_Consumer import routes, main, output, data_validation
# from Event_Consumer.data_validation import Event
# from Event_Consumer.routes import validate

def test_correct_send_event():
    data = {
      "event_payload": "hello",
      "event_type": "message"
    }
    assert data.send_events() == {"event_payload": "hello", "event_type": "message"}
# def test_correct_correct_validation():
#     """
#     Testing if the correct json data is provided..
#
#     :assert: bool
#     """
#     data = {'event_type': 'message', 'event_payload': 'yes, please'}
#     correct = {'event_type': 'message', 'event_payload': 'yes, please'}
#     print(type(data))
#     assert data.validate() == correct
#
# def test_correct_data_validation_with_correct_variable():
#     """
#     Testing if the correct json data is provided..
#
#     :assert: bool
#     """
#     data = Event().validate("Hello")
#     correct = {'_schema': ['Invalid input type.']}
#     assert data == correct
#
# def test_correct_data_validation_with_incorrect_variable():
#     """
#     Testing if the correct json data is provided..
#
#     :assert: bool
#     """
#     data = Event().validate({})
#     missing = {'event_payload': ['Missing data for required field.'], 'event_type': ['Missing data for required field.']}
#     print(type(data))
#     assert data == missing
