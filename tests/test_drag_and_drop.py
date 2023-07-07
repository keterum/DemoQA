from pages.droppable import Droppable
import time
from selenium.webdriver import ActionChains


def test_browser_tab(browser):
    able = Droppable(browser)
    action_chains = ActionChains(browser)
    able.visit()
    time.sleep(2)
    assert not able.drop.check_css('background-color', 'rgba(70, 130, 180, 1)')
    action_chains.drag_and_drop(able.drag.find_element(), able.drop.find_element()).perform()
    time.sleep(2)
    assert able.drop.check_css('background-color', 'rgba(70, 130, 180, 1)')
    action_chains.drag_and_drop_by_offset(able.drag.find_element(), -200, 0).perform()
    time.sleep(2)
    assert able.drop.check_css('background-color', 'rgba(70, 130, 180, 1)')
    