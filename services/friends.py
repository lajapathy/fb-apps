import pytest

from api_client import ApiClient
from graph_api import GraphAPI


class Friends(ApiClient):
    ''' 'This class will construct HTTP requests to obtain friends related information'''

    def __init__(self):
        super(Friends,self).__init__()
        self.graph_util = GraphAPI(
            access_token=self.token,
            api_version="2.10")

    def get_all_friends(self):
        '''  
        	This method returns all friends of a given access token

        	Returns:
	    List of IDs of all friends
        '''
        graph = self.graph_util.get(
            endpoint="me/friends",
            params={
            "debug": "all",
            "format": "json",
            "suppress_http_code": "1"
            })
        for friend in friends['data']:
            print("{} has id {}".format(friend['name'].encode('utf-8'), friend['id']))

        
