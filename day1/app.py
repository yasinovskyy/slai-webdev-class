from flask import Flask
from data_exploration import read_csv

app = Flask(__name__)


@app.route("/")
def index():
    data = read_csv("pokemon.csv")
    return data


@app.route("/<int:pok_id>")
def details(pok_id):
    data = read_csv("pokemon.csv")
    return data[pok_id]
