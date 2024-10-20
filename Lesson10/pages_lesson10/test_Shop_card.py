import allure
from selenium.webdriver.common.by import By


class ShopCard:
    def __init__(self, browser):
        self.driver = browser

    @allure.step("Fill out personal data for delivery")   
    def finish(self, browser):
        browser.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]').click()
        browser.find_element(By.CSS_SELECTOR, '[name="checkout"]').click()
        browser.find_element(By.CSS_SELECTOR, 'input[name="firstName"]').send_keys("Иван")
        browser.find_element(By.CSS_SELECTOR, 'input[name="lastName"]').send_keys("Иванов")
        browser.find_element(By.CSS_SELECTOR, 'input[name="postalCode"]').send_keys("100100")
        browser.find_element(By.CSS_SELECTOR, '[name="continue"]').click()

        total_price = browser.find_element(By.CSS_SELECTOR, '[data-test="total-label"]').text
        return total_price
