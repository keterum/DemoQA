from pages.demoqa import DemoQa
from pages.radio_button_page import RadioButton
import time
import pytest


def test_decor_5(browser):
    demoqa = DemoQa(browser)
    demoqa.visit()
    time.sleep(2)
    assert demoqa.headers_5.check_count_elements(6)
    for element in demoqa.headers_5.find_elements():
        assert element.text != ''


# @pytest.mark.skipif(True, reason='захотелось')
def test_decor_5(browser):
    radiopage = RadioButton(browser)
    radiopage.visit()

    radiopage.btn_yes.click()
    assert radiopage.text_selected.get_text() == 'Yes'
    time.sleep(2)

    radiopage.btn_impressive.click()
    assert radiopage.text_selected.get_text() == 'Impressive'
    time.sleep(2)

    assert 'disabled' in radiopage.btn_no.get_dom_attribute('class')

    # if radiopage.btn_yes

    # assert demoqa.headers_5.check_count_elements(6)
    # for element in demoqa.headers_5.find_elements():
    #     assert element.text != ''


def test_decor_1(browser):
    radio = RadioButton(browser)
    if not radio.code_status()
        pytest.skip(reason=f"Страница {radio.base_url} недоступна")
    radio.visit()

    radio.btn_yes.click_force()
    assert radio.text_selected.get_text() == 'Yes'

    radio.btn_impressive.click()
    assert radio.text_selected.get_text() == 'Impressive'
    time.sleep(2)

    assert 'disabled' in radio.btn_no.get_dom_attribute('class')