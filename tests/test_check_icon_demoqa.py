# from selenium import webdriver
# from selenium.webdriver.common.by import By
from pages.demoqa import DemoQa

def test_enter(browser):
    demo_page = DemoQa(browser)
    demo_page.visit()
    demo_page.icon.click()
    assert demo_page.equal_url()
    assert demo_page.icon.exist()



    # browser.get('https://demoqa.com/')
    # link = browser.find_element(By.CSS_SELECTOR, '#app > header > a')
    # if link is None:
    #     print("Элемент не найден")
    # else:
    #     print("Элемент найден")
