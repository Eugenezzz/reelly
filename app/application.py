from pages.base_page import Page
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.settings_page import SettingsPage
from pages.subscription_page import SubscriptionPage


class Application:

    def __init__(self, driver):
        self.page = Page(driver)

        self.login_page = LoginPage(driver)
        self.main_page = MainPage(driver)
        self.settings_page = SettingsPage(driver)
        self.subscription_page = SubscriptionPage(driver)