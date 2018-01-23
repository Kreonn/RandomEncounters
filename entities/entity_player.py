''' entity_player.py

    This module provides everything we need to manipulate the player
'''
from entities.entity_living import LivingEntity
from engine.battle.stats import StatsContainer


class Player(LivingEntity):
    ''' Class representing the player's character '''
    def __init__(self, name: str, level: int, max_hp: int,
                 max_mp: int, stats: StatsContainer):
        ''' Builds a player '''
        super().__init__(name, level, max_hp, max_mp, stats)
        self.experience = 0

    def __str__(self):
        description = "[Player] {0} Lvl.{1}\n".format(self.get_name(),
                                                      self.level)

        description += "HP: {0:4d}/{1:4d}".format(self.current_hp,
                                                  self.max_hp)
        description += "    MP: {0:4d}/{1:4d}\n".format(self.current_mp,
                                                        self.max_mp)

        for _, stat in self.stats.container.items():
            description += "    {0:3s}: {1:4d}\n".format(stat.abreviation,
                                                         stat.value)

        return description
