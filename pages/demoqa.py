from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException

class DemoQa(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)
    def exist_icon(self):
        try:
            self.find_element(locator='#app > header > a')
        except NoSuchElementException:
            return False
        return True
    def click_on_the_icon(self):
        self.find_element('#app > header > a').click()

    def equal_url(self):
        if self.get_url() == self.base_url:
            return True
        return False

    def click_on_the_btn_elements(self):
        self.find_element('#app > div > div > div.home-body > div > div:nth-child(1) > div > div.avatar.mx-auto.white > svg').click()
