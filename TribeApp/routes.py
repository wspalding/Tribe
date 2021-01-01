
from flask import render_template
from flask import jsonify
from TribeApp import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', username='person1')


@app.route('/test', methods=['GET'])
def test_api():
    response = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    return jsonify(response)

