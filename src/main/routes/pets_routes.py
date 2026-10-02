from flask import Blueprint, jsonify

pets_routes_bp = Blueprint("pets_routes", __name__)

@pets_routes_bp.route("/pets", methods=["GET"])
def get_pets():
    return jsonify({"Hello": "World"})
