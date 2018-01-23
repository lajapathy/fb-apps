from api_client import ApiClient

class User(ApiClient):
    
    ''' This class will have methods related to User information '''

    def __init__(self):
        pass

    def search_user(keyword, type='user'):
        ''' Searches for an user with keyword in the name '''

        users = graph.search(type='user',q='Mark Zuckerberg')