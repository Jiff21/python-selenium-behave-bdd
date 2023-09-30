'''Shared steps for all tests'''
# pylint: disable=missing-function-docstring,attribute-defined-outside-init,consider-using-f-string,too-many-public-methods,function-redefined

import requests
from behave import step, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from custom_exceptions import loop_thru_messages
from settings import HOST_URL, log, PAGES_DICT


MENU_BUTTON = (By.CSS_SELECTOR, '#menu_button_container button')
PRODUCTS_SAUCE_LABS_TSHIRT_TITLE = (By.ID, 'item_1_title_link')
SAUCE_LABS_TSHIRT_ADD_REMOVE = (
    By.XPATH,
    '//*[contains(text(), "Sauce Labs Bolt T-Shirt")]/ancestor::div[contains'
    '(@class, "inventory_item")]/div[contains(@class, "pricebar")]//button'
)
CHECKOUT_COMPLETE_HEADER = (By.CSS_SELECTOR, '#checkout_complete_container h2')


@step('I am on "{page_name}"')
def get(context, page_name):
    context.page_name = page_name.lower()
    context.current_url = HOST_URL + PAGES_DICT[context.page_name]
    log.debug('On this url %s' , context.current_url)
    context.driver.get(context.current_url)


@step('I should be on "{page_name}"')
def get(context, page_name):
    context.page_name = page_name.lower()
    assert PAGES_DICT[context.page_name] in context.driver.current_url, \
        'Expected to be at {expected}, but wound up at {result}'.format(
            expected=PAGES_DICT[context.page_name],
            result=context.driver.current_url
        )


@step('I get "{page_name}" with requests session')
def get(context, page_name):
    context.page_name = page_name.lower()
    context.current_url = HOST_URL + PAGES_DICT[context.page_name]
    log.debug('Getting this url with reqests %s', context.current_url)
    context.response = context.session.get(context.current_url)
    # pylint: disable=E1101
    assert context.response.status_code is requests.codes.ok, \
    ' Unexpectedly got a {} response code'.format(context.response.status_code)


@step('it should have a "{code:d}" status code')
def step_impl(context, code):
    assert context.response.status_code == code, \
    'Did not get {expected} status code on response, instead {resullt}'.format(
        expected = code,
        resullt = context.response.status_code
    )


@step('I check the console logs')
def step_impl(context):
    context.console_errors = []
    for entry in context.driver.get_log('browser'):
        try:
            assert "SEVERE" not in entry['level']
        except AssertionError:
            context.console_errors.append(
                "On Page: %s. Expeced no errors in log instead got:\n%s" % (
                    context.current_url,
                    str(entry)
                )
            )

@step('there should be no severe console log errors')
def step_impl(context):
    assert len(context.console_errors) == 0, loop_thru_messages(context.console_errors)


@step(
    'I throttle network speed to "{download:f}" MB/s down,'
    ' "{upload:f}" MB/s up, with "{latency:f}" ms latency'
)
def step_impl(context, download, upload, latency):
    log.debug('Toggling speeds with {:.2f} down and {:.2f} up'.format(
            download,
            upload
    ))
    conversion = 18000
    log.debug(download * conversion)
    context.driver.set_network_conditions(
        offline=False,
        latency=latency,  # additional latency (ms)
        download_throughput=download * conversion,  # maximal throughput
        upload_throughput=upload * (conversion * 2)
    )

@step('I type in "{text}"')
def step_impl(context, text):
    context.current_element.send_keys(text)


@step('I wait for the Menu button')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.presence_of_element_located(MENU_BUTTON))


@then('the url should contain "{uri}"')
def step_impl(context, uri):
    assert uri in context.driver.current_url, "Expected {expected}, got {found}".format(
        expected=uri,
        found=context.driver.current_url
    )


@step('I hit the Return/Enter Key')
def step_impl(context):
    context.current_element.send_keys(Keys.RETURN)



@step('I Click on the title for Sauce Labs T-Shift')
def click_sauce_labs_tee(context):
    context.current_element = context.driver.find_element(*PRODUCTS_SAUCE_LABS_TSHIRT_TITLE)
    context.current_element.click()


@then('the Sauce Labs Bolt Shirt button should be in remove state')
def get(context):
    wait = WebDriverWait(context.driver, 10, 0.2)
    context.current_element = wait.until(EC.element_to_be_clickable(SAUCE_LABS_TSHIRT_ADD_REMOVE))
    assert context.current_element.text == 'REMOVE', 'Button had "{}" text'.format(
        context.current_element.text
    )


@step('the checkout complete header should appear')
def click_sauce_labs_tee(context):
    wait = WebDriverWait(context.driver, 10, 0.2)
    context.current_element = wait.until(EC.visibility_of_element_located(CHECKOUT_COMPLETE_HEADER))
    assert context.current_element.text == "THANK YOU FOR YOUR ORDER", \
        'Did not get expected success text, instead {}'.format(context.current_element.text)
