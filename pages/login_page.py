from pages.base_page import Page

from selenium.webdriver.common.by import By


class LoginPage(Page):
    EMAIL_FIELD = (By.ID, 'email-2')
    PASSWORD_FIELD = (By.ID, 'field')
    LOGIN_BTN = (By.CSS_SELECTOR, ".login-button")