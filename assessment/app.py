#!/usr/bin/env python3
"""
Menagerie

@author: Roman Yasinovskyy
@version: 2025.7
"""

from flask import Flask, render_template, request
from data_exploration import read_data


app = Flask(__name__)
# TODO: Read data from the file menagerie.csv using function read_data


@app.route("/")
def index():
    """Render main template with all the data"""
    # TODO: Implement this function


@app.route("/<int:animal_id>")
def animal_details(animal_id):
    """Render the template with details of an animal with the specific id"""
    # TODO: Implement this function


@app.route("/search")
def search():
    """
    Render the search results if there are any request arguments,
    render search form otherwise
    """
    # TODO: Implement this function
    if request.args:
        ...
    else:
        ...


def query(question):
    """Return filtered data based on the user's request"""
    # TODO: Implement this function
