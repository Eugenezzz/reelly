from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


HEADER = (By.CSS_SELECTOR, '.h1-menu')


@given('Open the Main page and verify the "Main menu" header is present')
def verify_header_preset(context):
    context.driver.find_element(*HEADER)
    sleep(3)


@when('Click on Settings option')
def click_settings(context):
    context.app.main_page.click_settings()
    sleep(3)
