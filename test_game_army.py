import unittest
from game import DarkArmy, LightArmy, Swordsman, Archer


class TestLesson13(unittest.TestCase):
    def test_train_swordsman_returns_swordsman(self):
        army = DarkArmy()
        a = army.train_swordsman('John', 100)
        self.assertIsInstance(a, Swordsman)

    def test_train_archer_returns_archer(self):
        army = LightArmy()
        a = army.train_archer('Steve', 120)
        self.assertIsInstance(a, Archer)

    def test_creating_warriors_extends_warriors_list(self):
        army1 = LightArmy()
        army2 = DarkArmy()
        archer = army1.train_archer('Max', 50)
        swordsman = army2.train_swordsman('Joe', 120)
        self.assertIn(archer, army1.warriors)
        self.assertIn(swordsman, army2.warriors)

    def test_repr_check(self):
        self.assertEqual(repr(LightArmy()), 'Light Army')
        self.assertEqual(repr(DarkArmy()), 'Dark Army')
