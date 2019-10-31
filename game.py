from abc import ABC


class Warrior(ABC):
    def __init__(self, name, health, army):
        self.name = name
        self.army = army
        self._health = health
        self._alive = True
        self.damage = 15

    def hit(self, warrior):
        if isinstance(warrior, Archer):
            self.damage = self.damage * 1.15
        if warrior.alive:
            warrior.health -= self.damage

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = value  # value is a result of operation
        if self._health <= 0:
            self.alive = False

    @property
    def alive(self):
        return self._alive

    @alive.setter
    def alive(self, value):
        self._alive = value
        if not self._alive:
            self.army.warriors.remove(self)

    def __repr__(self):
        return f'{self.name} : {self.health}'


class Swordsman(Warrior):
    def __init__(self, name, health, army):
        super().__init__(name, health, army)
        self.damage = 25
        army.warriors.append(self)


class Archer(Warrior):
    def __init__(self, name, health, army):
        super().__init__(name, health, army)
        self.damage = 20
        army.warriors.append(self)


class Army(ABC):
    def __init__(self):
        self.warriors = []

    def train_swordsman(self, name, health):
        warrior = Swordsman(name, health, self)
        self.warriors.append(warrior)
        return warrior

    def train_archer(self, name, health):
        warrior = Archer(name, health, self)
        self.warriors.append(warrior)
        return warrior


class DarkArmy(Army):
    def __repr__(self):
        return 'Dark Army'


class LightArmy(Army):
    def __repr__(self):
        return 'Light Army'


