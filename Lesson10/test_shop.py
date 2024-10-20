from time import sleep
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages_lesson10.test_Shop_login import ShopLogin
from pages_lesson10.test_Shop_choice import ShopChoice
from pages_lesson10.test_Shop_card import ShopCard

browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))


@allure.epic("HW10")
@allure.severity("blocker")
@allure.story("Shopping")
@allure.feature("method shop")
@allure.title("Shop")

def test_shop():
    #browser = webdriver.Chrome()
    with allure.step("Login"):
        shop_login = ShopLogin(browser)
    
    with allure.step("Choice"):
        shop_choice = ShopChoice(browser)
    
    with allure.step("Card"):
        shop_card = ShopCard(browser)

    to_be = shop_card.finish()

    assert to_be == "Total: $58.29"

    browser.quit()
