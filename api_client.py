import pytest
import facebook
import json
from access_token import AccessToken

class ApiClient(object):
    """ Base class for all api client classes of APIC EM. """

    def __init__(self, api_client):
        """Initializer of Apis of APIC EM.

        Args:
            api_client (Object): ClientManager Object that makes API calls.
        """

        self.api_client = api_client

    @pytest.mark.fixture(autouse=True)
    def setup_client(self):
        ''' Setups up Facebook API client '''

        self.access_token_util = AccessToken()
        self.graph_util = facebook.GraphAPI(access_token="your_token", version="2.10")
        self.app_info = json.loads(open("app-info",'r'))
        

