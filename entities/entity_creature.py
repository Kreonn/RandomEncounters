''' entity_creature.py

    This module provides everything we need to manipulate a creature
'''
from entities.entity_living import LivingEntity


class Creature(LivingEntity):
    ''' Class representing a creature '''
    def __init__(self, base, level, max_hp, max_mp, stats):
        ''' Builds a creature '''
        super().__init__(base, level, max_hp, max_mp, stats)

    def __str__(self):
        description = "[Creature] {0} Lvl.{1}\n".format(self.get_name(),
                                                        self.level)

        description += "HP: {0:4d}/{1:4d}".format(self.current_hp,
                                                  self.max_hp)
        description += "\tMP: {0:4d}/{1:4d}\n".format(self.current_mp,
                                                      self.max_mp)

        for _, stat in self.stats.container.items():
            description += "    {0:3s}: {1:4d}\n".format(stat.abreviation,
                                                         stat.value)

        return description

    def get_name(self):
        ''' Get this creature's name

            :return:
                Name of the creature
        '''
        return "{0}".format(self.name).capitalize()
