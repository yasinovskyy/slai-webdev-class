# Complete application

## Goals

Develop a small application that uses Flask, Jinja, and MVP.css to display animals in a menagerie and allow users search for specific animals based on their species, location, or age.

## Outcomes

An application with the following functionality:

1. All animals are loaded from *menagerie.csv*.
2. All animals are displayed as a table at the main route "/".
3. Search form is available at "/search".
4. Users must be able to search by
     - species (`select` element with `id` *selSpecies*)
     - location (`select` element with `id` *selLocation*)
     - age (min and max) (`number` input elements with ids *numMinAge* and *numMaxAge* respectively)
5. When searching, any criterion may be omitted by users.
6. Animal name must be a link to its details page.
7. Animal details page must contain a short description of the animal including its name as an `h3` element, species, and age.
8. Every page must contain a link to the home and the search pages.
9. Errors must be handled, the application must not crash.

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

Once those packages are installed you should be able to test the application:

```bash
python -m pytest tests/
```
