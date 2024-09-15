from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

input_field_name = driver.find_element(By.CSS_SELECTOR, 'input[name="user-name"]')
input_field_name.send_keys("standard_user")
sleep(2)
input_field_name.click()

input_field_password = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
input_field_password.send_keys("secret_sauce")
input_field_password.click()
sleep(2)

input_field_input = driver.find_element(By.CSS_SELECTOR, 'input[name="login-button"]')
input_field_input.click()
sleep(5)

driver.find_element(By.TAG_NAME, "button").click()

input_field_n1 = driver.find_element(By.CSS_SELECTOR,'[name="add-to-cart-sauce-labs-backpack"]')
input_field_n1.click()

input_field_n2 = driver.find_element(By.CSS_SELECTOR,'[name="add-to-cart-sauce-labs-bolt-t-shirt"]')
input_field_n2.click()

input_field_n3 = driver.find_element(By.CSS_SELECTOR,'[name="add-to-cart-sauce-labs-onesie"]')
input_field_n3.click()

input_field_bag = driver.find_element(By.CSS_SELECTOR,'[data-test="shopping-cart-link"]')
input_field_bag.click()

input_field_checkout = driver.find_element(By.CSS_SELECTOR,'[name="checkout"]')
input_field_checkout.click()

input_field_name = driver.find_element(By.CSS_SELECTOR, 'input[name="firstName"]')
input_field_name.send_keys("Иван")

input_last_name = driver.find_element(By.CSS_SELECTOR, 'input[name="lastName"]')
input_last_name.send_keys("Иванов")

input_field_index = driver.find_element(By.CSS_SELECTOR, 'input[name="postalCode"]')
input_field_index.send_keys("100100")

input_field_continue=driver.find_element(By.CSS_SELECTOR, '[name="continue"]')
input_field_continue.click()

total_price=driver.find_element(By.CSS_SELECTOR,'[data-test="total-label"]').text
assert total_price == "Total: $58.29"

print(total_price)
print("OK")

driver.quit()
