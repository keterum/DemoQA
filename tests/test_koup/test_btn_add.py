from pages.kuapp.kuapp import Kuapp
from pages.kuapp.kuapp import RemoveElements
import time

def test_kuapp(browser):
    kuapp = Kuapp(browser)
    remove_elements = RemoveElements(browser)
    kuapp.visit()
    time.sleep(2)
    assert kuapp.icon.get_text() == 'Add/Remove Elements'
    kuapp.icon.click()
    time.sleep(3)
    assert remove_elements.equal_url()
    assert remove_elements.btn_add.exist()

    for i in range(4):
        remove_elements.btn_add.click()
    time.sleep(3)
    assert remove_elements.btns_delete.check_count_elements(4)

    for element in remove_elements.btns_delete.find_elements():
        assert element.text == 'Delete'

    while remove_elements.btns_delete.exist():
        remove_elements.btns_delete.click()

    time.sleep(3)
    assert not remove_elements.btns_delete.exist()
