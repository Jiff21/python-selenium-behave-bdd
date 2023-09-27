import time
from behave import given, when, then
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
