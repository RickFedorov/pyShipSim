import unittest
from models.ship import Ship
from models.modul import Modul, Active_Modul, Passive_Modul
from models.battle import Battle

class MyTestCase(unittest.TestCase):
    def test_ships_load(self):
        ship1 = Ship("Ship #1")
        ship2 = Ship("Ship #2")

        self.assertEqual(ship1.ship_name, "Ship #1")
        self.assertEqual(ship2.ship_name, "Ship #2")

    def test_ships_with_modules(self):
        ship = Ship("Ship with modules",
                    modules=[Active_Modul("Active Module"),
                             Passive_Modul("Passive Module")]
                    )

        self.assertEqual(len(ship.modules),2)

    def test_ships_with_modules_prop(self):
        ship = Ship("Ship with modules",
                    modules=[Active_Modul("Active Module",modul_type=Modul.Type.Active,lasers=1000),
                             Passive_Modul("Passive Module",modul_type=Modul.Type.Passive,hp=1000)]
                    )

        self.assertEqual(len(ship.get_modules(Modul.Type.Active)), 1)
        self.assertEqual(len(ship.get_modules(Modul.Type.Passive)), 1)

        self.assertEqual(ship.get_modules(Modul.Type.Active)[0].lasers, 1000)
        self.assertEqual(ship.get_modules(Modul.Type.Passive)[0].hp, 1000)

        ship1 = Ship("Ship #1",
                    modules=[Active_Modul("Active Module",modul_type=Modul.Type.Active,lasers=1000),
                             Passive_Modul("Passive Module",modul_type=Modul.Type.Passive,hp=1000)]
                    )

        ship2 = Ship("Ship #2",
                    modules=[Active_Modul("Active Module",modul_type=Modul.Type.Active,lasers=1000),
                             Passive_Modul("Passive Module",modul_type=Modul.Type.Passive,hp=1000)]
                    )

        battle = Battle(ship1,ship2)
        self.assertTrue(battle.attacker != battle.defender)


if __name__ == '__main__':
    unittest.main()
