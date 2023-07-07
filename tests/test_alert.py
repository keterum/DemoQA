from pages.alerts import Alert
import time

def test_alert(browser):
    window_alert = Alert(browser)
    window_alert.visit()
    assert not window_alert.alert()
    window_alert.albtn.click()
    time.sleep(2)
    assert window_alert.alert()
    window_alert.alert().accept()


def test_alert_text(browser):
    window_a = Alert(browser)
    window_a.visit()
    window_a.albtn.click()
    time.sleep(2)
    assert window_a.alert().text == 'You clicked a button'
    window_a.alert().accept()
    assert not window_a.alert()


def test_confirm(browser):
    win_a = Alert(browser)
    win_a.visit()
    win_a.confbtn.click()
    time.sleep(2)
    win_a.alert().dismiss()
    assert win_a.block_confirm_result.get_text() == 'You selected Cancel'


def test_prompt(browser):
    win_a = Alert(browser)
    win_a.visit()
    win_a.promptbtn.click()
    time.sleep(2)
    name = "Grogu"
    win_a.alert().send_keys(name)
    win_a.alert().accept()
    assert win_a.block_prompt_result.get_text() == 'You entered Grogu'

