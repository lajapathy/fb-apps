import json

class Base(object):
    ''' Base level methods '''

    def __init__(self):
        pass

    def read_app_data(self, data_file):
        ''' Reads information from JSON/YAML file and returns a dictionary '''

        if data_file.endswith('.json'):
            test_data = json.loads(open(data_file,'r'))

        return test_data
