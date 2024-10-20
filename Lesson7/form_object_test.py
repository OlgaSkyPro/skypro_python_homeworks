from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.Form_Open_Page import FormOpenPage
from pages.Form_Result_Page import FormResultPage
from pages.Form_Color_Page import FormColorPage

browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))


def test_fill_form():

    browser = webdriver.Chrome()

    open_page = FormOpenPage(browser)

    result_page = FormResultPage(browser)
    
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
