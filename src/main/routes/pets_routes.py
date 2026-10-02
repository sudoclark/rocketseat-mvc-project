from flask import Blueprint, jsonify

from src.main.composer.pets_lister_composer import pets_lister_composer
from src.main.composer.pet_deleter_composer import pet_deleter_composer
from src.views.http_types.http_request import HttpRequest

pets_routes_bp = Blueprint("pets_routes", __name__)

@pets_routes_bp.route("/pets", methods=["GET"])
def get_pets():
    view = pets_lister_composer()
    http_request = HttpRequest()
    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code

@pets_routes_bp.route("/pets/<name>", methods=["DELETE"])
def delete_pet(name):
    view = pet_deleter_composer()
    http_request = HttpRequest(param={"name": name})
    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code
