import json
import logging
import sys
from .data_validation import Event
from .output import persist_output
from marshmallow import ValidationError
from flask import Blueprint
from flask import request, Response
sys.path.insert(0, "/EventConsumer")
from config import TARGET_FILE_LOCATION


routes = Blueprint("routes", __name__)

@routes.route('/event', methods=["POST"])
def event_endpoint():
    '''
    The function handles /event POST requests by persisting valid payloads
    into the TARGET_FILE_LOCATION defined on startup. Successful requests
    return Success 200 status codes, and invalid requests return
    a Bad Request with the error message printed
    :return: Response
    '''
    try:
        request_json = request.get_json(force=True)
        Event().load(request_json)
        persist_output(request_json, TARGET_FILE_LOCATION)
        return request_json

    except ValidationError as err:
        logging.error(f"Bad request was sent with {err}")
        res_str = json.dumps({"error": f"Validation error - {err}"})
        resp = Response(response=res_str, status=400, mimetype="application/json")
        return resp

    except Exception as error:
        res_str = json.dumps({"error": f"Unknown error - {error}"})
        resp = Response(response=res_str, status=400, mimetype="application/json")
        sys.stderr.write(f'ERROR : {error}\n')
        return resp
