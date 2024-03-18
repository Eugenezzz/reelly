from selenium.webdriver.common.by import By

from pages.base_page import Page


class SettingsPage(Page):
    SUBSCRIPTION_BTN = (By.CSS_SELECTOR, '.settings-block-menu [href="/subscription"]')


    def click_subscription(self):
        self.click(*self.SUBSCRIPTION_BTN)