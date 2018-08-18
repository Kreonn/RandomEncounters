''' main.py
    Game entry point
'''
from generators.generator_creatures import CreaturesGenerator


def main():
    ''' Main function '''
    creature = CreaturesGenerator().generate()
    print(creature)


if __name__ == "__main__":
    main()
