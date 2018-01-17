''' entity_base.py

    This module contains an abstract class for all of the entities
'''
from abc import ABC


class BaseEntity(ABC):
    def get_name(self):
        return NotImplemented
