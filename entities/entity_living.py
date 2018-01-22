''' entity_living.py

    This module provides a base class for living entities
'''
from entities.entity_base import BaseEntity


class LivingEntity(BaseEntity):
    ''' Class representing a living entity '''
    def __init__(self, name, stats):
        ''' Builds a living creature

            :param name:
                Name of the living entity
            
            :param stats:
                StatsContainer of this entity
        '''
        super().__init__(name)
        self.stats = stats
