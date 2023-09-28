'''Shared steps for all tests'''
# pylint: disable=missing-function-docstring,attribute-defined-outside-init,consider-using-f-string,too-many-public-methods,function-redefined

import requests
from behave import step, then
from hover_state import *
from custom_exceptions import loop_thru_messages
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from settings import HOST_URL, log, PAGES_DICT


MENU_BUTTON = (By.CSS_SELECTOR, '#menu_button_container button')


@step('I am on "{page_name}"')
def get(context, page_name):
    context.page_name = page_name.lower()
    context.current_url = HOST_URL + PAGES_DICT[context.page_name]
    print('On this url %s' % context.current_url)
    context.driver.get(context.current_url)


@step('I get "{page_name}" with requests session')
def get(context, page_name):
    context.page_name = page_name.lower()
    context.current_url = HOST_URL + PAGES_DICT[context.page_name]
    print('Getting this url with reqests %s' % context.current_url)
    context.response = context.session.get(context.current_url)
    # pylint: disable=E1101
    assert context.response.status_code is requests.codes.ok, \
    ' Unexpectedly got a %d response code' % context.response.status_code


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
