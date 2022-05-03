class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


import unittest
class TestWorker(unittest.TestCase):
    def test_worker_initializing(self):
        worker = Worker("Test", 1000, 10)

        self.assertEqual(1000, worker.salary)
        self.assertEqual(10, worker.energy)
        self.assertEqual("Test", worker.name)
        self.assertEqual(0, worker.money)

    def test_worker_energy_after_taking_rest(self):
        worker = Worker("Test", 1000, 10)

        self.assertEqual(10, worker.energy)
        worker.rest()
        self.assertEqual(11, worker.energy)
        worker.rest()
        self.assertEqual(12, worker.energy)

    def test_if_error_raised_after_tries_work_with_zero_energy(self):
        worker = Worker("Test", 1000, 0)

        self.assertEqual(0, worker.energy)

        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_if_error_raised_after_tries_work_with_negative_energy(self):
        worker = Worker("Test", 1000, -10)

        self.assertEqual(-10, worker.energy)

        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_correct_money_increasing_after_work(self):
        worker = Worker("Test", 1000, 10)
        self.assertEqual(0, worker.money)
        worker.work()
        self.assertEqual(1000, worker.money)
        worker.work()
        self.assertEqual(2000, worker.money)

    def test_energy_is_decreased_correctly_after_work(self):
        worker = Worker("Test", 1000, 10)
        self.assertEqual(10, worker.energy)
        worker.work()
        self.assertEqual(9, worker.energy)
        worker.work()
        self.assertEqual(8, worker.energy)

    def test_get_info_method_return_correct_values(self):
        worker = Worker("Test", 1000, 10)
        expected_result = "Test has saved 0 money."
        self.assertEqual(expected_result, worker.get_info())


if __name__ == "__main__":
    unittest.main()