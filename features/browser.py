# pylint: disable=missing-function-docstring,attribute-defined-outside-init,consider-using-f-string,too-many-public-methods
'''Configuratins saved to easily setup different browsers'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from settings import DEFAULT_WIDTH, DEFAULT_HEIGHT, DEFAULT_BROWSER_POSITION
from settings import DRIVER, log, SELENIUM, SL_DC


CHROME_PATH = './env/bin/chromedriver'
FIREFOX_PATH = './env/bin/geckodriver'


def dict_from_string(current_dict, string):
    for item in string.split(','):
        key, value = item.split(':')
        current_dict[key.strip(' \"}{:')] = value.strip(' \"}{:')
    return current_dict


class Browser():
    '''Configuratins saved to easily setup different browsers'''

    def __init__(self):
        log.info('Loading normal browser list')

    def set_defaults(self, browser_obj):
        ''' 
          Sets position of browser on screen.
          Keep set_window_position after set_window_sizeself or Safari will reposition.
          Safari also requires you account for OSX Top Nav with poistioning.
        '''
        browser_obj.set_window_size(DEFAULT_WIDTH, DEFAULT_HEIGHT)
        browser_obj.set_window_position(
            DEFAULT_BROWSER_POSITION['x'],
            DEFAULT_BROWSER_POSITION['y']
        )


    def mandatory_chrome_options(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument(
            '--disable-plugins --disable-instant-extended-api --ignore-certificate-errors'
        )
        return self.chrome_options


    def get_chrome_driver(self):
        self.chrome_options = self.mandatory_chrome_options()
        self.service = Service(executable_path=CHROME_PATH)
        self.browser = webdriver.Chrome(
            service=self.service,
            options=self.chrome_options,
        )
        # Desktop size
        self.set_defaults(self.browser)
        return self.browser


    def get_headless_chrome(self):
        self.chrome_options = self.mandatory_chrome_options()
        self.chrome_options.headless = True
        # soon https://www.selenium.dev/blog/2023/headless-is-going-away/#after
        # self.chrome_options.add_argument("--headless=new")
        self.service = Service(executable_path=CHROME_PATH)
        assert self.chrome_options.headless is True, \
            'Chrome did not get set to headless'
        self.browser = webdriver.Chrome(
            service=self.service,
            options=self.chrome_options,
        )
        # Desktop size
        self.set_defaults(self.browser)
        return self.browser


    def get_firefox_driver(self):
        self.firefox_options = FirefoxOptions()
        self.service = FirefoxService(executable_path=FIREFOX_PATH)
        self.browser = webdriver.Firefox(
            options=self.firefox_options,
            service=self.service
        )
        # Desktop size
        self.set_defaults(self.browser)
        return self.browser


    def get_headless_firefox_driver(self):
        self.firefox_options = FirefoxOptions()
        self.service = FirefoxService(executable_path=FIREFOX_PATH)
        self.firefox_options.add_argument("--headless")
        self.browser = webdriver.Firefox(
            options=self.firefox_options,
            service=self.service
        )
        # Desktop size
        self.set_defaults(self.browser)
        return self.browser


    def get_safari_driver(self):
        '''
          Sets up Safari Driver, set_defaults sometimes causes 
          safari problems so watch out for it.
        '''
        self.browser = webdriver.Safari()
        self.set_defaults(self.browser)
        return self.browser


    def get_iphone_12_pro(self):
        self.chrome_options = self.mandatory_chrome_options()
        self.service = Service(executable_path=CHROME_PATH)
        mobile_emulation = { "deviceName": "iPhone 12 Pro" }
        self.chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        self.browser = webdriver.Chrome(
            service=self.service,
            options=self.chrome_options,
        )
        # Desktop size
        self.set_defaults(self.browser)
        return self.browser


    def get_iphone_12_pro(self):
        self.chrome_options = self.mandatory_chrome_options()
        self.service = Service(executable_path=CHROME_PATH)
        mobile_emulation = { "deviceName": "iPhone 12 Pro" }
        self.chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        self.browser = webdriver.Chrome(
            service=self.service,
            options=self.chrome_options,
        )
        # Desktop size
        self.set_defaults(self.browser)
        return self.browser


    def get_galaxy_s8_plus(self):
        self.chrome_options = self.mandatory_chrome_options()
        self.service = Service(executable_path=CHROME_PATH)
        mobile_emulation = { "deviceName": "Samsung Galaxy S8+" }
        self.chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        self.browser = webdriver.Chrome(
            service=self.service,
            options=self.chrome_options,
        )
        # Desktop size
        self.set_defaults(self.browser)
        return self.browser


    def get_custom_device(self):
        self.chrome_options = self.mandatory_chrome_options()
        service = Service(executable_path='./env/bin/chromedriver')
        mobile_emulation = {
           "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
           "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko)"
        }
        self.chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        self.browser = webdriver.Chrome(
            service=service,
            options=self.chrome_options,
        )
        # Desktop size
        self.set_defaults(self.browser)
        return self.browser


    def return_driver_dict(self):
        '''Returns a dict that maps short driver names to functions'''
        self.drivers = {
            'chrome': self.get_chrome_driver,
            'custom_device': self.get_custom_device,
            'firefox': self.get_firefox_driver,
            'galaxy_s8_plus': self.get_galaxy_s8_plus,
            'headless_chrome': self.get_headless_chrome,
            'headless_firefox': self.get_headless_firefox_driver,
            'iphone_12_pro': self.get_iphone_12_pro,
            'safari': self.get_safari_driver,
        }
        return self.drivers


    def get_browser_driver(self):
        '''Returns driver based on environmental variable'''
        drivers = self.return_driver_dict()
        if DRIVER not in drivers:
            raise EnvironmentError('Unrecognized driver: {}'.format(DRIVER))
        return drivers.get(DRIVER)()


    def get_driver_by_name(self, name):
        '''Returns driver based on name'''
        log.info('Getting Custom Driver: %s' % name)
        drivers = self.return_driver_dict()
        if DRIVER not in drivers:
            raise EnvironmentError('Unrecognized driver: {}'.format(DRIVER))
        return drivers.get(name)()
