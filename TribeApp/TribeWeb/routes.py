from flask import Blueprint
from flask import jsonify
from flask import render_template
from TribeApp.TribeWeb import web


@web.route('/')
@web.route('/index')
def index():
    return render_template('index.html', username='person1')

