import pytest
import json
import sys
import os
sys.path.append(os.getcwd()+"/resources")

from access_token import AccessToken
from graph_api import GraphAPI

class ApiClient(object):
    """ Base class for all api client classes of APIC EM. """

    @pytest.mark.fixture(autouse=True)
    def setup_client(self):
        ''' Setups up Facebook API client '''

        self.access_token_util = AccessToken()
        self.token = self.access_token_util.get_access_token()
        self.graph_util = GraphAPI(access_token=self.token, version="2.10")
        self.app_info = json.loads(open("app-info.json",'r'))
        

