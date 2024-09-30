from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SecondStep:

    def __init__(self, browser):
        self.driver = browser

    def calc_input(self, browser):
        browser.find_element(By.XPATH, '//span[text()="7"]').click()
        browser.find_element(By.XPATH, '//span[text()="+"]').click()
        browser.find_element(By.XPATH, '//span[text()="8"]').click()
        browser.find_element(By.XPATH, '//span[text()="="]').click()

        wait = WebDriverWait(browser, 46).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))

        rezult = browser.find_element(By.CLASS_NAME, "screen").text
        return rezult
