import pytest

from facebook_test_helper import FacebookTestHelper


class FacebookTest(FacebookTestHelper):
    ''' Test basic facebook APIs '''

    def test_one_f(self):
        ''' Dummy test '''
        x = "this"
        assert 'h' in x

    def test_two_f(self):
        ''' Dummy test '''
        x = "h"
        string="check"
        err_msg = "Character {} not present in string {}".format(x, string)
        assert self.check_char_in_string(x, string), err_msg

    def test_post_on_wall(self):
        ''' Posts msg on wall '''

        msg="Test post using Python API client"
        self.posts_util.post_msg_on_wall(
        	msg=msg)

    def test_get_friends_list(self):
        ''' '''
        print(self.get_friends_list())