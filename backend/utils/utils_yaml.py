''' utils_yaml.py

    Provides function to manipulate yaml files
'''
from yaml import load, CLoader, YAMLError
from definitions import DB_DIR, TESTS_FIXTURES_DIR


def load_yaml(dictionary_name, test_mode=False):
    ''' Loads a list or a dictionary from a YAML file by name

        :param dictionary_name:
            Name of the dictionary in db/, without extension

        :param test_mode:
            Determine whether the file should be looked for in db/ or fixtures/

        :return:
            Loaded list if success, empty list if failed
    '''
    if test_mode:
        file_path = TESTS_FIXTURES_DIR + dictionary_name + ".yml"
    else:
        file_path = DB_DIR + dictionary_name + ".yml"
    result_list = []

    try:
        with open(file_path, mode='r') as yml_file:
            result_list = load(yml_file, Loader=CLoader)[dictionary_name]
    except YAMLError as yaml_err:
        print("Error while parsing YAML file ({0})".format(yaml_err))
        raise YAMLError
    except FileNotFoundError:
        print("File {0} does not exist".format(file_path))
        raise FileNotFoundError

    return result_list
