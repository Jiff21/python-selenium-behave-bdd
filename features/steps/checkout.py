''' Step definition for check_once.feature'''
# pylint: disable=missing-function-docstring,attribute-defined-outside-init,consider-using-f-string,too-many-public-methods,function-redefined
import re
from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from workarounds import SessionStorage
from selenium.webdriver.common.action_chains import ActionChains


CHECKOUT_BODY = (By.ID, 'checkout_summary_container')
CHECKOUT_CART_ITEM = (By.CSS_SELECTOR, '.cart_item')
CHECKOUT_INFO_SUBMIT = (By.XPATH, '//*[@type="submit"]')
CHECKOUT_INFO_VALIDATION_MESSAGE =  (By.XPATH, '//*[@data-test="error"]')
CHECKOUT_FINISH_BUTTON = (By.LINK_TEXT, 'FINISH')
CHECKOUT_FIRST_NAME = (By.ID, 'first-name')
CHECKOUT_LAST_NAME = (By.ID, 'last-name')
CHECKOUT_SUBTOTAL = (By.CSS_SELECTOR, '.summary_subtotal_label')
CHECKOUT_TAX = (By.CSS_SELECTOR, '.summary_tax_label')
CHECKOUT_TOTAL = (By.CSS_SELECTOR, '.summary_total_label')
CHECKOUT_ZIP_CODE = (By.ID, 'postal-code')


@step('I wait for the checkout summary to load')
def step_impl(context):
    context.wait.until(EC.presence_of_element_located(CHECKOUT_BODY))


@step('I wait for at least one cart item to load')
def step_impl(context):
    context.wait.until(EC.presence_of_element_located(CHECKOUT_CART_ITEM))


@step('the subtotal should be "{expected_total}"')
def step_impl(context, expected_total):
    context.current_element = context.wait.until(EC.visibility_of_element_located(CHECKOUT_SUBTOTAL))
    price = re.findall(r'\$.*', context.current_element.text)[0]
    assert expected_total == price, 'Expected {expected_total}, but got {total}'.format(
        expected_total=expected_total,
        total=price
    )


@step('the tax should be "{expected_total}"')
def step_impl(context, expected_total):
    context.current_element = context.wait.until(EC.visibility_of_element_located(CHECKOUT_TAX))
    price = re.findall(r'\$.*', context.current_element.text)[0]
    assert expected_total == price, 'Expected {expected_total}, but got {total}'.format(
        expected_total=expected_total,
        total=price
    )


@step('the total should be "{expected_total}"')
def step_impl(context, expected_total):
    context.current_element = context.wait.until(EC.visibility_of_element_located(CHECKOUT_TOTAL))
    price = re.findall(r'\$.*', context.current_element.text)[0]
    assert expected_total == price, 'Expected {expected_total}, but got {total}'.format(
        expected_total=expected_total,
        total=price
    )


@step('I fill up the cart with all items')
def step_impl(context):
    session = SessionStorage(context.driver, 'cart-contents', '[0, 1, 2, 3, 4, 5]')
    session.set()


@step('I click the finish button')
def step_impl(context):
    context.current_element = context.wait.until(EC.element_to_be_clickable(CHECKOUT_FINISH_BUTTON))
    context.current_element.click()


@step('I type "{text}" into the checkout first name field')
def step_impl(context, text):
    context.current_element = context.wait.until(EC.element_to_be_clickable(CHECKOUT_FIRST_NAME))
    context.current_element.send_keys(text)


@step('I type "{text}" into the checkout last name field')
def step_impl(context, text):
    context.current_element = context.wait.until(EC.element_to_be_clickable(CHECKOUT_LAST_NAME))
    context.current_element.send_keys(text)


@step('I type "{text}" into the checkout zip code field')
def step_impl(context, text):
    wait = WebDriverWait(context.driver, 15, 0.1)
    context.current_element = wait.until(EC.element_to_be_clickable(CHECKOUT_ZIP_CODE))
    context.current_element.send_keys(text)


@step('I click the continue button on the checkout info page')
def step_impl(context):
    context.current_element = context.wait.until(EC.element_to_be_clickable(CHECKOUT_INFO_SUBMIT))
    context.current_element.click()


@step('the checkout info pages shows one validation error')
def step_impl(context):
    error_messages = context.driver.find_elements(*CHECKOUT_INFO_VALIDATION_MESSAGE)
    assert len(error_messages) > 0 and len(error_messages) < 2, 'Expected 1 validation error' \
        ', found {} error elements'.format(len(error_messages))


@step('the checkout info pages validation error should include "{string}"')
def step_impl(context, string):
    context.current_element = context.driver.find_element(*CHECKOUT_INFO_VALIDATION_MESSAGE)
    assert string in context.current_element.text, \
        'Expected "{expected}" to be error message, "{result}"'.format(
            expected=string,
            result=context.current_element.text
        )
