from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


driver = webdriver.Chrome()
driver.get(" https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

input_field = driver.find_element(By.CSS_SELECTOR, '#delay')
input_field.clear()
input_field.send_keys(45)

input_field_7 = driver.find_element(By.XPATH, '//span[text()="7"]')
input_field_7.click()

input_field_plus = driver.find_element(By.XPATH, '//span[text()="+"]')
input_field_plus.click()

input_field_8 = driver.find_element(By.XPATH, '//span[text()="8"]')
input_field_8.click()

input_field_equel = driver.find_element(By.XPATH, '//span[text()="="]')
input_field_equel.click()

wait = WebDriverWait(driver, 46).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))

rezult = driver.find_element(By.CLASS_NAME,"screen").text

assert rezult == "15"

print(rezult)
print("OK")

driver.quit()
