#!/usr/bin/python3
"""Module to start a web applicaction
"""

from cgitb import text
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def str_text(text):
    return ('C {}'.format(text.replace("_", " ")))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    return ('Python {}'.format(text.replace("_", " ")))


@app.route('/number/<int:n>', strict_slashes=False)
def n_int(n):
    return ('{} is a number'.format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_HTML_n_int(n):
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
