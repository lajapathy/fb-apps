import requests

class GraphAPI(object):
    def __init__(self, access_token=None, headers=None, api_version='v2.6'):
        self.api_url = 'https://graph.facebook.com/'
        self.api_version = api_version
        if self.api_version:
            self.api_url = '%s%s/' % (self.api_url, self.api_version)
        self.access_token = access_token

        # If there's headers, set them. If not, lets
        self.headers = headers or {'User-agent': 'Requests-Facebook %s' % __version__}

    def get(self, endpoint, params=None):
        return self.request(endpoint, params=params)

    def post(self, endpoint, params=None, files=None):
        return self.request(endpoint, method='POST', params=params)

    def delete(self, endpoint, params=None):
        return self.request(endpoint, method='DELETE', params=params)

    def request(self, endpoint, method='GET', params=None):
        params = params or {}

        url = self.api_url + endpoint + '?access_token=' + self.access_token
        method = method.lower()

        if not method in ('get', 'post', 'delete'):
            raise FacebookClientError('Method must be of GET, POST or DELETE')

        params, files = _split_params_and_files(params)

        func = getattr(requests, method)
        try:
            if method == 'get':
                response = func(url, params=params, headers=self.headers)
            else:
                response = func(url,
                                data=params,
                                files=files,
                                headers=self.headers)

        except requests.exceptions.RequestException:
            raise FacebookClientError('An unknown error occurred.')

        try:
            content = response.json()
        except ValueError:
            raise FacebookClientError('Unable to parse response, invalid JSON.')

        if response.status_code != 200:
            if content.get('error') is not None:
                error = content['error']
                error_type = error.get('type', '')
                error_message = error.get('message', '')
                error_code = error.get('code')

                raise GraphAPIError(error_message, error_type=error_type, error_code=error_code)

        return content

    def __repr__(self):
        return u'<GraphAPI: %s>' % self.access_token