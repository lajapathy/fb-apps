import json
import os
import pytest
import inspect


class Base(object):
    ''' Base level methods '''

    def __init__(self):
        #import pdb;pdb.set_trace()
        #self.logger = logging.getLogger(__name__)
        pass

    def read_app_data(self,file_name=None,dir_name=None,class_name=None,fn_name=None):
        '''
        	Args:
        	    file_name(str): Name of the JSON file
        	    file_path(str): Path of the JSON file. If None,
        	        the method will search for the corresponding testdata directory for a file with name as  file_name
        	Returns:
        	    Parsed data in dictionary
        '''
        if file_name is None or class_name is None:
            print('Cannot get the test data file name') 
            raise Exception
        else:
            stack = inspect.stack()[1]
            if dir_name is None:
                dir_name = os.path.basename(stack[1])
            if fn_name is None:
                fn_name = stack[3]          
            file = os.getcwd() + '/applications/sample/testdata' + '/' + dir_name + '/' + class_name +'/' + fn_name + '/' + file_name

            #Check if test data file exists at the last level , if it doesnt move back to 
            # eg. File name : toothless/fb-apps/applications/sample/testdata/test_class.py/TestClass/test_three/info.json 
            print('File : {} '.format(file))          
            if os.path.isfile(file):
                print('Found file '.format(file))
            else:
                file = ""
                file = os.getcwd() + '/applications/sample/testdata' + '/' + dir_name + '/' + class_name +'/' + file_name
                print('File : {} '.format(file)) 
                if os.path.isfile(file):
                    print('Found file '.format(file))
                else:
                    file = ""
                    file = os.getcwd() + '/applications/sample/testdata' + '/' + dir_name + '/' + file_name
                    print('File : {} '.format(file)) 
                    if os.path.isfile(file):
                        print('Found file '.format(file))
                    else:
                        file = ""
                        file = os.getcwd() + '/applications/sample/testdata/'  + file_name
                        print('File : {} '.format(file)) 
                        if os.path.isfile(file):
                            print('Found file '.format(file))
                        else:
                            print('Cannot find the test data file')
                            raise Exception

            # File should be found by now. Now parse the json file and return the dict
            with open(file, 'r') as f:
                json_dict = json.load(f)

            return json_dict





