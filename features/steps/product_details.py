''' Step definition for check_once.feature'''
# pylint: disable=missing-function-docstring,attribute-defined-outside-init,consider-using-f-string,too-many-public-methods,function-redefined
import re
from behave import step, then
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


DETAILS_ADD_TO_CART = (By.CSS_SELECTOR, '.btn_inventory')
BACK_BUTTON = (By.CSS_SELECTOR, '.inventory_details_back_button')


@then('the header "{header}" should contain "{expected}"')
def get(context, expected, header):
    assert expected in context.response.headers[header], \
    'Expected {expected} to be in the response {header} headers'.format(
        expected = expected,
        header = header
    )


@then('the response should use https')
def get(context):
    regex = re.compile('^https:')
    assert regex.match(context.response.url), \
    'Expected the response to be on https, but got {url}'.format(
        url = context.response.url
    )


@then('the response url should include "{page_name}"')
def get(context, page_name):
    assert page_name in context.response.url, \
    'We the uri {expected}, to be included in {url}'.format(
        expected = page_name,
        url = context.response.url
    )


@step('I hover over the add to cart button')
def get(context):
    context.current_element = context.driver.find_element(*DETAILS_ADD_TO_CART)
    actions = ActionChains(context.driver)
    actions.move_to_element(context.current_element)
    actions.perform()


@step('I click the add to cart button')
def get(context):
    context.current_element = context.driver.find_element(*DETAILS_ADD_TO_CART)
    context.current_element.click()


@step('I click the back button')
def get(context):
    context.current_element = context.driver.find_element(*BACK_BUTTON)
    context.current_element.click()
