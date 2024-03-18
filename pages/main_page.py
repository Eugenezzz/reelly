from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class MainPage(Page):
    SETTINGS_BTN = (By.CSS_SELECTOR, '.menu_block_1 .w-layout-grid [href="/settings"]')


    def open_main(self):
        self.open_url('https://soft.reelly.io/')

    def click_settings(self):
        self.click(*self.SETTINGS_BTN)