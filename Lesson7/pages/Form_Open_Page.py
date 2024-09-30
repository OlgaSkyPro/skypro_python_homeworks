from selenium.webdriver.common.by import By


class FormOpenPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def fille_field(self):
        self._driver.filling_form()
