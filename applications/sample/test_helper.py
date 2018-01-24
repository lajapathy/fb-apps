import pytest

from base.base import Base
from services.friends import Friends
from services.posts import Posts
from services.user import User
from api_client import ApiClient


class TestHelper(object):
    ''' Helper methods for sample tests ''' 

    @pytest.fixture(autouse=True)
    def setup_utils(self):
        self.base = Base()
        self.posts_util = Posts()
        self.friends_util = Friends()
        self.user_util = User()

    def check_char_in_string(self, char, string):
        ''' 
 	Checks whether a char is present in a string or not

	Args:
	    char: Character to be checked
	    String: String in which character is present or not

	Returns:
	    True: If char is present in string
	    False: Otherwise
        '''
	
        return (char in string)

    def get_friends_list(self):
        ''' 
            Returns list of friends
        '''
        return self.friends_util.get_all_friends()
