from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

input_field_name = driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]')
input_field_name.send_keys("Иван")

input_field_last_name = driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]')
input_field_last_name.send_keys("Петров")

input_field_address = driver.find_element(By.CSS_SELECTOR, 'input[name="address"]')
input_field_address.send_keys("Ленина, 55-3")

input_field_city = driver.find_element(By.CSS_SELECTOR, 'input[name="city"]')
input_field_city.send_keys("Москва")

input_field_country = driver.find_element(By.CSS_SELECTOR, 'input[name="country"]')
input_field_country.send_keys("Россия")

input_field_email = driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]')
input_field_email.send_keys("test@skypro.com")

input_field_phone = driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]')
input_field_phone.send_keys("+7985899998787")

input_field_job = driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]')
input_field_job.send_keys("QA")

input_field_company = driver.find_element(By.CSS_SELECTOR, 'input[name="company"]')
input_field_company.send_keys("SkyPro")

submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
submit_button.click()

zip_cod_color = driver.find_element(By.CSS_SELECTOR, "#zip-code.alert.py-2.alert-danger")
assert zip_cod_color.is_displayed()

field_name_color = driver.find_element(By.CSS_SELECTOR, "#first-name.alert.py-2.alert-success")
assert field_name_color.is_displayed()

field_last_name_color = driver.find_element(By.CSS_SELECTOR, "#last-name.alert.py-2.alert-success")
assert field_last_name_color.is_displayed()

field_address_color = driver.find_element(By.CSS_SELECTOR, "#address.alert.py-2.alert-success")
assert field_address_color.is_displayed()

field_city_color = driver.find_element(By.CSS_SELECTOR, "#city.alert.py-2.alert-success")
assert field_city_color.is_displayed()

field_country_color = driver.find_element(By.CSS_SELECTOR, "#country.alert.py-2.alert-success")
assert field_country_color.is_displayed()

field_email_color = driver.find_element(By.CSS_SELECTOR, "#e-mail.alert.py-2.alert-success")
assert field_email_color.is_displayed()

field_phon_color = driver.find_element(By.CSS_SELECTOR, "#phone.alert.py-2.alert-success")
assert field_phon_color.is_displayed()

field_job_color = driver.find_element(By.CSS_SELECTOR, "#job-position.alert.py-2.alert-success")
assert field_job_color.is_displayed()

field_company_color = driver.find_element(By.CSS_SELECTOR, "#company.alert.py-2.alert-success")
assert field_company_color.is_displayed()

print("OK")
driver.quit()
