import unittest
from worker_boss import Worker, Boss, Person


class TestBoss(unittest.TestCase):
    def test_add_workers_works_only_with_workers(self):
        boss = Boss(1, 'Joshua', 'Tesla')
        another_boss = Boss(2, 'Kim', 'Samsung')
        person = Person(3, 'Jim', 'Apple')
        worker = (4, 'Pete', 'Samsung', another_boss)
        self.assertFalse(boss.add_worker(another_boss))
        self.assertFalse(boss.add_worker(person))
        self.assertTrue(boss.add_worker(worker))

    def test_add_workers_method_adds_them_to_workers_set(self):
        boss = Boss(1, 'Joshua', 'Tesla')
        another_boss = Boss(2, 'Kim', 'Samsung')
        worker = Worker(4, 'Pete', 'Samsung', another_boss)
        boss.add_worker(worker)
        self.assertIn(worker, boss.workers)