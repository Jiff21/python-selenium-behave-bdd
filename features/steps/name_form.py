''' Step definition for check_once.feature'''
# pylint: disable=missing-function-docstring,attribute-defined-outside-init,consider-using-f-string,too-many-public-methods,function-redefined
from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

FIRST_NAME_FIELD = (By.CSS_SELECTOR, 'input[placeholder="First Name"]')
LAST_NAME_FIELD = (By.CSS_SELECTOR, 'input[placeholder="Last Name"]')
ZIP_CODE_FIELD = (By.CSS_SELECTOR, 'input[placeholder="Zip/Postal Code"]')


@step('I enter "{name}" into the first name field')
def first_name(context, name):
    wait = WebDriverWait(context.driver, 10, 0.1)
    wait.until(EC.element_to_be_clickable(FIRST_NAME_FIELD)).send_keys(name)


@step('I enter "{name}" into the last name field')
def last_name(context, name):
    context.driver.find_element(*LAST_NAME_FIELD).send_keys(name)


@step('I enter "{zippy}" into the zip code field')
def zip_code(context, zippy):
    context.current_element = context.driver.find_element(*ZIP_CODE_FIELD)
    context.current_element.send_keys(zippy)
