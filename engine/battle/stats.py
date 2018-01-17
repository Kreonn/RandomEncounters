''' stats.py

    This module contains a class representing combat stats
'''


class Stats(object):
    def __init__(self, level=1, max_hp=20, max_mp=5, strength=5,
                 intelligence=5, dexterity=5, faith=5, constitution=5,
                 willpower=5, sin=5):
        self.level = level
        self.max_hp = max_hp
        self.max_mp = max_mp
        self.strength = strength
        self.intelligence = intelligence
        self.dexterity = dexterity
        self.faith = faith
        self.constitution = constitution
        self.willpower = willpower
        self.sin = sin
