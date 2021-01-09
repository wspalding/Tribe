from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_script import Manager
from flask_login import LoginManager

from config import *

from TribeAPI.BaseAPI import api_routes
from TribeAuthorization.LoginAPI import auth_routes

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.register_blueprint(api_routes, url_prefix='/api')
app.register_blueprint(auth_routes, url_prefix='/auth')

db = SQLAlchemy(app)
login = LoginManager(app)

from TribeApp import routes, models


if __name__ == '__main__':
    Manager.run()