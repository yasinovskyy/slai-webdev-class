from data_exploration import read_csv
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Welcome to SLAI!"


@app.route("/<int:number>")
def details(number):
    data = read_csv("pokemon.csv")
    return data[number]
