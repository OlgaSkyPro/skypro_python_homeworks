from time import sleep # импортировали метод из пакета
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/dynamicid")
sleep(2)
blu_button = driver.find_element(
By.XPATH, '//button[text()="Button with Dynamic ID"]').click()
print("1")

blu_button = driver.find_element(
By.XPATH, '//button[text()="Button with Dynamic ID"]').click()
print("2")

blu_button = driver.find_element(
By.XPATH, '//button[text()="Button with Dynamic ID"]').click()
print("3")

driver.quit()

# Chrome
# Клик по кнопке без ID
# Откройте страницу http://uitestingplayground.com/dynamicid.
# Кликните на синюю кнопку.
# Запустите скрипт три раза подряд. Убедитесь, что он отработает одинаково.
