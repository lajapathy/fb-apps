import pytest
import json
import sys
import os
sys.path.append(os.getcwd()+"/resources")

from access_token import AccessToken
from graph_api import GraphAPI


class ApiClient(object):
    """ Base class for all api client classes of APIC EM. """

    def __init__(self):
        ''' Setups up Facebook API client '''

        self.access_token_util = AccessToken()

    def _generate_access_token(self):

        token = self.access_token_util.get_user_access_token()
        return token

    def _create_graph_util_object(self, token, api_version="2.10"):
        '''
            Creates new graph util object with new token

            Args:
                token: Token used to post APIs
                api_version: API version
        '''

        return GraphAPI(
            access_token=token,
            api_version=api_version)

    def call_api(self, url, method, params={}):
        '''
            Makes API calls
            Args:
                url:
                method: post,get,put or delete
                params(dict): Optional parameters for API call
        '''
        graph_util = self._create_graph_util_object(
            token=self._generate_access_token())

        if method=='POST':
            pass
        elif method=='GET':
            return graph_util.get(
                endpoint=url,
                params=params)



