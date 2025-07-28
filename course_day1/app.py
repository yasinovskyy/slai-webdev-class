from flask import Flask
from data_exploration import read_data

app = Flask(__name__)


@app.route("/")
def index():
    data = read_data("pokemon.csv")
    return data


@app.route("/<int:poke_number>")
def pokemon_details(poke_number):
    data = [record for record in read_data("pokemon.csv") if int(record["#"]) == poke_number]
    return data


@app.route("/<str:poke_type>")
def poke_type(poke_type): ...
