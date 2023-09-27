import requests
import time
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from settings import HOST_URL, PAGES_DICT

# Locator Map
BIKE_LIGHT_BUTTON = (By.XPATH, '//*[contains(text(), "Sauce Labs Bike Light")]/ancestor::div[contains(@class, "inventory_item")]/div[contains(@class, "pricebar")]//button')
CART_BADGE = (By.CSS_SELECTOR, '.shopping_cart_badge')
SUBMIT_BUTTON = (By.XPATH, '//center/input[@name="btnK"]')
RESULTS_WAIT = (By.ID, 'cnt')
RESULTS_ASSERTION = (By.XPATH, '//*[@id="rso"]//a')


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
    assert context.current_element.text == num, "Expected {num}, got {text}".format(
        num=num,
        text=context.current_element.text
    )

@then('the cart badge should not be present')
def step_impl(context):
    cart_badges = context.driver.find_elements(*CART_BADGE)
    import time; time.sleep(2)
    assert len(cart_badges) == 0, "Cart badge was present"
    



    


