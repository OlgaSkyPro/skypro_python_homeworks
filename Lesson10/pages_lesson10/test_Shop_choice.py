import allure
from selenium.webdriver.common.by import By


class ShopChoice:
    def __init__(self, browser):
        self.driver = browser

    @allure.step("Selection of items for card")  
    def shop_choice(self, browser):
        browser.find_element(By.CSS_SELECTOR, '[name="add-to-cart-sauce-labs-backpack"]').click()
        browser.find_element(By.CSS_SELECTOR, '[name="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        browser.find_element(By.CSS_SELECTOR, '[name="add-to-cart-sauce-labs-onesie"]').click()
