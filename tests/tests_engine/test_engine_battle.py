''' test_engine_battle.py

    Unit tests for battle.py
'''
import pytest
from entities.entity_player import Player
from entities.entity_creature import Creature
from engine.stats import StatsContainer
from engine.actions import ActionResult
from engine.battle import Battle, TurnReport


class TestEngineBattle(object):
    ''' Unit tests container for Battle '''

    @pytest.fixture
    def creature(self):
        ''' Creature fixture '''
        return Creature("Test", 1, 20, 5, StatsContainer(), "strength")

    @pytest.fixture
    def player(self):
        ''' Player fixture '''
        return Player("Player", 1, 25, 5, StatsContainer())

    @pytest.fixture
    def battle(self, player, creature):
        ''' Battle fixture '''
        return Battle(player, creature)

    def test_battle_constructor(self, battle):
        ''' Test for battle constructor '''
        assert battle.turn == 1
        assert isinstance(battle.creature, Creature)
        assert isinstance(battle.player, Player)

    def test_battle_execute_turn(self, battle):
        ''' Test for execute_turn method '''
        battle.is_player_turn = True
        turn_report = battle.execute_turn("attack")

        assert battle.turn == 2
        assert isinstance(turn_report, TurnReport)
        assert isinstance(turn_report.actor, Player)
        assert isinstance(turn_report.action_result, ActionResult)
        assert turn_report.action == "attack"

        turn_report = battle.execute_turn("attack")

        assert battle.turn == 3
        assert isinstance(turn_report, TurnReport)
        assert isinstance(turn_report.actor, Creature)
        assert isinstance(turn_report.action_result, ActionResult)
        assert turn_report.action == "attack"
