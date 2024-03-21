from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep

from app.application import Application


def browser_init(context):
    """
    :param context: Behave context
    """
    # OTHER BROWSERS #
    # service = FirefoxService("D:/Downloads/geckodriver-v0.34.0-win-aarch64/geckodriver.exe")
    service = FirefoxService(GeckoDriverManager().install())
    context.driver = webdriver.Firefox(service=service)
    # context.driver = webdriver.Safari()

    # HEADLESS MODE #
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless=new')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    # HEADED MODE #
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)
    context.app = Application(context.driver)

    context.driver.maximize_window()

    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 15)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)

    context.driver.get('https://soft.reelly.io/sign-in')
    context.driver.find_element(By.ID, 'email-2').send_keys("your_email")
    context.driver.find_element(By.ID, 'field').send_keys("your_password")
    context.driver.find_element(By.CSS_SELECTOR, ".login-button").click()


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
