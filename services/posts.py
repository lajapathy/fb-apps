from api_client import ApiClient


class Posts(ApiClient):
    ''' 'This class will construct HTTP requests to obtain posts related information'''

    def __init__(self):
        pass

    def post_msg_on_wall(self, msg="Default: Post from Python API client"):
        '''
        	This method posts the given message on the wall of the profile ID
        	Args:

        	Returns:
        '''
        oauth_access_token = self.access_token_util.get_access_token(
        	app_id=self.app_info["app_id"],
        	app_secret=self.app_info["app_secret"])
        facebook_graph = facebook.GraphAPI(oauth_access_token)

        try:
            fb_response = facebook_graph.put_wall_post(
    		'Hello from Python',
    		profile_id = self.app_info["profile_id"])
        except facebook.GraphAPIError as e:
            print('Something went wrong:', e.type, e.message)