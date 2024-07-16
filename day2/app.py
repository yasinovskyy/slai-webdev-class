from data_exploration import read_csv
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    result = read_csv("pokemon.csv")
    return render_template("index.html", data=result, greeting="SLAI students")


@app.route("/<int:number>")
def details(number):
    data = read_csv("pokemon.csv")
    result = []
    for monster in data:
        if int(monster["#"]) == number:
            result.append(monster)
    return render_template("details.html", data=result)
