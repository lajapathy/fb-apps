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
        #test_info = self.base.read_app_data(file_name="info.json",class_name=class_name)
        #test_info = self.base.read_app_data(file_name="info.json",dir_name="test_class1.py",class_name=class_name,fn_name="test_four")

        class_name = self.__class__.__name__
        test_info  = self.base.read_app_data(file_name="info.json",class_name=class_name)

        for distro in test_info:
            print(distro['x'])
            print(distro['y'])

    def test_get_friends_list(self):
        ''' '''

        print(self.get_friends_list())
