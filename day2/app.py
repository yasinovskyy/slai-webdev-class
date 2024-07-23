from flask import Flask, render_template
from data_exploration import read_csv

app = Flask(__name__)


@app.route("/")
def index():
    data = read_csv("pokemon.csv")
    return render_template("index.html", data=data)


@app.route("/<int:pok_id>")
def details(pok_id):
    result = []
    data = read_csv("pokemon.csv")
    for monster in data:
        if int(monster.get("#")) == pok_id:
            result.append(monster)
    if result:
        return render_template("details.html", data=result)
    return "Not found"
