''' Step definition for check_once.feature'''
# pylint: disable=missing-function-docstring,attribute-defined-outside-init,consider-using-f-string,too-many-public-methods,function-redefined
import re
from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


CHECKOUT_BODY = (By.ID, 'checkout_summary_container')
CHECKOUT_SUBTOTAL = (By.CSS_SELECTOR, '.summary_subtotal_label')
CHECKOUT_TAX = (By.CSS_SELECTOR, '.summary_tax_label')
CHECKOUT_TOTAL = (By.CSS_SELECTOR, '.summary_total_label')


@step('I wait for the checkout summary to load')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10, 0.1)
    wait.until(EC.presence_of_element_located(CHECKOUT_BODY))


@step('the subtotal should be "{expected_total}"')
def step_impl(context, expected_total):
    wait = WebDriverWait(context.driver, 10, 0.1)
    context.current_element = wait.until(EC.visibility_of_element_located(CHECKOUT_SUBTOTAL))
    price = re.findall(r'\$.*', context.current_element.text)[0]
    assert expected_total == price, 'Expected {expected_total}, but got {total}'.format(
        expected_total=expected_total,
        total=price
    )


@step('the tax should be "{expected_total}"')
def step_impl(context, expected_total):
    wait = WebDriverWait(context.driver, 10, 0.1)
    context.current_element = wait.until(EC.visibility_of_element_located(CHECKOUT_TAX))
    price = re.findall(r'\$.*', context.current_element.text)[0]
    assert expected_total == price, 'Expected {expected_total}, but got {total}'.format(
        expected_total=expected_total,
        total=price
    )

@step('the total should be "{expected_total}"')
def step_impl(context, expected_total):
    wait = WebDriverWait(context.driver, 10, 0.1)
    context.current_element = wait.until(EC.visibility_of_element_located(CHECKOUT_TOTAL))
    price = re.findall(r'\$.*', context.current_element.text)[0]
    assert expected_total == price, 'Expected {expected_total}, but got {total}'.format(
        expected_total=expected_total,
        total=price
    )
