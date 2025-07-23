from flask import Flask, render_template, request
from data_exploration import get_data

app = Flask(__name__)
all_pokemons = get_data("pokemon.csv")

poke_types = set()
for pokemon in all_pokemons:
    poke_types.add(pokemon["Type 1"])
    poke_types.add(pokemon["Type 2"])
    poke_types.discard("")


@app.route("/")
def index():
    # raw_data = get_data("pokemon.csv")
    if not request.args:
        return render_template(
            "search_form.jinja", types=sorted(poke_types), generations=range(1, 7)
        )
    filtered_data = filter_pokemon("pokemon.csv", dict(request.args))
    return render_template("main_page.jinja", data=filtered_data)


@app.route("/<int:number>")
def details(number):
    chosen_monsters = [
        monster for monster in get_data("pokemon.csv") if monster["#"] == str(number)
    ]
    return render_template("details_page.jinja", data=chosen_monsters)


def filter_pokemon(filename, question):
    all_pokemons = get_data(filename)
    result = []
    for pokemon in all_pokemons:
        if pokemon["Type 1"] != question["type"]:
            continue
        if pokemon["Generation"] != question["generation"]:
            continue
        result.append(pokemon)
    return result
