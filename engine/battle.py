''' battle.py

    This module contains the rules of battle in the game
'''
from engine.actions import Attack


class TurnReport(object):
    ''' Class representing the result of a turn '''
    def __init__(self, actor, action, action_result):
        self.actor = actor
        self.action = action
        self.action_result = action_result


class Battle(object):
    ''' Class representing a battle instance '''
    def __init__(self, player, creature):
        self.player = player
        self.creature = creature
        self.turn = 1
        self.is_player_turn = self.__get_turn_order()
        self.actions = {
            "attack": Attack()
        }

    def execute_turn(self, action, **kwargs):
        ''' Apply an action for the current turn '''
        if self.is_player_turn:
            actor = self.player
            target = self.creature
        else:
            actor = self.creature
            target = self.player

        action_result = self.actions[action].execute_action(actor,
                                                            target,
                                                            **kwargs)

        self.turn += 1
        self.is_player_turn = not self.is_player_turn

        turn_report = TurnReport(actor, action, action_result)
        return turn_report

    def __get_turn_order(self):
        ''' Get whether the player plays first

            :return: True if the player plays first, False otherwise
        '''
        return True
