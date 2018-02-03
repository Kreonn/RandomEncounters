''' battle.py

    This module contains the rules of battle in the game
'''


class TurnReport(object):
    ''' Class representing the result of a turn '''
    def __init__(self, actor, action):
        self.actor = actor
        self.action = action


class Battle(object):
    ''' Class representing a battle instance '''
    def __init__(self, player, creature):
        self.player = player
        self.creature = creature
        self.turn = 1
        self.is_player_turn = self.__get_turn_order()

    def execute_turn(self, action):
        ''' Apply an action for the current turn '''
        actor = "player" if self.is_player_turn else "creature"
        turn_report = TurnReport(actor, action)

        self.turn += 1

        return turn_report

    def __get_turn_order(self):
        ''' Get whether the player plays first

            :return: True if the player plays first, False otherwise
        '''
        return True
