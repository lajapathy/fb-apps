import pytest
import os

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

    @pytest.mark.usefixtures("get_test_details")
    def test_three(self):
        ''' 
           This test will read input data from JSON file 
           and check if a character is present in a string or not
        '''
        test_info = self.base.read_app_data("info.json")

    def test_get_friends_list(self):
        ''' 
            Dummy test - gets all friends
        '''

        friends = self.get_friends_list()

    @pytest.fixture
    def get_test_details(self, request):
        self.test_case_name = request.node.name
        self.cwd = os.getcwd()
        self.class_name = self.__class__.__name__
        self.file_name = os.path.basename(__file__)
        self.file_absolute_path = os.path.abspath(os.path.dirname(__file__))
