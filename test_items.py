import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_user_should_see_addtobasket_button(browser):
    browser.get(link)
    button = browser.find_elements_by_css_selector(".btn-add-to-basket")
   
    assert button, "Button was not found!"
    #time.sleep(30)
