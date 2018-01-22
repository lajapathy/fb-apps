import pytest
import json

from access_token import AccessToken
from resources.graph_api import GraphAPI

class ApiClient(Services):
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
        self.token = self.access_token_util.get_access_token()
        self.graph_util = GraphAPI(access_token="your_token", version="2.10")
        self.app_info = json.loads(open("app-info.json",'r'))
        

