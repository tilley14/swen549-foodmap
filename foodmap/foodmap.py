from flask import Flask
from flask import render_template

import logging

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "This is the home route. Just testing flask. By Kevin"

@app.route('/vue/<name>', methods=['GET'])
def hello_world(name=None):
    return render_template('hello.html', name=name)

@app.route('/map', methods=['GET'])
def test_map():
    return render_template('maptest.html')


if __name__ == '__main__':
    app.run()
