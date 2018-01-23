import requests

class FacebookAPI(object):
    def __init__(self, client_id=None, client_secret=None, redirect_uri=None,
                headers=None):

        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

        # If there's headers, set them. If not, lets
        self.headers = headers or {'User-agent': 'Requests-Facebook %s' % __version__}

    def get_auth_url(self, display='popup', scope=None):
        scope = scope or []
        url = 'https://www.facebook.com/dialog/oauth'
        qs = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'redirect_uri': self.redirect_uri,
            'display': display,
            'scope': ','.join(scope)
        }
        return '%s?%s' % (url, urlencode(qs))

    def get_access_token(self, code):
        url = 'https://graph.facebook.com/oauth/access_token'
        qs = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'redirect_uri': self.redirect_uri,
            'code': code
        }
        response = requests.get(url, params=qs, headers=self.headers)

        status_code = response.status_code
        content = response.content

        if status_code != 200:
            try:
                content = response.json()
            except ValueError:
                raise FacebookClientError('Unable to parse response, invalid JSON.')

            if content.get('error') is not None:
                error = content['error']
                error_type = error.get('type', '')
                error_message = error.get('message', '')
                error_code = error.get('code')

                raise FacebookAuthError(error_message, error_type=error_type, error_code=error_code)
            else:
                raise FacebookClientError('An unknown error occurred.')

        try:
            data = response.json()
        except ValueError:
            data = dict(parse_qsl(content))
        except AttributeError:
            raise FacebookAuthError('Unable to obtain access token.')

        return data