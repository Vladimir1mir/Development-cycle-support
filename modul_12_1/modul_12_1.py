
from runner import Runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner("RunnerName")
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner("RunnerName")
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = Runner("RunnerName1")
        runner2 = Runner("RunnerName2")
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)
        self.assertEqual(runner1.distance, 100)
        self.assertEqual(runner2.distance, 50)

if __name__ == '__main__':
    unittest.main()
