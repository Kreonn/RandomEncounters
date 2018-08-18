''' test_entities_player.py

    Unit tests for entity_player.py
'''
import pytest
from entities.entity_player import Player
from engine.stats import Stat, StatsContainer


class TestEntitiesCreature(object):
    ''' Unit tests container for entity_player '''

    @pytest.fixture
    def player(self):
        ''' Creature fixture '''
        return Player("test", 1, 20, 5, StatsContainer())

    def test_player_constructor(self, player):
        ''' Test for player building '''
        assert isinstance(player, Player)
        assert player.name == "test"
        assert player.level == 1
        assert player.max_hp == 20
        assert player.max_mp == 5
        assert isinstance(player.stats, StatsContainer)

    def test_player_str(self, player):
        ''' Test for player __str__ function '''
        assert "[Player]" in player.__str__()

    def test_player_get_name(self, player):
        ''' Test for player get_name function '''
        assert player.get_name() == "Test"

    def test_player_get_main_stat(self, player):
        main_stat = player.get_main_stat()

        assert isinstance(main_stat, Stat)
        assert main_stat.display_name == "Strength"

    def test_player_is_alive(self, player):
        assert player.is_alive()

        player.current_hp = 0

        assert not player.is_alive()
