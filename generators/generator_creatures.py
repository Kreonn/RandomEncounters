''' generator_creatures.py

    This module provides methods to generate creatures
'''
from generators.generator_base import BaseGenerator
from entities.entity_creature import Creature
from engine.battle.stats import StatsContainer
from utils.utils_random import get_random_string_from_list


class CreaturesGenerator(BaseGenerator):
    ''' Class used to generate a creature '''
    # def __init__(self):

    def generate(self):
        # Load lists
        creatures_base_list = self.load_db("creatures_base")

        # Draw creature parts
        base = get_random_string_from_list(creatures_base_list)
        stats = StatsContainer()

        # Create and return creature
        creature = Creature(base, stats)
        return creature
