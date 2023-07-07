from pages.text_box_page import TextBox
def test_text_box_submit(browser):
    textbox = TextBox(browser)
    textbox.visit()
    assert textbox.submit.check_css('color', 'rgba(255, 255, 255, 1)')
