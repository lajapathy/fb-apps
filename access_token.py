import urllib
import subprocess
import warnings

class AccessToken(object):
    ''' Description '''
    # def get_access_token(self, app_id, app_secret, profile_id):
    #     ''' 
    #        This method returns access token
          
    #        Args:

    #        Returns:

    #     '''
    #     warnings.filterwarnings('ignore', category=DeprecationWarning)
    #     oauth_args = dict(client_id  = app_id,
    #                client_secret = app_secret,
    #                grant_type    = 'client_credentials')

    #     oauth_curl_cmd = ['curl',
    #         'https://graph.facebook.com/oauth/access_token?' + urllib.urlencode(oauth_args)]

    #     oauth_response = subprocess.Popen(oauth_curl_cmd,
    #                                stdout = subprocess.PIPE,
    #                                stderr = subprocess.PIPE).communicate()[0]

    #     try:
    #         oauth_access_token = urlparse.parse_qs(str(oauth_response))['access_token'][0]
    #     except KeyError:
    #         print('Unable to grab an access token!')
    #         exit()

    #     return oauth_access_token

    def get_access_token(self,
        app_id="139232676651716", app_secret="e96006b4dba8fc282171d061c462f437"):
        '''
            pass
        '''
        
        import pdb; pdb.set_trace()  # breakpoint cf26be4f //
        data = {'grant_type': 'client_credentials', 'client_id': app_id, 'client_secret': app_secret}
        file = requests.post('https://graph.facebook.com/oauth/access_token?', params = data)
        result = file.text.split("=")[1]
        return result
