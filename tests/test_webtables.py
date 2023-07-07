from pages.webtables_page import WebTables
def test_tables(browser):
    web_tables = WebTables(browser)
    web_tables.visit()
    assert not web_tables.no_rows_found.exist()
    while web_tables.btns_delete.exist():
        web_tables.btns_delete.click()
    assert web_tables.no_rows_found.exist()
