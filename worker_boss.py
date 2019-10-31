# Add a new method to our Worker-Boss program to the Boss class.
# This method is called (dump_workers). It must take all workers from
# workers list and output them into a .csv file (just the way we did it)
#
# Extra point for doing it using built-in csv library
# Extra point for doing it using 3rd party library pandas


from random import randint
from abc import ABC
import csv


class Person(ABC):
    def __init__(self, id: int, name: str, company: str):
        self.id = id
        self.name = name
        self.company = company
        self.id = randint(1, 101)


class Boss(Person):
    def __init__(self, id: int, name: str, company: str):
        super().__init__(id, name, company)
        self.workers = set()

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self.workers.add(worker)

    def dump_workers(self):
        with open('files/workers.csv', mode='w') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(self.workers)

    def __repr__(self):
        return f'{self.id} | {self.name} | {self.company}'


class Worker(Person):
    def __init__(self, id: int, name: str, company: str, boss: Boss):
        super().__init__(id, name, company)
        self._boss = boss
        self._boss.workers.add(self)

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if isinstance(new_boss, Boss):
            self._boss.workers.remove(self)
            self._boss = new_boss
            self._boss.workers.add(self)
            self.company = new_boss.company

    def __repr__(self):
        return f'{self.name}'

