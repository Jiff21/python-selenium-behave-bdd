''' Step definition for check_once.feature'''
# pylint: disable=missing-function-docstring,consider-using-f-string,function-redefined

from behave import step, then
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
# pylint: disable=unused-import
from name_form import first_name, last_name, zip_code

# Locator Map
BIKE_LIGHT_BUTTON = (
    By.XPATH,
    '//*[contains(text(), "Sauce Labs Bike Light")]/ancestor::div[contains'
    '(@class, "inventory_item")]/div[contains(@class, "pricebar")]//button'
)
TEST_ALL_TSHIRT = (
    By.XPATH,
    '//*[contains(text(), "Test.allTheThings() T-Shirt (Red)")]/ancestor::div[contains'
    '(@class, "inventory_item")]/div[contains(@class, "pricebar")]//button'
)
CART_ICON = (By.CSS_SELECTOR, '#shopping_cart_container > a')
CART_BADGE = (By.CSS_SELECTOR, '.shopping_cart_badge')
CHECKOUT_BUTTON = (By.CSS_SELECTOR, 'a.checkout_button')
SORT_SELECTOR = (By.CSS_SELECTOR, 'select.product_sort_container')


@step('I Click the Bike Light Add to Cart Button')
def step_impl(context):
    context.current_element = context.driver.find_element(*BIKE_LIGHT_BUTTON)
    context.current_element.click()


@step('I Click the Test all the things T-Shirt Add to Cart Button')
def step_impl(context):
    context.current_element = context.driver.find_element(*TEST_ALL_TSHIRT)
    context.current_element.click()


@then('the button should contain the Text "{text}"')
def step_impl(context, text):
    context.current_element = context.driver.find_element(*BIKE_LIGHT_BUTTON)
    assert context.current_element.text == text, 'Expected {expected}, got {found}'.format(
        expected=text,
        found=context.current_element.text
    )

@step('the cart badge displays "{num}"')
def step_impl(context, num):
    context.current_element = context.driver.find_element(*CART_BADGE)
    assert context.current_element.text == num, 'Expected {expected}, got {found}'.format(
        expected=num,
        found=context.current_element.text
    )

@then('the cart badge should not be present')
def step_impl(context):
    cart_badges = context.driver.find_elements(*CART_BADGE)
    assert len(cart_badges) == 0, 'Cart badge was present'


@step('I select "{text}" from the sort selector')
def step_impl(context, text):
    selector = Select(context.driver.find_element(*SORT_SELECTOR))
    selector.select_by_visible_text(text)


@step('item "{num}" shold be "{text}"')
def step_impl(context, num, text):
    xpath_selector = '//div[contains(@class, "inventory_item")][' + num + ']'
    context.current_item = context.driver.find_element(By.XPATH, xpath_selector)
    context.current_item_title = context.current_item.find_element(
        By.CSS_SELECTOR,
        '.inventory_item_name'
    )
    assert context.current_item_title.text == text, 'Expected {expected}, got {found}'.format(
        expected=text,
        found=context.current_item_title.text
    )


@step('I click on the cart icon')
def step_impl(context):
    context.current_element = context.driver.find_element(*CART_ICON)
    context.current_element.click()


@step('the price for item "{num}" should be "{price}"')
def step_impl(context, num, price):
    selector = '(//div[@class="inventory_item_price"])[{}]'.format(num)
    context.current_element = context.driver.find_element(By.XPATH, selector)
    assert context.current_element.text == price, 'Expected {expected}, got {found}'.format(
        expected=price,
        found=context.current_element.text
    )

@step('I click the checkout button')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10, 0.1)
    checkout_button = wait.until(EC.element_to_be_clickable(CHECKOUT_BUTTON))
    actions = ActionChains(context.driver)
    actions.move_to_element(checkout_button)
    actions.click()
    actions.perform()

@step('I fill out the contact information with "{first}" "{last}" from the "{zipcode}"')
def step_impl(context, first, last, zipcode):
    context.execute_steps('''
      Given I enter "{0}" into the first name field
      When I enter "{1}" into the last name field
      Then I enter "{2}" into the zip code field
    '''.format(
        first,
        last,
        str(zipcode)
    ))
