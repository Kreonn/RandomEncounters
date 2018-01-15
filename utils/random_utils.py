''' ramdom_utils.py

    This module contains utility methods to manipulate randomness
'''
from secrets import choice


def get_random_string_from_list(str_list: list):
    ''' Choose a random string in a list

        :param str_list:
            List of strings

        :return:
            Random string from the list
    '''
    return choice(str_list)
