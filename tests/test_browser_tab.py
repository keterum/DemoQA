from pages.browser_tab import BrowserTab
import time

def test_browser_tab(browser):
    tab = BrowserTab(browser)
    tab.visit()
    time.sleep(2)
    assert len(browser.window_handles) == 1
    tab.new_tab.click()
    time.sleep(2)
    assert len(browser.window_handles) == 2
    browser.switch_to.window(browser.window_handles[0])
    time.sleep(2)
