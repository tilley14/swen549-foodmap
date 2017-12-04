""" foodmap_utils.py

    RIT Food Map is a demonstration of utilizing Cloud Technologies for SWEN 549
    It utilizes Google's Maps API, as well as Google's Cloud Storage.
    Deployed on Google App Engine.

    @Authors Nikolas Tilley
"""

import os
import cloudstorage as gcs

from google.appengine.api import users
from google.appengine.api import app_identity


def get_bucket_info():
    bucket_name = os.environ.get('BUCKET_NAME', app_identity.get_default_gcs_bucket_name())
    info = ('version: ' + os.environ['CURRENT_VERSION_ID'] + '\n'
            + 'name: ' + bucket_name)
    return info


def list_bucket_contents(folder_name=''):
    # Get the Default Bucket Name
    bucket_name = os.environ.get('BUCKET_NAME', app_identity.get_default_gcs_bucket_name())
    bucket = '/' + bucket_name
    contents = ''

    folder = '/' + folder_name

    page_size = 1
    files = gcs.listbucket(bucket + folder, max_keys=page_size)
    while True:
        count = 0
        for file in files:
            count += 1
            contents += repr(file) + '</br>'

        if count != page_size or count == 0:
            break
        files = gcs.listbucket(bucket + folder, max_keys=page_size, marker=file.filename)

    return contents


def read_gcs_file(filename):
    bucket_name = os.environ.get('BUCKET_NAME', app_identity.get_default_gcs_bucket_name())
    bucket = '/' + bucket_name

    gcs_file = gcs.open(bucket + '/' + filename)
    file_contents = gcs_file.read()
    gcs_file.close()
    return file_contents