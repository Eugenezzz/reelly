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


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    # OTHER BROWSERS #
    # service = FirefoxService(GeckoDriverManager().install())
    # context.driver = webdriver.Firefox(service=service)
    # context.driver = webdriver.Safari()

    # HEADLESS MODE #
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless=new')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    # BROWSERSTACK #
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    bs_user = 'your_user'
    bs_key = 'your_key'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
        # 'os': 'Windows',
        # 'osVersion': '10',
        # 'browserName': 'Firefox',
        # 'sessionName': scenario_name

        'os': 'OS X',
        'osVersion': 'Big Sur',
        'browserName': 'Firefox',
        'sessionName': scenario_name
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    # HEADED MODE #
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    context.driver.maximize_window()

    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 15)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)

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
