from selenium.webdriver.common.by import By


class ShopLogin:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")

    def shop_login(self, driver):
        input_field_name = driver.find_element(By.CSS_SELECTOR, 'input[name="user-name"]')
        input_field_name.send_keys("standard_user")
        input_field_name.click()

        input_field_password = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
        input_field_password.send_keys("secret_sauce")
        input_field_password.click()

        input_field_input = driver.find_element(By.CSS_SELECTOR, 'input[name="login-button"]')
        input_field_input.click()

        driver.find_element(By.TAG_NAME, "button").click()
