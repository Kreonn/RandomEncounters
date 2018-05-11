''' test_engine_actions

    Unit tests for actions.py
'''
import pytest
from entities.entity_player import Player
from entities.entity_creature import Creature
from engine.stats import StatsContainer
from engine.actions import ActionResult, Attack


class TestEngineActions(object):
    ''' Unit tests container for Action '''

    @pytest.fixture
    def creature(self):
        ''' Creature fixture '''
        return Creature("Test", 1, 12, 5, StatsContainer(), "strength")

    @pytest.fixture
    def player(self):
        ''' Player fixture '''
        return Player("Player", 1, 25, 5, StatsContainer())

    def test_actions_attack(self, player, creature):
        action = Attack()
        assert action.action_display == "attack"

        action_result = action.execute_action(player, creature)
        assert isinstance(action_result, ActionResult)

        while creature.is_alive():
            action.execute_action(player, creature)

        assert not creature.is_alive()
