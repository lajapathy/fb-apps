from access_token import AccessToken

class ServiceHelper(object):
    ''' Provides common utilities used in services'''

    def __init__(self):
        self.access_token_util = AccessToken()

    def generate_access_token(self):
        token = self.access_token_util.get_access_token()
        return token