from flask import Blueprint, jsonify

from src.main.composer.pets_lister_composer import pets_lister_composer
from src.main.composer.pet_deleter_composer import pet_deleter_composer
from src.views.http_types.http_request import HttpRequest
from src.errors.error_handler import handle_errors

pets_routes_bp = Blueprint("pets_routes", __name__)

@pets_routes_bp.route("/pets", methods=["GET"])
def get_pets():
    try:
        view = pets_lister_composer()
        http_request = HttpRequest()
        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as ex:
        http_response = handle_errors(ex)
        return jsonify(http_response.body), http_response.status_code

@pets_routes_bp.route("/pets/<name>", methods=["DELETE"])
def delete_pet(name):
    try:
        view = pet_deleter_composer()
        http_request = HttpRequest(param={"name": name})
        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as ex:
        http_response = handle_errors(ex)
        return jsonify(http_response.body), http_response.status_code
