#!/usr/bin/env python3
"""
Using pytest-flask to test the back end

@authors: Roman Yasinovskyy
@version: 2025.7
"""

from itertools import product

import pytest

from app import app, query


@pytest.fixture(name="client")
def fixture_client():
    """Create the client fixture"""
    with app.test_client() as test_client:
        with app.app_context():
            yield test_client


def test_status_main(client) -> None:
    """GET request to the main page"""
    assert client.get("/").status_code == 200


@pytest.mark.parametrize(
    "animal_id",
    range(1, 11),
)
def test_status_details(client, animal_id: int) -> None:
    """GET request to the details page"""
    assert client.get(f"/{animal_id}").status_code == 200


def test_status_search_form(client) -> None:
    """GET request to the search page"""
    assert client.get("/search").status_code == 200


@pytest.mark.parametrize(
    "species, location",
    product(
        [
            "any",
            "Armadillo",
            "Humboldt Penguin",
            "Jaguar",
            "Long-Eared Owl",
            "Macaroni Penguin",
            "Newt",
            "Pink Fairy Armadillo",
        ],
        ["any", "Attic", "Back yard", "Basement", "Garage"],
    ),
)
def test_status_search_results(client, species: str, location: str) -> None:
    """GET request with various combinations of species and location"""
    assert client.get("/", data=dict(species=species, location=location)).status_code == 200


@pytest.mark.parametrize(
    "species, location, found",
    [
        ("any", "any", 10),
        ("any", "Attic", 3),
        ("any", "Back yard", 2),
        ("any", "Basement", 3),
        ("any", "Garage", 2),
        ("Armadillo", "any", 1),
        ("Armadillo", "Back yard", 1),
        ("Humboldt Penguin", "any", 1),
        ("Humboldt Penguin", "Attic", 1),
        ("Jaguar", "any", 2),
        ("Jaguar", "Attic", 2),
        ("Long-Eared Owl", "any", 1),
        ("Long-Eared Owl", "Garage", 1),
        ("Macaroni Penguin", "any", 1),
        ("Macaroni Penguin", "Basement", 1),
        ("Newt", "any", 3),
        ("Newt", "Basement", 2),
        ("Newt", "Garage", 1),
        ("Pink Fairy Armadillo", "any", 1),
        ("Pink Fairy Armadillo", "Back yard", 1),
    ],
)
def test_query(species: str, location: str, found: int) -> None:
    """Various combinations of species/location yield different results"""
    assert len(query({"species": species, "location": location})) == found


@pytest.mark.parametrize(
    "species, location, min_age, max_age, found",
    [
        ("any", "any", 0, 50, 7),
        ("any", "any", 51, 100, 3),
        ("any", "Attic", 0, 30, 1),
        ("any", "Attic", 31, 50, 2),
        ("any", "Back yard", 0, 50, 1),
        ("any", "Back yard", 51, 100, 1),
        ("any", "Basement", 0, 50, 1),
        ("any", "Basement", 51, 100, 2),
        ("any", "Garage", 0, 25, 1),
        ("any", "Garage", 26, 50, 1),
        ("Jaguar", "any", 0, 35, 1),
        ("Jaguar", "any", 36, 100, 1),
        ("Newt", "any", 0, 50, 2),
        ("Newt", "any", 51, 100, 1),
    ],
)
def test_query_with_age(
    species: str, location: str, min_age: int, max_age: int, found: int
) -> None:
    """Various combinations of species/location/age range yield different results"""
    assert (
        len(
            query(
                {"species": species, "location": location, "min_age": min_age, "max_age": max_age}
            )
        )
        == found
    )


@pytest.mark.parametrize(
    "species, location",
    [
        ("Armadillo", "Attic"),
        ("Armadillo", "Garage"),
        ("Humboldt Penguin", "Basement"),
        ("Humboldt Penguin", "Garage"),
        ("Jaguar", "Basement"),
        ("Jaguar", "Back yard"),
        ("Long-Eared Owl", "Attic"),
        ("Long-Eared Owl", "Back yard"),
        ("Macaroni Penguin", "Back yard"),
        ("Macaroni Penguin", "Garage"),
        ("Newt", "Attic"),
        ("Newt", "Back yard"),
        ("Pink Fairy Armadillo", "Attic"),
        ("Pink Fairy Armadillo", "Garage"),
    ],
)
def test_query_without_results(species: str, location: str) -> None:
    """Various combinations of species/location yield no results"""
    assert len(query({"species": species, "location": location})) == 0


if __name__ == "__main__":
    pytest.main(["-v", __file__])
