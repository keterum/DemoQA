from components.components import WebElement
from pages.base_page import BasePage

class WebTables(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)
        self.no_rows_found = WebElement(driver, 'div.rt-noData')
        self.btns_delete = WebElement(driver, '[title="Delete"]')