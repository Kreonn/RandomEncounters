from definitions import ROOT_DIR
from yaml import load, CLoader, YAMLError


def load_yaml(dictionary_name):
    ''' Loads a list inside a YAML file by name

        :param dictionary_name:
            Name of the dictionary in db/, without extension

        :return:
            Loaded list if success, empty list if failed
    '''
    file_path = ROOT_DIR + "/db/" + dictionary_name + ".yml"
    result_list = []

    with open(file_path, mode='r') as yml_file:
        try:
            result_list = load(yml_file, Loader=CLoader)[dictionary_name]
        except YAMLError as e:
            print("Error while parsing YAML file ({0})".format(e))

    return result_list
