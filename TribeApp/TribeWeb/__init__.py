from flask import Blueprint

web = Blueprint('web', __name__)

from TribeApp.TribeWeb import routes