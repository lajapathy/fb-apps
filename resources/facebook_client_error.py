
class FacebookClientError(Exception):
    ''' '''

    def __init__(self, message, error_type=None, error_code=None):
        self.type = error_type

        self.message = message
        if error_type is not None:
            self.message = '%s: %s' % (error_type, message)

        self.code = error_code

        super(FacebookClientError, self).__init__(self.message)