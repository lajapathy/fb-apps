import json
import os
import pytest

class Base(object):
    ''' Base level methods '''

    def __init__(self):
        pass

    def read_app_data(self, file_name, file_path=None):
        '''
        	Args:
        	    file_name(str): Name of the JSON file
        	    file_path(str): Path of the JSON file. If None,
        	        the method will search for the corresponding testdata directory for a file with name as  file_name
        	Returns:
        	    Parsed data in dictionary
        '''
        import pdb; pdb.set_trace()  # breakpoint 98f9d1c0 //
        if td_dir is None:
            td_dir = self.test["case_td_dir"]



