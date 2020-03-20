"""
Challenge 2
Create test_challenge2.py and write a test that does the following:

Go to copart.com
Search for "exotics"
Assert "PORSCHE" is in the list of cars on the Results Page
"""
from selenium.webdriver.common.keys import Keys


def test_challenge_two(py):
    search_word = 'exotics'
    assert_word = 'PORSCHE'

    py.visit('https://www.copart.com')
    py.get('#input-search').type(search_word, Keys.ENTER)
    assert py.contains(assert_word)


# def test_challenge_two(py):
#     search_word = 'exotics'
#     assert_word = 'PORSCHE'
#
#     py.visit('https://www.copart.com')
#     py.get('#input-search').type(search_word, Keys.ENTER)
#     results = py.xpath('//*[@id="serverSideDataTable"]/tbody')
#
#     assert assert_word in results.text
