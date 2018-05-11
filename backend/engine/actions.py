''' actions.py

    This module contains classes representing actions in battle
'''
from abc import ABC, abstractmethod
from enum import Enum


class ActionResult(Enum):
    SUCCESS = 1
    FAILURE = 2


class Action(ABC):
    ''' Abstract class representing a battle action '''
    def __init__(self, action_display):
        self.action_display = action_display

    @abstractmethod
    def execute_action(self, actor, target, **kwargs):
        ''' Execute the action '''
        raise NotImplementedError


class Attack(Action):
    ''' Basic attack action '''
    def __init__(self):
        super().__init__(action_display="attack")

    def execute_action(self, actor, target):
        actor_stat = actor.get_main_stat()
        target_stat = target.stats.get_stat(actor_stat.counter)

        damage = actor_stat.value * 2 - target_stat.value
        target.current_hp -= damage
        if target.current_hp < 0:
            target.current_hp = 0

        return ActionResult.SUCCESS
