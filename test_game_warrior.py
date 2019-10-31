import unittest
from game import Archer, Swordsman, LightArmy, DarkArmy


class TestLesson13(unittest.TestCase):
    def test_hitting_archer_makes_more_damage(self):
        army1 = LightArmy()
        army2 = DarkArmy()
        archer = Archer('Justin', 100, army1)
        swordsman = Swordsman('Hugo', 98, army2)
        initial_health = archer.health
        standard_damage = swordsman.damage
        swordsman.hit(archer)
        self.assertGreater(initial_health - standard_damage, archer.health)

    def test_creating_warrior_adds_him_to_the_army_warriors_list(self):
        army1 = LightArmy()
        army2 = DarkArmy()
        archer = Archer('Joseph', 110, army1)
        swordsman = Swordsman('Kyle', 12, army2)
        self.assertIn(archer, army1.warriors)
        self.assertIn(swordsman, army2.warriors)

    def test_if_health_below_zero_then_warrior_is_dead(self):
        army1 = LightArmy()
        army2 = DarkArmy()
        archer = Archer('Sam', 1, army1)
        swordsman = Swordsman('Kenneth', 100, army2)
        swordsman.hit(archer)
        self.assertEqual(archer.alive, False)
        swordsman.health = 0
        self.assertEqual(swordsman.alive, False)

    def test_if_warrior_is_dead_he_is_removed_from_warriors_list(self):
        army = LightArmy()
        warrior = Archer('Luke', 1, army)
        warrior.alive = False
        self.assertNotIn(warrior, army.warriors)