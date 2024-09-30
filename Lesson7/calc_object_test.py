from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.Calc_first_step import FirstStep
from pages.Calc_second_step import SecondStep

browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))


def calc():
    browser = webdriver.Chrome()
    first_step = FirstStep(browser)
    second_step = SecondStep(browser)
    to_be = second_step.calc_input(browser)

    assert to_be == "15"

    browser.quit()
