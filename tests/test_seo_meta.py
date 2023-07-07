from pages.demoqa import DemoQa
from pages.alerts import Alert
from pages.browser_tab import BrowserTab
import time
import pytest

@pytest.mark.parametrize("pages", [Alert, DemoQa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert page.metaView.get_dom_attribute('name') == "viewport"
    assert page.metaView.get_dom_attribute('content') == "width=device-width,initial-scale=1"

