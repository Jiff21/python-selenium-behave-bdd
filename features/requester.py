"""Sets up requests session, adding bearer_header if set."""
# pylint: disable=too-few-public-methods

import requests
from settings import log, default_headers


class SetupRequests():
    '''Setup for requests session used in the various auth files'''

    def __init__(self):
        log.debug('Setting up requests')

    def setup_session(self, bearer_header=None):
        '''Sets up a sesssion with default headers set in settings.py'''
        session = requests.Session()
        session.headers.update(default_headers)
        if bearer_header is not None:
            session.headers.update(bearer_header)

        return session
