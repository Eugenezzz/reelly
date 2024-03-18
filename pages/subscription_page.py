from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class SubscriptionPage(Page):
    SUBSCRIPTION_URL = "https://soft.reelly.io/subscription"
    SUBSCRIPTION_TITLE = (By.CSS_SELECTOR, '.lotion-your-h3--price')
    UPGRADE_PLAN_BTN = (By.CSS_SELECTOR, '[wized="upgradePlanButton"]')
    BACK_BTN = (By.CSS_SELECTOR, '.verify-step-block [href="/settings"]')
