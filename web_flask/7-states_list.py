#!/usr/bin/python3
"""Module to start a web applicaction
"""

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def session_close():
	storage.close()


@app.route('/states_list', strict_slashes=False)
def display_HTML_db(n):
    return render_template('7-states_list.html', states_list=storage.all(State).values())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
