# import pytest
# from pylenium import Pylenium
#
#
# @pytest.fixture
# def copart(py) -> Pylenium:
#     py.visit('https://www.copart.com')
#     return py


import pytest


@pytest.fixture
def copart(py):
    py.visit('https://www.copart.com')
    return py
