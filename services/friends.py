import pytest

from api_client import ApiClient
from services.services_helper import ServiceHelper


class Friends(ServiceHelper):
    ''' 'This class will construct HTTP requests to obtain friends related information'''

    def __init__(self):
        #super(Friends,self).__init__()
        self.api_client = ApiClient()

    def get_all_friends(self):
        '''  
            This method returns all friends of a given access token

            Returns:
        List of IDs of all friends
        '''

        data=self.api_client.call_api(
            url="me/friends",
            method='GET')
        return data
        # graph = self.graph_util.get(
        #     endpoint="me/friends",
        #     params={
        #     "debug": "all",
        #     "format": "json",
        #     "suppress_http_code": "1"
        #     })
        # for friend in friends['data']:
        #     print("{} has id {}".format(friend['name'].encode('utf-8'), friend['id']))

        
