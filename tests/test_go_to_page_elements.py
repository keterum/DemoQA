from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
def test_page_elements(browser):
    demo_page = DemoQa(browser)
    demo_page.visit()
    assert demo_page.equal_url()
    demo_page.click_on_the_btn_elements()
    elements_page = ElementsPage(browser)
    assert elements_page.equal_url()