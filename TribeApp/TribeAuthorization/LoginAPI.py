from flask import jsonify
from flask_login import current_user, login_user
from flask import request, redirect, url_for
from TribeApp.TribeAuthorization import auth_routes

from TribeApp.Models.UserModel import User
from TribeApp import db

@auth_routes.route('/login', methods=['GET', 'POST'])
def test_api():
    username = request.data['username']
    password = request.data['password']
    user = User.query.filter_by(username=username).first()
    if user is None or not user.check_password(password):
        return jsonify({
            'success': False
            })
    login_user(user, remember=remember_me.data)
    return jsonify({
        'success': True
        })


@auth_routes.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    body = request.get_json()
    email = body.get('email')
    username = body.get('username')
    password = body.get('password')
    new_user = User(username=username,
                    password=password,
                    email=email)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({
        'success': True
        })