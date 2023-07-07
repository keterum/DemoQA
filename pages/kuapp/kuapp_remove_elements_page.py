from components.components import WebElement
from pages.base_page import BasePage


class RemoveElements(BasePage):
    def __init__(self, driver):
        self.base_url = 'http://the-internet.herokuapp.com/add_remove_elements/'
        super().__init__(driver, self.base_url)
        self.btn_add = WebElement(driver, '#content > div > button')
        self.btns_delete = WebElement(driver, '#elements > button')

        # self.btns_delete = WebElement(driver, '//*[@id="elements"]/button')
        # self.btn_delete_2 = WebElement(driver, '# elements > button:nth-child(2)')
        # self.btn_delete_3 = WebElement(driver, '# elements > button:nth-child(3)')
        # self.btn_delete_4 = WebElement(driver, '# elements > button:nth-child(4)')