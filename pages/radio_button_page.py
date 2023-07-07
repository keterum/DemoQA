from pages.base_page import BasePage
from components.components import WebElement

class RadioButton(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/radio-button'
        super().__init__(driver, self.base_url)
        self.btn_yes = WebElement(driver, '#yesRadio')
        self.btn_impressive = WebElement(driver, '#impressiveRadio')
        self.btn_no = WebElement(driver, '#noRadio')
        self.text_selected = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div:nth-child(2) > p > span')

