from api_client import ApiClient

class Friends(ApiClient):
    ''' 'This class will construct HTTP requests to obtain friends related information'''

    def __init__(self):
        pass

    def get_all_friends(self, access_token):
        '''  
        	This method returns all friends of a given access token

        	Args:
        	    access_token

        	Returns:
	    List of IDs of all friends
        '''

        self.access_token = self.access_token_util.get_access_token()