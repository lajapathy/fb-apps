import facebook

class User(ApiClient):
    
    ''' This class will have methods related to User information '''

    def search_user(keyword, type='user'):
        ''' Searches for an user with keyword in the name '''

        users = graph.search(type='user',q='Mark Zuckerberg')