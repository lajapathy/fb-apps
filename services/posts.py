import facebook


class Posts(ApiClient):
    ''' 'This class will construct HTTP requests to obtain posts related information'''

    def post_msg_on_wall(self, profile_id, msg="Default: Post from Python API client"):
        '''
        	This method posts the given message on the wall of the profile ID
        	Args:

        	Returns:
        '''
        oauth_access_token = self.access_token_util.get_access_token(
        	self.app_info["app-id"],
        	self.app_info["app-secret"],
        	profile_id)
        facebook_graph = facebook.GraphAPI(oauth_access_token)

        try:
    	fb_response = facebook_graph.put_wall_post('Hello from Python', \
                                               profile_id = FACEBOOK_PROFILE_ID)
    	print(fb_response)
        except facebook.GraphAPIError as e:
            print('Something went wrong:', e.type, e.message)

    