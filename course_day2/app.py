from flask import Flask, render_template
from data_exploration import read_data

app = Flask(__name__)


@app.route("/")
def index():
    data = read_data("pokemon.csv")
    return render_template("index.jinja", template_data=data)


@app.route("/<int:poke_number>")
def pokemon_details(poke_number):
    data = [record for record in read_data("pokemon.csv") if int(record["#"]) == poke_number]
    return render_template("details.jinja", poke_data=data)


@app.route("/<string:poke_type>")
def poke_type(poke_type): ...


@app.route("/speed/<int:min_speed>/<int:max_speed>")
def poke_by_speed(min_speed, max_speed):
    data = [
        record
        for record in read_data("pokemon.csv")
        if int(record["Speed"]) > min_speed and int(record["Speed"]) < max_speed
    ]
    return render_template("index.jinja", template_data=data)
