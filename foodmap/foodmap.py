""" foodmap.py

    RIT Food Map is a demonstration of utilizing Cloud Technologies for SWEN 549
    It utilizes Google's Maps API, as well as Google's Cloud Storage.
    Deployed on Google App Engine.

    @Authors Nikolas Tilley
"""

from flask import Flask, Response
from flask import render_template, url_for
from google.appengine.api import users
from google.appengine.api import app_identity


import logging
import requests
import os
import cloudstorage as gcs


default_bucket = app_identity.get_default_gcs_bucket_name()


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    """ Testing GCP
    """
    return "This is the home route. Just testing flask. By Kevin"


@app.route('/vue/<name>', methods=['GET'])
def hello_world(name=None):
    """ Testing the use of Vue with Jinja2 templates
    """
    return render_template('hello.html', name=name)


@app.route('/map', methods=['GET'])
def test_map():
    """ Testing the use of Google's map API
    """
    dataURL = url_for('feedData', _external=True)
    return render_template('foodmap.html', dataURL=dataURL)


@app.route('/feedData', methods=['GET'])
def feedData():
    """ Dynamically creating a Javascript file that contains Data to
        Be displayed by the Map
    """
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    data = open(os.path.join(APP_ROOT, 'static/earthquake.json')).read() # TODO subsitute in for reading from GCP
    return 'eqfeed_callback(' + data + ');'


@app.route('/submit', methods=['POST'])
def write_data():
    """ Writes JSON data to our Food Data file in Google Cloud Storage
    """
    # Write a File

    # TODO read data from Request

    write_retry_params = gcs.RetryParams(backoff_factor=1.1)

    filename = '/<bucket_name>/food.dat'
    gcs_file = gcs.open(filename,
                        'w',
                        content_type='text/plain',
                        retry_params=write_retry_params)

    gcs_file.write("SomeData") # TODO make sure that this appends to the end of the file

    gcs_file.close()
    return 'Successful Write'


if __name__ == '__main__':
    app.run()
