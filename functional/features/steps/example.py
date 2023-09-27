import time
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from settings import HOST_URL, PAGES_DICT

# Locator Map
BIKE_LIGHT_BUTTON = (By.XPATH, '//*[contains(text(), "Sauce Labs Bike Light")]/ancestor::div[contains(@class, "inventory_item")]/div[contains(@class, "pricebar")]//button')
CART_BADGE = (By.CSS_SELECTOR, '.shopping_cart_badge')
SORT_SELECTOR = (By.CSS_SELECTOR, 'select.product_sort_container')


@step('I type in "{thing}"')
def step_impl(context, thing):
    el = context.driver.find_element(*SEARCH_FIELD_SELECTOR)
    el.send_keys(thing)
    el.send_keys(Keys.ENTER)


@step('the results should contain "{word}"')
def step_impl(context, word):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.visibility_of_element_located(RESULTS_WAIT))
    el = context.driver.find_element(*RESULTS_ASSERTION)
    assert word in el.text, "Did not get expected text, instead:\n%s" % (
        el.text
    )

@step('I Click the Bike Light Add to Cart Button')
def step_impl(context):
    context.current_element = context.driver.find_element(*BIKE_LIGHT_BUTTON)
    context.current_element.click()

@then('the button should contain the Text "{text}"')
def step_impl(context, text):
    context.current_element = context.driver.find_element(*BIKE_LIGHT_BUTTON)
    assert context.current_element.text == text, "Expected {expected}, got {found}".format(
        expected=text,
        found=context.current_element.text
    )

@step('the cart badge displays "{num}"')
def step_impl(context, num):
    context.current_element = context.driver.find_element(*CART_BADGE)
    assert context.current_element.text == num, "Expected {expected}, got {found}".format(
        expected=num,
        found=context.current_element.text
    )

@then('the cart badge should not be present')
def step_impl(context):
    cart_badges = context.driver.find_elements(*CART_BADGE)
    assert len(cart_badges) == 0, "Cart badge was present"


@step('I select "{text}" from the sort selector')
def step_impl(context, text):
    selector = Select(context.driver.find_element(*SORT_SELECTOR))
    selector.select_by_visible_text(text)

@step('item "{num}" shold be "{text}"')
def step_impl(context, num, text):
    xpath_selector = '//div[contains(@class, "inventory_item")][' + num + ']'
    context.current_item = context.driver.find_element(By.XPATH, xpath_selector)
    context.current_item_title = context.current_item.find_element(By.CSS_SELECTOR, ".inventory_item_name")
    assert context.current_item_title.text == text, "Expected {expected}, got {found}".format(
        expected=text,
        found=context.current_item_title.text
    )
