from flask_sqlalchemy import SQLAlchemy
from TribeApp import app
from TribeApp.Models.TribeModel import Tribe
db = SQLAlchemy(app)


class TribeService:
    pass