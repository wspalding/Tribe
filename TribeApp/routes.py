
from flask import render_template
from flask import jsonify, request
from flask_sqlalchemy import SQLAlchemy

from TribeApp import app
from TribeApp.Models.TribeModel import Tribe

from json import loads

db = SQLAlchemy(app)

@app.route('/')
@app.route('/index')
def index():
    tribes = Tribe.query.all()
    return render_template('index.html', tribes=tribes)




# ! API
@app.route('/test', methods=['GET'])
def test_api():
    response = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    return jsonify(response)



@app.route('/tribe/create', methods=['POST'])
def create_tribe():
    tribe = loads(request.data)
    try:
        new_tribe = Tribe(
            name=tribe['name'],
        )
        db.session.add(new_tribe)
        db.session.commit()
    except Exception as e:
        return jsonify("error creating Tribe, error: {}".format(e))

    return jsonify(new_tribe.members)

