''' generator_creatures.py

    This module provides methods to generate creatures
'''
from entities.entity_creature import Creature
from generators.generator_base import BaseGenerator
from utils.random_utils import get_random_string_from_list


class CreaturesGenerator(BaseGenerator):
    ''' Class used to generate a creature '''
    # def __init__(self):

    def generate(self):
        # Load lists
        creatures_base_list = self.load_list("creatures_base")

        # Draw creature parts
        base = get_random_string_from_list(creatures_base_list)

        # Create and return creature
        creature = Creature(base)
        return creature
