''' entity_creature.py

    This module provides everything we need to manipulate a creature
'''


class Creature(object):
    ''' Class representing a creature '''
    def __init__(self, base):
        ''' Builds a creature

            :param base:
                Base type of the creature
        '''
        self.base = base

    def get_name(self):
        ''' Get this creature's name

            :return:
                Name of the creature
        '''
        return "{0}".format(self.base).capitalize()

    def __str__(self):
        return "[Creature] {0}".format(self.get_name())
