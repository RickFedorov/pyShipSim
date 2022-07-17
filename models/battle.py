import random
from typing import Optional
from .ship import Ship


class Battle():

    def __init__(self, ship1: Ship, ship2: Ship):
        self.attacker: Optional[Ship] = None
        self.attacker: Optional[Ship] = None

        self.attacker, self.defender = self.rand_ship_order(ship1, ship2)



    def rand_ship_order(self, ship1: Ship, ship2: Ship):

        same_value = True

        while same_value:
            if random.randint(1, 6) > random.randint(1, 6):
                return ship1, ship2
            if random.randint(1, 6) < random.randint(1, 6):
                return ship2, ship1
