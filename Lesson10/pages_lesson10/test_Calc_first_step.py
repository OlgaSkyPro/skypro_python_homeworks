from selenium.webdriver.common.by import By
import allure

class FirstStep:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get(" https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    @allure.step("Fill in the Time field = 10")
    def field_wait(self, driver):
        input_field = driver.find_element(By.CSS_SELECTOR, '#delay')
        input_field.clear()
        input_field.send_keys(10)
