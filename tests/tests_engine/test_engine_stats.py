''' test_engine_stats.py

    Unit tests for stats.py
'''
from utils.utils_yaml import load_yaml
from engine.stats import Stat, StatsContainer


class TestEngineStats(object):
    ''' Unit Tests container for stats '''

    def test_stat(self):
        ''' Test for Stat class '''
        stat = Stat("test_display", "test_abv", "test_categ", "test_counter", 1)

        assert stat.display_name == "test_display"
        assert stat.abreviation == "test_abv"
        assert stat.category == "test_categ"
        assert stat.counter == "test_counter"
        assert stat.value == 1

    def test_stats_container(self):
        ''' Test for StatsContainer class '''
        stats_yaml = load_yaml("stats")
        stats = StatsContainer()

        assert stats.container
        assert len(stats.container) == len(stats_yaml)
