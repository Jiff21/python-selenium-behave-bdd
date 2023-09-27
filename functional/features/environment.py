# -*- coding: UTF-8 -*-
import os
import sys
from behave import *
from functional.features.browser import Browser
from functional.features.steps.workarounds import LocalStorage
from functional.features.requester import SetupRequests
from settings import DEFAULT_WIDTH, DEFAULT_HEIGHT
from settings import DISPLAY, XVFB_RESOLUTION
from settings import EDITOR_EMAIL, EDITOR_PASSWORD, EDITOR_NAME
from settings import HOST_URL, DRIVER, QA_ENV, log
from settings import MOBILE_WIDTH, MOBILE_HEIGHT
from settings import TABLET_WIDTH, TABLET_HEIGHT
from selenium.webdriver.support.ui import WebDriverWait



def get_jira_number_from_tags(context):
    for tag in context.tags:
        if JIRA_PROJECT_ABBR in tag:
            return tag


def dismiss_cookie_consent(driver):
    local_storage = LocalStorage(driver)
    # Dismiss Cookie Consent Banner by Default
    local_storage.set('cookieConsent', 'true')


def clear_local_storage(driver):
    local_storage = LocalStorage(driver)
    local_storage.clear()


def is_not_chromedriver():
    return bool('chrome' not in DRIVER.lower())


def before_all(context):
    pass


def after_all(context):
    pass


def before_feature(context, feature):
    if 'server' in context.config.userdata:
        feature.name += ' on ' + context.config.userdata['server'] + ' environment'
        current_driver = str('tested_in_' + DRIVER)
        feature.tags.append(current_driver)


# def after_feature(context, feature):


def before_scenario(context, scenario):
    if 'skip' in context.tags:
        jira_number = get_jira_number_from_tags(context)
        scenario.skip("\n\tSkipping tests until %s is fixed" % jira_number)
        return
    if 'chrome-only' in context.tags:
        if is_not_chromedriver() is True:
            scenario.skip('Skipping test not supported outside chrome')
            return
    if 'no-safari' in context.tags:
        if 'safari' in DRIVER:
            scenario.skip('Skipping test not supported in safari')
            return
    if 'local-only' in context.tags:
        if QA_ENV != 'local':
            scenario.skip('Skipping test, only supported locally')
            return
    if 'no-local' in context.tags:
        if QA_ENV == 'local':
            scenario.skip('Skipping test, not supported locally')
            return
    elif 'browser' in context.tags:
        context.browser = Browser()
        context.driver = context.browser.get_browser_driver()
        if 'chrome' in DRIVER:
            scenario.name += ' in %s %s' % (
                context.driver.capabilities['browserName'].capitalize(),
                context.driver.capabilities['browserVersion']
            )
        if 'firefox' in DRIVER:
            scenario.name += ' in %s %s' % (
                context.driver.capabilities['browserName'].capitalize(),
                context.driver.capabilities['browserVersion']
            )
    else:
        context.driver = None
    if 'requests' in context.tags:
        requester = SetupRequests()
        context.session = requester.setup_session()
    if context.driver is not None:
        context.wait = WebDriverWait(context.driver, 20, 0.25)
        if 'mobile' in context.tags:
            context.driver.set_window_size(MOBILE_WIDTH, MOBILE_HEIGHT)
        if 'tablet' in context.tags:
            context.driver.set_window_size(TABLET_WIDTH, TABLET_HEIGHT)
        if 'not-logged-in' in context.tags:
            delete_firebase_cookies(context.driver)


def after_scenario(context, scenario):
    if ('skip' not in context.tags):
        if is_not_chromedriver() is True and 'chrome-only' in context.tags:
            return
        else:
            context.driver.quit()
