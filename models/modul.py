from abc import ABC, abstractmethod
from enum import Enum


class Modul(ABC):
    class Type(Enum):
        Active: int = 1
        Passive: int = 2

    def __init__(self,
                 modul_name: str = "Modul name not defined.",
                 modul_type: Type = Type.Passive,
                 hp: float = 0,
                 armor: float = 0,
                 shields: float = 0,
                 lasers: float = 0,
                 rockets: float = 0,
                 kinetic: float = 0,
                 ):
        self.modul_name = modul_name
        self.modul_type: Modul.Type = modul_type

        self.hp: float = hp
        self.armor: float = armor
        self.shields: float = shields

        self.lasers: float = lasers
        self.rockets: float = rockets
        self.kinetic: float = kinetic

    @abstractmethod
    def do_action(self):
        pass


class Active_Modul(Modul):

    def do_action(self):
        pass


class Passive_Modul(Modul):

    def do_action(self):
        pass
