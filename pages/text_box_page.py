from components.components import WebElement
from pages.base_page import BasePage

class TextBox(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)
        self.submit = WebElement(driver, '#submit')