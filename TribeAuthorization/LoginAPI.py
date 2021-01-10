from flask import Blueprint
from flask import jsonify
from flask_login import current_user, login_user
from flask import request

# from TribeApp.Models.UserModel import User


auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route('/login', methods=['GET', 'POST'])
def test_api():
    username = request.data['username']
    password = request.data['password']
    return jsonify({
        'username': username,
        'password': password
    })


@auth_routes.route('/signup', methods=['GET', 'POST'])
def sign_up():
    body = request.get_json()
    print(body)
    email = body.get('email')
    username = body.get('username')
    password = body.get('password')
    return jsonify({
        'email': email,
        'username': username,
        'password': password
    })