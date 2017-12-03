from flask import Flask
from flask import render_template

import logging
import requests

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


@app.route('/submit', methods=['POST'])
def writeData(request):
    #request.data
    #write(data)
    pass

if __name__ == '__main__':
    app.run()
