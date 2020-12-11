
from flask import render_template
from flask import jsonify
from TribeApp import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', username='person1')





@app.route('/' methods=['GET'])
def test_api()
    response = {
        "value1": "hello",
        "value2": "world"
    }
    return jsonify(response)