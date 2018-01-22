''' entity_creature.py

    This module provides everything we need to manipulate a creature
'''
from entities.entity_living import LivingEntity


class Creature(LivingEntity):
    ''' Class representing a creature '''
    def __init__(self, base, stats):
        ''' Builds a creature

            :param base:
                Base type of the creature
        '''
        super().__init__(base, stats)

    def __str__(self):
        description = "[Creature] {0}\n".format(self.get_name())

        for _, stat in self.stats.container.items():
            description += "   {0:3s}: {1:4d}\n".format(stat.abreviation,
                                                        stat.value)

        return description

    def get_name(self):
        ''' Get this creature's name

            :return:
                Name of the creature
        '''
        return "{0}".format(self.name).capitalize()
