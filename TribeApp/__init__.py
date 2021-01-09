from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_script import Manager
from flask_login import LoginManager
from config import *

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db = SQLAlchemy(app)
login = LoginManager(app)

from TribeApp import routes, models


if __name__ == '__main__':
    Manager.run()