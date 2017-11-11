import pytest

class TestHelper(object):
    ''' Helper methods for sample tests ''' 

    def test_answer(cmdopt):
        if cmdopt == "type1":
            print ("first")
        elif cmdopt == "type2":
            print ("second")
        assert 0 # to see what was printed
