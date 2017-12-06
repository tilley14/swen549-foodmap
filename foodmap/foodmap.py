""" foodmap.py

    RIT Food Map is a demonstration of utilizing Cloud Technologies for SWEN 549
    It utilizes Google's Maps API, as well as Google's Cloud Storage.
    Deployed on Google App Engine.

    @Authors Nikolas Tilley, Edward Wong
"""

from flask import Flask, request
from flask import render_template, url_for
from google.appengine.api import users
from google.appengine.api import app_identity

import json
import logging
import os
import cloudstorage as gcs


default_bucket = app_identity.get_default_gcs_bucket_name()


app = Flask(__name__)


def read_gcs_file(filename="earthquake.json"):

    bucket_name = os.environ.get('BUCKET_NAME', app_identity.get_default_gcs_bucket_name())
    bucket = '/' + bucket_name

    gcs_file = gcs.open(bucket + '/' + filename)
    file_contents = gcs_file.read()
    gcs_file.close()
    return file_contents

@app.route('/', methods=['GET'])
def home():
    """ The actual foodmap that uses Google's map API
    """
    dataURL = url_for('feedData', _external=True)
    return render_template('foodmap.html', dataURL=dataURL)



@app.route('/maptest', methods=['GET'])
def fake_map():
    """ Testing the use of Google's map API
    """
    #dataURL = url_for('feedData', _external=True)
    dataURL = ''
    return render_template('maptest.html', dataURL=dataURL)


@app.route('/feedData', methods=['GET'])
def feedData():
    """ Dynamically creating a Javascript file that contains Data to
        Be displayed by the Map
    """
    #APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    #data = open(os.path.join(APP_ROOT, 'static/earthquake.json')).read()
    data = read_gcs_file()
    return 'eqfeed_callback(' + data + ');'


def write_data(data, title="testing.json"):
    # Write a File
    write_retry_params = gcs.RetryParams(backoff_factor=1.1)

    bucket_name = os.environ.get('BUCKET_NAME', app_identity.get_default_gcs_bucket_name())
    bucket = '/' + bucket_name
    filename = bucket + '/' + title

    gcs_file = gcs.open(filename)
    file_contents = gcs_file.read()
    gcs_file.close()

    gcs_file = gcs.open(filename,
                        'w',
                        content_type='text/plain',
                        retry_params=write_retry_params)

    gcs_file.write(file_contents + data.__str__() + "\n")

    gcs_file.close()
    return "Write complete"

@app.route('/submit', methods=['GET'])
def submit_data():
    # if request.method == 'GET':
    write_data('Writing to the file')
    return 'Write sucessful'
    # elif request.method == 'Post':
    #     data = request.get_json(force=True)
    #     write_data(json.dumps(data))
    #     return "post recieved"
    # else:
    #     return "Error"








if __name__ == '__main__':
    app.run()
