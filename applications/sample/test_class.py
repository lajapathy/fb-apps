import pytest

class TestClass(object):
    ''' Sample Class to test pytest basic functionalities '''
    def test_one(self):
	''' Dummy test '''
        x = "this"
        assert 'h' in x

    def test_two(self):
	''' Dummy test '''
        x = "hello"
        assert hasattr(x, 'check')

    def test_three(self):
	''' 
           This test will read input data from JSON file 
           and check if a character is present in a string or not
        '''
	pass
