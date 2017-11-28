from flask import Flask
from flask import render_template

import logging

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "Hello From Heroku Bitches!!!"

@app.route('/<name>', methods=['GET'])
def hello_world(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run()
