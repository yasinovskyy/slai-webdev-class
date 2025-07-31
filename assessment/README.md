# Complete application

## Goals

Develop a small application that uses Flask, Jinja, and MVP.css to display animals in a menagerie and allow users search for specific animals based on their species, location, or age.

## Outcomes

An application with the following functionality:

1. All animals are loaded from *menagerie.csv*.
2. All animals are displayed as a table at the main route "/".
3. Animal name must be a link to its details page (available at the route "/animal_id").
4. Animal details page must contain a short description of the animal including its name as an `h3` element, species, and age.
5. Search `form` with `action` */search* and `method` *GET* is available at the route "/search".
6. Submit button as an `input` element of `type` *submit* with `id` *btnSubmit*.
7. Users must be able to search by
     - species (`select` element with `name` *species* and `id` *selSpecies*)
     - location (`select` element with `name` *location* and `id` *selLocation*)
     - minimum age (`number` input element with `name` *min_age* and `id` *numMinAge*)
     - maximum age (`number` input element with `name` *max_age* and `id` *numMaxAge*)
8. When searching, any criterion may be omitted by users.
9. Every page must contain a link to the home and the search pages.
10. Errors must be handled, the application must not crash.

## Demo

Use the following command to run the application:

```bash
flask run
```

## Test

In order to test your application you must activate a virtual environment and install the following packages:

```text
playwright
pytest
pytest-playwright
pytest-timeout
```

```bash
python -m pip install playwright pytest pytest-playwright pytest-timeout
```

Once those packages are installed you should be able to test the application:

```bash
python -m pytest tests/
```

Back-end (logic) and front-end (user interface) of the application can be tested separately:

```bash
python -m pytest tests/test_menagerie_back.py
python -m pytest tests/test_menagerie_front.py
```

