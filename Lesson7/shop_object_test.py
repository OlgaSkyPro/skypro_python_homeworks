from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.Shop_login import ShopLogin
from pages.Shop_choice import ShopChoice
from pages.Shop_card import ShopCard

browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))


def shop():
    browser = webdriver.Chrome()
    shop_login = ShopLogin(browser)
    shop_choice = ShopLogin(browser)
    shop_card = ShopCard(browser)

    to_be = shop_card.finish()

    assert to_be == "Total: $58.29"

    browser.quit
