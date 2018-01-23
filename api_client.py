import pytest
import json
import sys
import os

sys.path.append(os.getcwd()+"/resources")

from access_token import AccessToken

class ApiClient(object):
    """ Base class for all api client classes of APIC EM. """

    def __init__(self):
        ''' Setups up Facebook API client '''

        self.access_token_util = AccessToken()
        self.token = self.access_token_util.get_access_token()