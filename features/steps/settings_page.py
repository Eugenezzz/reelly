from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


@when('Click on Subscription & payments option')
def click_subscription(context):
    context.app.settings_page.click_subscription()
