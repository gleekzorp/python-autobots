"""
Challenge 3
Create test_challenge3.py and write a test that does the following:

Go to copart.com
On the Home Page, under Most Popular Items, there is a Makes/Models section. For each Make or Model in this section, print the name of the Make or Model with its URL (aka href) next to it
Example Output: SILVERADO - https://www.copart.com/popular/model/silverado
"""


def test_makes_models(copart):
    makes_models = py.xpath('//*[@id="tabTrending"]/div[1]//a')
    for make_model in makes_models:
        print(f"{make_model.text} - {make_model.get_attribute('href')}")


# def test_makes_models(py):
#     py.visit('https://www.copart.com')
#     makes_models = py.find("[ng-repeat*='popularSearch'] > a")
#     for make_model in makes_models:
#         print(f"{make_model.text} - {make_model.get_attribute('href')}")
