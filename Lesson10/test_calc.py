import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages_lesson10.test_Calc_first_step import FirstStep
from pages_lesson10.test_Calc_second_step import SecondStep

browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))
#browser = webdriver.Chrome(ChromeDriverManager().install())

@allure.epic("HW10. Allure practice")
@allure.severity("blocker")
@allure.story("Call calculator")
@allure.title("Testing Calculator Operation")

def test_calc():
    #browser = webdriver.Chrome()
    
    with allure.step("Step1: Settting the working time of calculator!!!"):
        first_step = FirstStep(browser)
        to_be1 = first_step.field_wait(browser)

    with allure.step("Step 2: input 7+8"):
        second_step = SecondStep(browser)
        to_be = second_step.calc_input(browser)

    assert to_be == "15"

    browser.quit()
