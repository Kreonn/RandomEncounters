''' test_entities_creature.py

    Unit tests for entity_creature.py
'''
import pytest
from entities.entity_creature import Creature
from engine.stats import StatsContainer


class TestEntitiesCreature(object):
    ''' Unit tests container for entity_creature '''

    @pytest.fixture
    def creature(self):
        ''' Creature fixture '''
        return Creature("test", 1, 20, 5, StatsContainer())

    def test_creature_constructor(self, creature):
        ''' Test for creature building '''
        assert isinstance(creature, Creature)
        assert creature.name == "test"
        assert creature.level == 1
        assert creature.max_hp == 20
        assert creature.max_mp == 5
        assert isinstance(creature.stats, StatsContainer)

    def test_creature_str(self, creature):
        ''' Test for creature __str__ function '''
        assert "[Creature]" in creature.__str__()

    def test_creature_get_name(self, creature):
        ''' Test for creature get_name function '''
        assert creature.get_name() == "Test"
