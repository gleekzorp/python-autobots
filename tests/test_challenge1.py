"""
Challenge 1
Within test_challenge1.py, write a new test that does the following:

Go to google.com
Search for “puppies”
Assert that the results page that loads has “puppies” in its title
"""

from selenium.webdriver.common.keys import Keys


def test_google_search(py):
    py.visit('https://www.google.com')
    py.get('[name="q"]').type('puppies', Keys.ENTER)
    assert 'puppies' in py.title
