''' Steps for the login page '''
# pylint: disable=missing-function-docstring,attribute-defined-outside-init,consider-using-f-string,too-many-public-methods,function-redefined,unused-import
from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from settings import HOST_URL, PAGES_DICT

# Locator Map
USERNAME_LOCATOR = (By.ID, 'user-name')
PASSWORD_LOCATOR = (By.ID, 'password')
LOGIN_BUTTON = (By.ID, 'login-button')
VALIDATIOR_ERROR = (By.CSS_SELECTOR, '.error-button')
ERROR_MESSAGE = (By.XPATH, '//*[@data-test="error"]')


@step('I click on the Username field')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    context.current_element = wait.until(EC.visibility_of_element_located(USERNAME_LOCATOR))
    context.current_element.click()


@step('I click on the Password field')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    context.current_element = wait.until(EC.visibility_of_element_located(PASSWORD_LOCATOR))
    context.current_element.click()


@step('I click on the Login Button')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    context.current_element = wait.until(EC.visibility_of_element_located(LOGIN_BUTTON))
    context.current_element.click()


@step('there should be one validation error')
def step_impl(context):
    error_messages = context.driver.find_elements(*VALIDATIOR_ERROR)
    assert len(error_messages) > 0 and len(error_messages) < 2, 'Expected 1 validation error' \
        ', found {} error elements'.format(len(error_messages))


@step('the validation error should include "{string}"')
def step_impl(context, string):
    context.current_element = context.driver.find_element(*ERROR_MESSAGE)
    assert string in context.current_element.text, \
        'Expected "{expected}" to be error message, "{result}"'.format(
            expected=string,
            result=context.current_element.text
        )
