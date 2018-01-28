''' test_generators_creature.py

    Unit tests for generator_creature.py
'''
import pytest
from entities.entity_creature import Creature
from generators.generator_creatures import CreaturesGenerator


class TestGeneratorsCreature(object):
    ''' Unit tests container for generator_creature '''

    @pytest.fixture
    def generator(self):
        ''' Generator fixture '''
        return CreaturesGenerator()

    def test_generate(self, generator):
        ''' Test for creature generator's generate function '''
        creature = generator.generate()

        assert isinstance(creature, Creature)
