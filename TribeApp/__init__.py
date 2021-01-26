from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_script import Manager
from flask_login import LoginManager
from flask_json import FlaskJSON

from config import *

db = SQLAlchemy()
login = LoginManager()
migrate = Migrate()
json = FlaskJSON()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    json.init_app(app)

    from TribeApp.TribeWeb import web
    app.register_blueprint(web)

    from TribeApp.TribeAuthorization import auth_routes 
    app.register_blueprint(auth_routes, url_prefix='/auth')

    from TribeApp.TribeAPI.BaseAPI import api_routes 
    app.register_blueprint(api_routes, url_prefix='/api')

    return app


from TribeApp import models

# if __name__ == '__main__':
#     Manager.run()