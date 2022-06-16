#!/usr/bin/python3
"""This is 0-hello_route module containing script that
starts a Flask web application.
"""
from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """Prints the hello message for the base url"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def just_hbnb():
    """Prints only HBNB for the route hbnb"""
    return 'HBNB'


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
