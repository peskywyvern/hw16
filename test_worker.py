import unittest
from worker_boss import Worker, Boss


class TestWorker(unittest.TestCase):
    def test_created_worker_is_added_to_workers_list(self):
        boss = Boss(1, 'Elon Musk', 'Tesla')
        worker = Worker(2, 'Joe', 'Tesla', boss)
        self.assertIn(worker, boss.workers)

    def test_changing_boss_transfers_worker_to_new_boss_list(self):
        boss1 = Boss(1, 'Elon Musk', 'Tesla')
        boss2 = Boss(2, 'Jeff Bezos', 'Blue Origin')
        worker = Worker(3, 'Jim', 'Tesla', boss1)
        worker.boss = boss2
        self.assertIn(worker, boss2.workers)
        self.assertNotIn(worker, boss1.workers)

    def test_changing_boss_changes_company_name_attribute(self):
        boss1 = Boss(1, 'Elon Musk', 'Tesla')
        boss2 = Boss(2, 'Jeff Bezos', 'Blue Origin')
        worker = Worker(3, 'Jim', 'Tesla', boss1)
        worker.boss = boss2
        self.assertEqual(worker.company, boss2.company)

    def repr_check(self):
        boss = Boss(1, 'Elon Musk', 'Tesla')
        worker = Worker(1, 'Kelsie', 'Tesla', boss)
        self.assertEqual(repr(worker), worker.name)
