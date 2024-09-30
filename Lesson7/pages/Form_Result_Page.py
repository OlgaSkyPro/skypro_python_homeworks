from selenium.webdriver.common.by import By


class FormResultPage:

    def __init__(self, browser):
        self.driver = browser

    def fill_fields(self, browser):
        browser.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys("Иван")
        browser.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys("Петров")
        browser.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys("Ленина, 55-3")
        browser.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys("Москва")
        browser.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys("Россия")
        browser.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys("test@skypro.com")
        browser.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys("+7985899998787")
        browser.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys("QA")
        browser.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys("SkyPro")

        submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()
