''' entity_living.py

    This module provides a base class for living entities
'''
from abc import abstractmethod
from entities.entity_base import BaseEntity


class LivingEntity(BaseEntity):
    ''' Class representing a living entity '''
    def __init__(self, name, level, max_hp, max_mp, stats, main_stat="strength"):
        ''' Builds a living creature

            :param name:
                Name of the living entity

            :param stats:
                StatsContainer of this entity
        '''
        super().__init__(name)
        self.level = level
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.max_mp = max_mp
        self.current_mp = max_mp
        self.stats = stats
        self.main_stat = main_stat

    def get_main_stat(self):
        return self.stats.get_stat(self.main_stat)

    def is_alive(self):
        return self.current_hp > 0
