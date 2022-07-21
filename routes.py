from flask import Blueprint
from flask import request, jsonify

# from api.services.auth_service import AuthService


routes = Blueprint("routes", __name__)


@routes.route("/event", methods=["POST"])
def testpost():
    input_json = request.get_json(force=True)
    dictToReturn = {'text': input_json['text']}
    return jsonify(dictToReturn)
# def login():
#     return AuthService.auth_user(request)