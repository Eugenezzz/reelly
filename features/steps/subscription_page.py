from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


SUBSCRIPTION_TITLE = (By.CSS_SELECTOR, '.lotion-your-h3--price')
UPGRADE_PLAN_BTN = (By.CSS_SELECTOR, '[wized="upgradePlanButton"]')
BACK_BTN = (By.CSS_SELECTOR, '.verify-step-block [href="/settings"]')

@then('Verify the Subscription page opens')
def verify_subscription_page_url(context):
    expected_partial_url = "subscription"
    context.app.page.verify_partial_url(expected_partial_url)


@then('Verify title “Subscription & payments” is visible')
def verify_subscription_title_present(context):
    expected_text = "Subscription & payments"
    context.app.page.verify_text(expected_text, *SUBSCRIPTION_TITLE)


@then('Verify “Upgrade plan” button is available')
def verify_back_btn_present(context):
    expected_text = "Upgrade plan"
    context.app.page.verify_text(expected_text, *UPGRADE_PLAN_BTN)


@then('Verify “Back” button is available')
def verify_back_btn_present(context):
    expected_text = "<- Back"
    context.app.page.verify_text(expected_text, *BACK_BTN)