from time import sleep # импортировали метод из пакета
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/classattr")
sleep(2)
blu_button = driver.find_element(
By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]") 
blu_button.click()
driver.switch_to.alert.accept()
print("1")

blu_button = driver.find_element(
By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]") 
blu_button.click()
driver.switch_to.alert.accept()
print("2")

blu_button = driver.find_element(
By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]") 
blu_button.click()
driver.switch_to.alert.accept()
print("3")

driver.quit()

# Chrome
# Клик по кнопке с CSS-классом
# Откройте страницу http://uitestingplayground.com/classattr.
# Кликните на синюю кнопку.
# Запустите скрипт три раза подряд. Убедитесь, что он отработает одинаково.
