from data_exploration import read_csv
from flask import Flask, render_template, request


def create_app():
    app = Flask(__name__)
    app.data = read_csv("pokemon.csv")
    types = set()
    for monster in app.data:
        types.add(monster["Type 1"])
        if monster["Type 2"]:
            types.add(monster["Type 2"])
    app.types = sorted(types)
    return app


app = create_app()


@app.route("/")
def index():
    return render_template("query_form.html", types=app.types)


@app.post("/")
def index_post():
    question = request.form
    data = query(app.data, question)
    return render_template("index.html", data=data, greeting="SLAI students")


def query(data, question):
    result = []
    ...
    return result


@app.route("/<int:number>")
def details(number):
    result = []
    for monster in app.data:
        if monster["ID"] == number:
            result.append(monster)
    return render_template("details.html", data=result)
