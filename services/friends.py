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
        graph = self.graph_util.get("me/friends")
        for friend in friends['data']:
            print("{} has id {}".format(friend['name'].encode('utf-8'), friend['id']))

        
