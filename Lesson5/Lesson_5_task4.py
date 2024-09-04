# from time import sleep # импортировали метод из пакета
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get('http://the-internet.herokuapp.com/entry_ad')

# print ("1")
wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable(
(By.CSS_SELECTOR, ".modal-footer")))
# print ("2")
button.click()
print("OK")
driver.quit()

# firefox
# О Модальное окно
# Откройте страницу http://the-internet.herokuapp.com/entry_ad.
# В модальном окне нажмите на кнопку Сlose