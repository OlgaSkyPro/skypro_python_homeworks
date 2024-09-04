from time import sleep # импортировали метод из пакета
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

for i in range(5):
    click_botton = driver.find_element(
By.CSS_SELECTOR, ("[onclick='addElement()']")).click()
sleep(2)
delete_buttons = driver.find_elements(
By.XPATH, "//button[@onclick='deleteElement()']")

print(f"Размер списка {len(delete_buttons)}")

driver.quit()

# sleep (5)

# Chrome
# Откройте страницу http://the-internet.herokuapp.com/add_remove_elements/.
# Пять раз кликните на кнопку Add Element
# Соберите со страницы список кнопок Delete
# Выведите на экран размер списка.