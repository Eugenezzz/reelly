from pages.base_page import Page

from selenium.webdriver.common.by import By
from time import sleep


class SettingsPage(Page):
    SUBSCRIPTION_BTN = (By.CSS_SELECTOR, '.settings-block-menu [href="/subscription"]')

    def click_subscription(self):
        sleep(5)
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.click(*self.SUBSCRIPTION_BTN)