import allure
from selenium.webdriver.common.by import By

@allure.story("Browser form")

class FormOpenPage:

    def __init__(self, browser):
        self._driver = browser
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    @allure.step("Open form")     
    def fille_field(self):
        self._driver.filling_form()
