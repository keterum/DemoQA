import pytest

# pytest .\tests\test_decor_mark.py -m smoke
@pytest.mark.smoke
def test_first(browser):
    assert True
@pytest.mark.regress
def test_second(browser):
    assert True

@pytest.mark.regress
def test_third(browser):
    assert True

@pytest.mark.regress
def test_fourth(browser):
    assert True
