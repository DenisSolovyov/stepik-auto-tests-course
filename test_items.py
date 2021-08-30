import time
from selenium import webdriver


def test_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(5)
    button = browser.find_elements_by_css_selector("#add_to_basket_form > button")
    assert button != [], "Кнопка не найдена"
    time.sleep(5)
