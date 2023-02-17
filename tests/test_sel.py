import pytest
from application.selDriver import Sel_driver

driver = Sel_driver()

#def test_get_roulette_title():
#    result = driver.get_roulette_title()
#    assert result != ''


def test_get_website_title():
    result = driver.get_website_title("https://www.reddit.com/")
    assert result == "Reddit - Explorez sans limite"