import facebook
import urllib
import urlparse
import subprocess
import warnings

class AccessToken(obj):
   ''' Description '''

   def get_access_token(self, app_id, app_secret, profile_id):
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
           'https://graph.facebook.com/oauth/access_token?' + urllib.urlencode(oauth_args)]

      oauth_response = subprocess.Popen(oauth_curl_cmd,
                                  stdout = subprocess.PIPE,
                                  stderr = subprocess.PIPE).communicate()[0]

      try:
          oauth_access_token = urlparse.parse_qs(str(oauth_response))['access_token'][0]
      except KeyError:
          print('Unable to grab an access token!')
          exit()

      return oauth_access_token









# Try to post something on the wall.
try:
    fb_response = facebook_graph.put_wall_post('Hello from Python', \
                                               profile_id = FACEBOOK_PROFILE_ID)
    print fb_response
except facebook.GraphAPIError as e:
    print 'Something went wrong:', e.type, e.message