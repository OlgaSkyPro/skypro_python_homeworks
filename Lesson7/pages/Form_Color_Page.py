from selenium.webdriver.common.by import By


class FormColorPage:
    def __init__(self, browser):
        self.driver = browser

    def empty_field(self, browser):
        zip_cod_color = browser.find_element(By.CSS_SELECTOR, "#zip-code.alert.py-2.alert-danger")
        empty_rez = zip_cod_color.is_displayed()
        return empty_rez

    def filled_field_name(self, browser):
        field_name_color = browser.find_element(By.CSS_SELECTOR, "#first-name.alert.py-2.alert-success")
        filled_rez = field_name_color.is_displayed()
        return filled_rez

    def filled_field_last_name(self, browser):
        field_last_name_color = browser.find_element(By.CSS_SELECTOR, "#last-name.alert.py-2.alert-success")
        filled_rez = field_last_name_color.is_displayed()
        return filled_rez

    def filled_field_address(self, browser):
        field_address_color = browser.find_element(By.CSS_SELECTOR, "#address.alert.py-2.alert-success")
        filled_rez = field_address_color.is_displayed()
        return filled_rez

    def filled_field_city(self, browser):
        field_city_color = browser.find_element(By.CSS_SELECTOR, "#city.alert.py-2.alert-success")
        filled_rez = field_city_color.is_displayed()
        return filled_rez

    def filled_field_country(self, browser):
        field_country_color = browser.find_element(By.CSS_SELECTOR, "#country.alert.py-2.alert-success")
        filled_rez = field_country_color.is_displayed()
        return filled_rez

    def filled_field_email(self, browser):
        field_email_color = browser.find_element(By.CSS_SELECTOR, "#e-mail.alert.py-2.alert-success")
        filled_rez = field_email_color.is_displayed()
        return filled_rez

    def filled_field_phone(self, browser):
        field_phone_color = browser.find_element(By.CSS_SELECTOR, "#phone.alert.py-2.alert-success")
        filled_rez = field_phone_color.is_displayed()
        return filled_rez

    def filled_field_job(self, browser):
        field_job_color = browser.find_element(By.CSS_SELECTOR, "#job-position.alert.py-2.alert-success")
        filled_rez = field_job_color.is_displayed()
        return filled_rez

    def filled_field_company(self, browser):
        field_company_color = browser.find_element(By.CSS_SELECTOR, "#company.alert.py-2.alert-success")
        filled_rez = field_company_color.is_displayed()
        return filled_rez
