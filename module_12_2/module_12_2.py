from runner_and_tournament import Runner, Tournament
import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runer_name1 = Runner('Усэйн', 10)
        self.runer_name2 = Runner('Андрей', 9)
        self.runer_name3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        result = {}
        for testkey, testval in cls.all_results.items():
            for key, val in testval.items():
                result[key] = str(val.name)
            print(result)

    # метода тестирования
    def testrun_1(self):
        run_1 = Tournament(90, self.runer_name1, self.runer_name3)
        finish = run_1.start()
        self.assertTrue(list(finish.values())[-1].name == str(self.runer_name3))
        self.all_results[f'{self.runer_name1}, {self.runer_name3}'] = finish

    def testrun_2(self):
        run_1 = Tournament(90, self.runer_name2, self.runer_name3)
        finish = run_1.start()
        self.assertTrue(list(finish.values())[-1].name == str(self.runer_name3))
        self.all_results[f'{self.runer_name2}, {self.runer_name3}'] = finish

    def testrun_3(self):
        run_1 = Tournament(90, self.runer_name1, self.runer_name2, self.runer_name3)
        finish = run_1.start()
        self.assertTrue(list(finish.values())[-1].name == str(self.runer_name3))
        self.all_results[f'{self.runer_name1}, {self.runer_name2}, {self.runer_name3}'] = finish


if __name__ == "__main__":
    unittest.main()