#!/usr/bin/env python3
"""
Using pytest-playwright to test the front end

@authors: Roman Yasinovskyy
@version: 2025.7
"""

import subprocess

import pytest
from playwright.sync_api import Page

TIMEOUT = 1000


def setup_module(module):
    """Create the server fixture"""
    module.server = subprocess.Popen(["flask", "run"])
    try:
        module.server.wait(timeout=1)
    except subprocess.TimeoutExpired:
        pass


def teardown_module(module):
    """Stop the server"""
    module.server.terminate()


def test_main_page(page: Page) -> None:
    """Default table on the main page"""
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:5000/")
    assert len(page.query_selector_all("table > tbody > tr")) == 10


@pytest.mark.parametrize(
    "a_id, name",
    [
        (1, "Chunk"),
        (2, "Wind"),
        (3, "Underrated Thunder"),
        (4, "Axe"),
        (5, "Wild Isotope"),
        (6, "Night Star"),
        (7, "Random Bully"),
        (8, "Cunning Fury"),
        (9, "Evening Chunk"),
        (10, "Thunder"),
    ],
)
def test_details_page(page: Page, a_id: int, name: str) -> None:
    """Animal name on the details page"""
    page.set_default_timeout(TIMEOUT)
    page.goto(f"http://localhost:5000/{a_id}")
    assert page.locator("h3").inner_text() == name


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
def test_search(page: Page, species: str, location: str, found: int) -> None:
    """Various combinations of species/location yield different results"""
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:5000/search")
    page.select_option("#selSpecies", species)
    page.select_option("#selLocation", location)
    page.click("#btnSubmit")
    assert len(page.query_selector_all("table > tbody > tr")) == found


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
def test_search_with_age(
    page: Page, species: str, location: str, min_age: int, max_age: int, found: int
) -> None:
    """Various combinations of species/location/age range yield different results"""
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:5000/search")
    page.select_option("#selSpecies", species)
    page.select_option("#selLocation", location)
    page.fill("#numMinAge", str(min_age))
    page.fill("#numMaxAge", str(max_age))
    page.click("#btnSubmit")
    assert len(page.query_selector_all("table > tbody > tr")) == found


@pytest.mark.parametrize(
    "species, location, max_age, found",
    [
        ("any", "any", 25, 1),
        ("any", "any", 50, 7),
        ("any", "any", 100, 10),
        ("any", "Attic", 30, 1),
        ("any", "Attic", 35, 2),
        ("any", "Attic", 100, 3),
        ("any", "Back yard", 50, 1),
        ("any", "Back yard", 100, 2),
        ("any", "Basement", 50, 1),
        ("any", "Basement", 75, 2),
        ("any", "Basement", 100, 3),
        ("any", "Garage", 25, 1),
        ("any", "Garage", 50, 2),
        ("Jaguar", "any", 35, 1),
        ("Jaguar", "any", 100, 2),
        ("Newt", "any", 30, 1),
        ("Newt", "any", 50, 2),
        ("Newt", "any", 100, 3),
    ],
)
def test_search_without_min_age(
    page: Page, species: str, location: str, max_age: int, found: int
) -> None:
    """Various combinations of species/location/age range yield different results"""
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:5000/search")
    page.select_option("#selSpecies", species)
    page.select_option("#selLocation", location)
    page.fill("#numMaxAge", str(max_age))
    page.click("#btnSubmit")
    assert len(page.query_selector_all("table > tbody > tr")) == found


@pytest.mark.parametrize(
    "species, location, min_age, found",
    [
        ("any", "any", 0, 10),
        ("any", "any", 50, 4),
        ("any", "Attic", 25, 3),
        ("any", "Attic", 30, 2),
        ("any", "Attic", 35, 1),
        ("any", "Back yard", 0, 2),
        ("any", "Back yard", 51, 1),
        ("any", "Basement", 40, 3),
        ("any", "Basement", 60, 2),
        ("any", "Basement", 80, 1),
        ("any", "Garage", 0, 2),
        ("any", "Garage", 26, 1),
        ("Jaguar", "any", 0, 2),
        ("Jaguar", "any", 36, 1),
        ("Newt", "any", 20, 3),
        ("Newt", "any", 40, 2),
        ("Newt", "any", 60, 1),
    ],
)
def test_search_without_max_age(
    page: Page, species: str, location: str, min_age: int, found: int
) -> None:
    """Various combinations of species/location/age range yield different results"""
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:5000/search")
    page.select_option("#selSpecies", species)
    page.select_option("#selLocation", location)
    page.fill("#numMinAge", str(min_age))
    page.click("#btnSubmit")
    assert len(page.query_selector_all("table > tbody > tr")) == found


@pytest.mark.parametrize(
    "species, location",
    [
        ("Armadillo", "Attic"),
        ("Armadillo", "Basement"),
        ("Armadillo", "Garage"),
        ("Humboldt Penguin", "Back yard"),
        ("Humboldt Penguin", "Basement"),
        ("Humboldt Penguin", "Garage"),
        ("Jaguar", "Back yard"),
        ("Jaguar", "Basement"),
        ("Jaguar", "Garage"),
        ("Long-Eared Owl", "Attic"),
        ("Long-Eared Owl", "Back yard"),
        ("Long-Eared Owl", "Basement"),
        ("Macaroni Penguin", "Attic"),
        ("Macaroni Penguin", "Back yard"),
        ("Macaroni Penguin", "Garage"),
        ("Newt", "Attic"),
        ("Newt", "Back yard"),
        ("Pink Fairy Armadillo", "Attic"),
        ("Pink Fairy Armadillo", "Basement"),
        ("Pink Fairy Armadillo", "Garage"),
    ],
)
def test_search_without_results(page: Page, species: str, location: str) -> None:
    """Various combinations of species/location yield no results"""
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:5000/search")
    page.select_option("#selSpecies", species)
    page.select_option("#selLocation", location)
    page.click("#btnSubmit")
    assert len(page.query_selector_all("table > tbody > tr")) == 0


if __name__ == "__main__":
    pytest.main(["-v", __file__])
