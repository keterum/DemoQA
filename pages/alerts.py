from components.components import WebElement
from pages.base_page import BasePage

class Alert(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/alerts'
        super().__init__(driver, self.base_url)
        self.albtn = WebElement(driver, '#alertButton')
        self.confbtn = WebElement(driver, '#confirmButton')
        self.promptbtn = WebElement(driver, '#promtButton')
        self.block_confirm_result = WebElement(driver, '#confirmResult')
        self.block_prompt_result = WebElement(driver, '#promptResult')
        # self.block_confirm_result = (driver, '#javascriptAlertsWrapper > div:nth-child(3) > div.col-md-6 > span.mr-3')
