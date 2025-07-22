from flask import Flask, render_template
from data_exploration import get_data

app = Flask(__name__)


@app.route("/")
def index():
    raw_data = get_data("pokemon.csv")
    return render_template("main_page.jinja", data=raw_data)


@app.route("/<int:number>")
def details(number):
    chosen_monsters = [
        monster for monster in get_data("pokemon.csv") if monster["#"] == str(number)
    ]
    return render_template("details_page.jinja", data=chosen_monsters)
