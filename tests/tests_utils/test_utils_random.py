''' test_utils_random.py

    Unit tests for utils_random
'''
from utils.utils_random import get_random_string_from_list


class TestUtilsRandom(object):
    ''' Unit tests container for utils_random '''

    def test_random_string_from_list(self):
        ''' Test for get_random_string_from_list '''
        str_list = ["1", "2", "3"]
        assert get_random_string_from_list(str_list) in str_list
