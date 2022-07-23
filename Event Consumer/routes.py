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
target_path = TARGET_FILE_LOCATION


@routes.route("/event", methods=["POST"])
def validate():
    try:
        request_json = request.get_json(force=True)
        # print(request_json)
        # print(type(request_json))
        Event().load(request_json)
        # print(Event().load(request_json))
        persist_output(request_json, target_path)
        # print(persist_output(request_json, target_path))
        # print(jsonify(request_json))
        return jsonify(request_json)

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