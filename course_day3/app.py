from flask import Flask, render_template, request
from data_exploration import read_data

app = Flask(__name__)
all_pokemons = read_data("pokemon.csv")
all_types = set()
for poke in all_pokemons:
    all_types.add(poke["Type 1"])
    all_types.add(poke["Type 2"])


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


@app.route("/search")
def search():
    return render_template("search.jinja", type_options=sorted(all_types))


@app.route("/results")
def find_pokemons():
    data = query(dict(request.args))
    return render_template("index.jinja", template_data=data)


def query(question):
    data = read_data("pokemon.csv")

    result = []
    for record in data:
        if record["Type 1"] != question["menu_type"]:
            continue
        if int(record["Speed"]) < int(question["min_speed"]) or int(record["Speed"]) > int(
            question["max_speed"]
        ):
            continue
        result.append(record)
    return result
