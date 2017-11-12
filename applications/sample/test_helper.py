import pytest
from base.base import Base

class TestHelper(object):
    ''' Helper methods for sample tests ''' 

    @pytest.fixture(autouse=True)
    def setup_utils(self):
        self.base = Base()

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
