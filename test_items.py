import time
link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_add_to_cart(browser):
    browser.get(link)
    button = len(browser.find_elements_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket"))
    assert button > 0, 'Button not found'
