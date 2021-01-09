from flask import render_template
from flask import jsonify
from TribeApp import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', username='person1')

