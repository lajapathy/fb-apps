import urllib
import subprocess
import warnings
import requests
import json
import urlparse

class AccessToken(object):
    ''' Pass  '''
    
    def get_app_access_token(self, app_id="139232676651716",
        app_secret="e96006b4dba8fc282171d061c462f437",
        profile_id="631299528"):
        ''' 
           This method returns access token
          
           Args:
           Returns:
        '''
        warnings.filterwarnings('ignore', category=DeprecationWarning)
        oauth_args = dict(client_id  = app_id,
                   client_secret = app_secret,
                   grant_type    = 'client_credentials')

        oauth_curl_cmd = ['curl',
            'https://graph.facebook.com/v2.11/oauth/access_token?' + urllib.urlencode(oauth_args)]

        oauth_response = subprocess.Popen(oauth_curl_cmd,
                                   stdout = subprocess.PIPE,
                                   stderr = subprocess.PIPE).communicate()[0]

        try:
            oauth_access_token = str((json.loads(str(oauth_response)))["access_token"])
        except KeyError:
            assert False, "Unable to grab access token"

        return oauth_access_token

    def get_user_access_token(self):
        ''' Returns user access token '''
        #TODO(lajju) - Replace this with a dynamic way
        user_access_token = ("EAABZBoaI7osQBAJxH9gfYqGKeZAZAPGResdZCU2PuNafOZAiIZB5ZB3ZAyvzuvdHDJXCnbb"
        "5AGaNq75ZBEaYZCKZCIs2ZBR8IJ8ywpaZBMBZCGTOic5EZAlsy2DtqiBzfK0DWnQmMQ7xka9mNNpRC3sjIul1BJKe"
        "Xe0KQkYgFxpQ0bvoYdVyNTAdhDnnwoxZCsQwbkZANarwZD")

        return user_access_token
