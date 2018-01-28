''' entity_base.py

    This module contains an abstract class for all of the entities
'''
from abc import ABC, abstractmethod


class BaseEntity(ABC):
    def __init__(self, name):
        self.name = name
        super().__init__()

    @abstractmethod
    def get_name(self):
        raise NotImplementedError
