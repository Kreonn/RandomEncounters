''' stats.py

    This module contains a class representing combat stats
'''
from utils.utils_yaml import load_yaml


class Stat(object):
    ''' Class representing a single stat '''
    def __init__(self, display, abv, categ, counter, value):
        self.display_name = display
        self.abreviation = abv
        self.category = categ
        self.counter = counter
        self.value = value


class StatsContainer(object):
    ''' Class representing a set of stats '''
    def __init__(self):
        self.container = {}
        self.__load_stats()

    def __load_stats(self):
        stats_db = load_yaml("stats")

        for key, dictionary in stats_db.items():
            self.container[key] = Stat(
                dictionary["display"],
                dictionary["abv"],
                dictionary["category"],
                dictionary["counter"],
                dictionary["start"]
            )
