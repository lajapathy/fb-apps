import pytest
from test_helper import TestHelper

class TestClass(TestHelper):
    ''' Sample Class to test pytest basic functionalities '''
    
    def test_one(self):
        ''' Dummy test '''
        x = "this"
        assert 'h' in x

    def test_two(self):
        ''' Dummy test '''
        x = "h"
        string="check"
        err_msg = "Character {} not present in string {}".format(x, string)
        assert self.check_char_in_string(x, string), err_msg

    def test_three(self):
        ''' 
           This test will read input data from JSON file 
           and check if a character is present in a string or not
        '''
        test_info = self.base.read_app_data("info.json")

    def test_get_friends_list(self):
        ''' '''

        import pdb; pdb.set_trace()  # breakpoint 2ed48f59 //
        print(self.get_friends_list())
