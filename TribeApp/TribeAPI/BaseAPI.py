from flask import Blueprint
from flask import jsonify

api_routes = Blueprint('api_routes', __name__)


@api_routes.route('/test', methods=['GET'])
def test_api():
    response = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    return jsonify(response)