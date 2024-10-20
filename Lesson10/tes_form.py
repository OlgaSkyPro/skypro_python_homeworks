import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages_lesson10.test_Form_Open_Page import FormOpenPage
from pages_lesson10.test_Form_Color_Page import FormColorPage
from pages_lesson10.test_Form_Result_Page import FormResultPage

browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))

@allure.epic("HW10")
@allure.severity("blocker")
@allure.story("Fill out the form")
@allure.feature("method form")
@allure.title("Form")

def test_fill_form():

    #browser = webdriver.Chrome()

    with allure.step("Open"):
        open_page = FormOpenPage(browser)
   
    with allure.step("validating form"):
        result_page = FormResultPage(browser)
   
    with allure.step("Color"):
        color_page = FormColorPage(browser)
        to_be1 = color_page.empty_field(browser)
        to_be2 = color_page.filled_field_name(browser)
        to_be3 = color_page.filled_field_last_name(browser)
        to_be4 = color_page.filled_field_address(browser)
        to_be5 = color_page.filled_field_city(browser)
        to_be6 = color_page.filled_field_country(browser)
        to_be7 = color_page.filled_field_email(browser)
        to_be8 = color_page.filled_field_phone(browser)
        to_be9 = color_page.filled_field_job(browser)
        to_be10 = color_page.filled_field_company(browser)

    assert to_be1 == True
    assert to_be2 == True
    assert to_be3 == True
    assert to_be4 == True
    assert to_be5 == True
    assert to_be6 == True
    assert to_be7 == True
    assert to_be8 == True
    assert to_be9 == True
    assert to_be10 == True

    browser.quit()
