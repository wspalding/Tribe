from flask import jsonify
from flask_login import current_user, login_user, logout_user
from flask import request, redirect, url_for
from TribeApp.TribeAuthorization import auth_routes

from TribeApp.TribeAuthorization.Validation import PasswordValidation 

from TribeApp.Models.UserModel import User
from TribeApp import db

from flask_json import json_response

@auth_routes.route('/login', methods=['GET', 'POST'])
def login():
    body = request.get_json()
    username = body.get('username')
    password = body.get('password')
    remember_me = body.get('remember_me')
    user = User.query.filter_by(username=username).first()
    if user is None or not user.check_password(password):
        return json_response(success=False, message='Could not authenticate username and password')
    login_user(user, remember=remember_me)
    return json_response(success=True, message='Success')


@auth_routes.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return json_response(success=False, message='user is already authenticated')
    body = request.get_json()
    email = body.get('email')
    username = body.get('username')
    password = body.get('password')
    if not PasswordValidation.validate_password(password):
        return json_response(success=False, message='invalid password')
    new_user = User(username=username,
                    password=password,
                    email=email)
    db.session.add(new_user)
    db.session.commit()
    return json_response(success=True, message='Success')



@auth_routes.route('/logout')
def logout():
    logout_user()
    return json_response(success=True, message='user has been logged out')