from selenium.webdriver.common.by import By
import time

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_guest_should_see_cart_button(browser):
    browser.get(link)
    time.sleep(30)

    cart = len(browser.find_elements(By.CSS_SELECTOR, "[class='btn btn-lg btn-primary btn-add-to-basket']"))
    assert cart == 1, f"No cart button"

