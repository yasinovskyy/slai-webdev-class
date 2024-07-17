# Day 1: Data processing

We work with a dataset stored in a CSV file and build a `Flask` application to present the data as a web page.

## Learning goals

- Set up development environment using *Visual Studio Code*, `python-venv`, and `Flask`
- Review Python and use `csv` module of the standard library to read data from a file.
- Understand the difference between various collections (`list`, `dict`, `tuple`) in Python.
- Create and initialize development environment using `venv`.
- Understand fundamentals of networking and client-server architecture.
- Understand fundamentals of `HTTP`.
- Start working with `Flask` and develop a simple web application.
- Understand basic structure (`head` and `body`) of a web page.

## Process

1. Python script is used to access a CSV file and explore the data within.
    - Script is broken into functions with guardrails around `main` so that it can later be imported into our `Flask` app.
    - Use command line to run the script.
2. Application has a couple routes and relies on the results provided by the data retrieval function.
3. Use `flask run` and `flask run --debug` from the command line to run *app.py* and access it via <http://localhost:5000>.

## Demo

1. Python script used to explore and present data read from a CSV file.
1. `Flask` application that returns some information about a specific record in the file.
1. Basic HTML is used to highlight some part of the returned text.

## Student outcomes

Students should be able to:

1. Set up their development environment.
2. Run Python script from command line.
3. Start `Flask` app from command line.
4. Access the app in their browser.
5. Debug Python code.

## References

- [Flask 3.0 documentation](https://flask.palletsprojects.com/en/3.0.x/)
- [Pokemon dataset](https://gist.github.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6)
