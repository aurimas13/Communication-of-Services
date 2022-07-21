import json
import logging
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
        Event().load(request_json)
        persist_output(request_json, target_path)
        return jsonify(request_json)

    except ValidationError as err:
        logging.error(f"Bad request was sent with {err}")
        res_str = json.dumps({"error": f"Validation error - {err}"})
        resp = Response(response=res_str, status=400, mimetype="application/json")
        return resp