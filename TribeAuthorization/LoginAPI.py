from flask import Blueprint
from flask import jsonify
from flask_login import current_user, login_user

from TribeApp.Models.UserModel import User


auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route('/login', methods=['GET', 'POST'])
def test_api():
    response = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    return jsonify(response)


@auth_routes.route('/signup', methods=['GET', 'POST'])
def sign_up():
    response = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    return jsonify(response)
