import os
import logging
from dotenv import load_dotenv

logging.basicConfig(level=os.environ.get("LOG_LEVEL", "ERROR"))
log = logging.getLogger("debug_logger")

# use `export QA_ENV=name` to set the current envionrment you're testing against
QA_ENV = os.getenv('QA_ENV', 'local').lower()
if 'test' in QA_ENV:
    print('Loading Testing Environment variables')
    load_dotenv(dotenv_path='./secrets/testing.env', verbose=True)
    IAP_ON = True
elif 'dev' in QA_ENV:
    print('Loading Dev Environment variables')
    load_dotenv(dotenv_path='./secrets/dev.env')
elif 'stag' in QA_ENV:
    print('Loading Staging Environment variables')
    load_dotenv(dotenv_path='./secrets/staging.env')
elif 'production' in QA_ENV or 'live' in QA_ENV:
    print('Loading Production Environment variables')
    load_dotenv(dotenv_path='./secrets/production.env')
else:
    assert QA_ENV == 'local', 'Unrecognized ENV name'
    print('Using default Environment variables')

########
# Overwritten by ENV files
########


# Host of server
HOST = os.getenv('HOST', 'localhost:3000')
if QA_ENV == 'local':
    HOST_URL = os.getenv('HOST_URL', 'http://%s' % HOST)
else:
    HOST_URL = os.getenv('HOST_URL', 'https://%s' % HOST)

# Google IAP
CLIENT_ID = os.getenv(
    'CLIENT_ID', '012345678901-am29widj4kW0l57Kaqmsh3ncjskepsk2.apps.googleusercontent.co')
GOOGLE_APPLICATION_CREDENTIALS = os.getenv(
    'GOOGLE_APPLICATION_CREDENTIALS', '/path/to/json/web/token.json')
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY', '0123456789')

ADMIN_EMAIL = os.getenv('ADMIN_EMAIL', 'fakeUser1@gmail.com')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'fakepassword')
ADMIN_NAME = os.getenv('ADMIN_NAME', 'Al\' Admin')

EDITOR_EMAIL = os.getenv('EDITOR_EMAIL', 'fakeUser2@gmail.com')
EDITOR_PASSWORD = os.getenv('EDITOR_PASSWORD', 'fakepassword')
EDITOR_NAME = os.getenv('EDITOR_NAME', 'Eddie Editor')

USER_EMAIL = os.getenv('USER_EMAIL', 'fakeUser3@gmail.com')
USER_PASSWORD = os.getenv('USER_PASSWORD', 'fakepassword')
USER_NAME = os.getenv('USER_NAME', 'Vinny Testaverde')

NO_ACCESS_EMAIL = os.getenv('NO_ACCESS_EMAIL', 'fakeUser4@gmail.com')
NO_ACCESS_PASSWORD = os.getenv('NO_ACCESS_PASSWORD', 'fakepassword')

RECOVERY_EMAIL = os.getenv('RECOVERY_EMAIL', 'another_fake_email@gmail.com')
RECOVERY_CITY = os.getenv('RECOVERY_CITY', 'New New York')
RECOVERY_PHONE = os.getenv('RECOVERY_PHONE', '555-555-5555')
#########


ACCOUNTS = {
    'admin': {
        'email': ADMIN_EMAIL,
        'password': ADMIN_PASSWORD,
        'name': ADMIN_NAME
    },
    'editor': {
        'email': EDITOR_EMAIL,
        'password': EDITOR_PASSWORD,
        'name': EDITOR_NAME
    },
    'user': {
        'email': USER_EMAIL,
        'password': USER_PASSWORD,
        'name': USER_NAME
    },
    'no access user': {
        'email': NO_ACCESS_EMAIL,
        'password': NO_ACCESS_PASSWORD,
        'name': 'No access user'
    }
}

JIRA_PROJECT_ABBR = 'KEY-'

DRIVER = os.getenv('DRIVER', 'chrome')
DRIVER = DRIVER.lower().replace(' ', '_').replace('-', '_')

SL_DC = os.getenv(
    'SL_DC',
    '{"platform": "Mac OS X 10.9", "browserName": "chrome", "version": "31"}'
)

PAGES_DICT = {
    'index': '',
    'inventory':'/v1/inventory.html',
    'products page':'/about/products',
    'contact':'/contact'
}

DEBIAN_CHROME = '/usr/bin/google-chrome'

DEFAULT_WIDTH = 1366
DEFAULT_HEIGHT = 768
MOBILE_WIDTH = 360
MOBILE_HEIGHT = 640
TABLET_WIDTH = 600
TABLET_HEIGHT = 1024

DISPLAY = os.getenv('DISPLAY', ':99')
XVFB_RESOLUTION = os.getenv('XVFB_RESOLUTION', '1366x768x24')

# Safari requires you account for OSX Top Nav & is iffy about edge
DEFAULT_BROWSER_POSITION = {
    'x': 10,
    'y': 30
}

PROXY_PASSTHROUGH = os.getenv('PROXY_PASSTHROUGH', [
    'example.oauth.googleusercontent.com',
])

SLACK_URL = os.getenv('SLACK_URL', 'https://hooks.slack.com/services/blarg/blerg')
SLACK_CHANNEL = os.getenv('SLACK_CHANNEL', None)

OK_SRCS = [
    HOST_URL,
    'cdn.firebase.com',
    'doubleclick.net',
    'fonts.googleapis.com',
    'google-analytics.com',
    'google.com',
    'googletagmanager.com',
    'gstatic.com',
    'gstatic.cn',
    'maps.googleapis.com',
    'oauth.googleusercontent.com',
    'schema.org',
]

default_headers = {
    'Accept-Charset': 'UTF-8',
    'Accept': 'text/html,application/xhtml+xml,application/xml,application/json,image/webp,image/apng,',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36, QA Tests'
}

print(HOST_URL)
print('Proxy passthrough set to {}'.format(PROXY_PASSTHROUGH))
