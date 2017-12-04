from flask import Flask, Response
from flask import render_template, url_for

import logging
import requests
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "This is the home route. Just testing flask. By Kevin"


@app.route('/vue/<name>', methods=['GET'])
def hello_world(name=None):
    return render_template('hello.html', name=name)


@app.route('/map', methods=['GET'])
def test_map():
    dataURL = url_for('feedData', _external=True)
    return render_template('maptest.html', dataURL=dataURL)


@app.route('/feedData', methods=['GET'])
def feedData():
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    data = open(os.path.join(APP_ROOT, 'static/earthquake.json')).read() # TODO subsitute in for reading from GCP
    return 'eqfeed_callback(' + data + ');'
    ##return Response(data, mimetype='.js')



@app.route('/submit', methods=['POST'])
def writeData(request):
    #request.data
    #write(data)
    pass

if __name__ == '__main__':
    app.run()
