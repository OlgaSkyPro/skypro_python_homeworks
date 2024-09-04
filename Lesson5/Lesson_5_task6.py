from time import sleep # импортировали метод из пакета
from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get('http://the-internet.herokuapp.com/login')
# sleep (2)
name_input = driver.find_element(By.ID, "username")
name_input.send_keys("tomsmith")
sleep(2)
password_input = driver.find_element(By.ID, "password")
password_input.send_keys("SuperSecretPassword!")
sleep(2)
button = driver.find_element(
By.TAG_NAME, "button").click()
print("OK")
driver.quit()

# firefox
# Форма авторизации
# Откройте страницу http://the-internet.herokuapp.com/login.
# В поле username введите значение tomsmith
# В поле password введите значение SuperSecretPassword!
# Нажмите кнопку Login
