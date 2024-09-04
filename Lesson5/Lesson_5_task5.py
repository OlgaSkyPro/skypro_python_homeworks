from time import sleep # импортировали метод из пакета
from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get('http://the-internet.herokuapp.com/inputs')
# sleep (2)
input = driver.find_element(By.TAG_NAME, "input")
sleep(2)
input.send_keys("1000")
sleep(2)
input.clear()
sleep(2)
input.send_keys("999")
print("OK")
driver.quit()

# firefox
# Поле ввода
# Откройте страницу http://the-internet.herokuapp.com/inputs.
# Введите в поле текст 1000
# Очистите это поле (метод clear).
# Введите в это же поле текст 999