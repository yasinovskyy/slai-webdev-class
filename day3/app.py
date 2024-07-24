from flask import Flask, render_template, request
from data_exploration import read_csv

app = Flask(__name__)
app.generations = range(1, 7)


@app.get("/")
def form_view():
    return render_template("form_view.html", generations=app.generations)


@app.post("/")
def index():
    if request.form:
        return render_template("index.html", data=query(dict(request.form)))


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


def query(question):
    result = []
    data = read_csv("pokemon.csv")
    for monster in data:
        if question["generation"] != monster["Generation"]:
            continue
        if not (
            int(question.get("hp_min", "0"))
            < int(monster["HP"])
            < int(question.get("hp_max", "1000"))
        ):
            continue
        if "legendary" in question and monster["Legendary"] == "False":
            continue
        result.append(monster)
    return result
