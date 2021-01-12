from flask import Blueprint

auth_routes = Blueprint('auth_routes', __name__)

from TribeApp.TribeAuthorization import LoginAPI