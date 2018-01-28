''' test_utils_yaml.py

    Unit tests for utils_yaml
'''
import pytest
from yaml import YAMLError
from utils.utils_yaml import load_yaml


class TestUtilsYaml(object):
    ''' Unit tests container for utils_yaml '''

    def test_load_yaml_list(self):
        ''' Test for yaml list loading '''
        expected_result = ["test_1", "test_2", "test_3", "test_4", "test_5"]
        yaml_list = load_yaml("fixture_yaml_list", test_mode=True)

        assert isinstance(yaml_list, list)
        assert yaml_list == expected_result

    def test_load_yaml_dict(self):
        ''' Test for yaml dictionary loading '''
        expected_result = {
            "test_1": {
                "string": "test_1",
                "integer": 1
            },
            "test_2": {
                "string": "test_2",
                "integer": 2
            },
            "test_3": {
                "string": "test_3",
                "integer": 3
            }
        }
        yaml_dict = load_yaml("fixture_yaml_dict", test_mode=True)

        assert isinstance(yaml_dict, dict)
        assert yaml_dict == expected_result

    def test_load_yaml_prod(self):
        ''' Test for real yaml files '''
        yaml = load_yaml("stats", test_mode=False)
        assert yaml

    def test_load_yaml_exception(self):
        ''' Test for load_yaml failure '''
        with pytest.raises(FileNotFoundError):
            load_yaml("fake_yaml_file", test_mode=True)

        with pytest.raises(YAMLError):
            load_yaml("fixture_yaml_fail", test_mode=True)
