import json
import logging
import sys
from data_validation import Event
from marshmallow import ValidationError
from config import TARGET_FILE_LOCATION
from output import persist_output
from flask import Blueprint
from flask import request, Response, jsonify


routes = Blueprint("routes", __name__)
@routes.route('/event', methods=["POST"])
def event_endpoint():
    try:
        request_json = request.get_json(force=True)
        print("hello", request_json)
        Event().load(request_json)
        persist_output(request_json, TARGET_FILE_LOCATION)
        print("hi", request_json)
        # print(jsonify(request_json))
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
