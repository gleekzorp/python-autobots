"""
Challenge 5
Part 1 - Create test_challenge5.py and write a test that does the following:

Go to copart.com
Search for "porsche"
Change Show Entries to 100
Print the number of occurrences for each Model
Example: There might be x3 PANAMERA T and x11 CAYENNE

Part 2 - Using the same, first three steps of Part 1, write a test that then does the following:

Count the number of occurrences of each Damage type
However, you need to map the Damage types to these:
REAR END
FRONT END
MINOR DENT/SCRATCHES
UNDERCARRIAGE
Any Damage type that does NOT match the above types should be grouped into a MISC Damage type
Example: SIDE and ALL OVER would each count towards MISC

Example Output: REAR END: 2, FRONT END: 7, MINOR DENT/SCRATCHES: 22, UNDERCARRIAGE: 0, MISC: 4
"""
from selenium.webdriver.common.keys import Keys


def test_challenge_five(copart):
    search_word = 'porsche'
    copart.get('#input-search').type(search_word, Keys.ENTER)
    copart.get('[name="serverSideDataTable_length"]').select('100')
    spinner = copart.get("#serverSideDataTable_processing")
    copart.wait.until(lambda _: spinner.get_attribute('style') == 'display: none;')

    damage_type_list = copart.find('[data-uname="lotsearchLotdamagedescription"]')
    damage_type_dict = {
        "REAR END": 0,
        "FRONT END": 0,
        "MINOR DENT/SCRATCHES": 0,
        "UNDERCARRIAGE": 0,
        "MISC": 0,
        '': 0
    }
    for damage in damage_type_list:
        if damage.text in damage_type_dict:
            damage_type_dict[damage.text] += 1
        elif damage.text not in damage_type_dict:
            damage_type_dict['MISC'] += 1
        else:
            damage_type_dict[damage.text] = 1
    print(damage_type_dict)
