from flask import Flask
from data_exploration import get_data

app = Flask(__name__)


@app.route("/")
def index():
    data = get_data("pokemon.csv")
    return data


@app.route("/<int:number>")
def details(number):
    return "I don't know what to do with this number"
