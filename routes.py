import json
import logging
from data_validation import Event
from marshmallow import ValidationError
from flask import Blueprint
from flask import request, Response, jsonify


routes = Blueprint("routes", __name__)


@routes.route("/event", methods=["POST"])
def validate():
    try:
        request_json = request.get_json(force=True)
        Event().load(request_json)
        return jsonify(request_json)

    except ValidationError as err:
        logging.error(f"Bad request was sent with {err}")
        res_str = json.dumps({"error": f"Validation error - {err}"})
        resp = Response(response=res_str, status=400, mimetype="application/json")
        return resp