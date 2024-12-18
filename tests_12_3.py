import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)


    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == False, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        runner = Runner("Mike")
        for i in range(10):
            runner.walk()

        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen == False, "Тесты в этом кейсе заморожены")
    def test_run(self):
        runner = Runner("Bob")
        for i in range(10):
            runner.run()

        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen == False, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        runner1 = Runner("Robby")
        runner2 = Runner("Bobby")
        for i in range(10):
            runner1.walk()
            runner2.run()

        self.assertNotEqual(runner1.distance, runner2.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Usain", speed=10)
        self.runner2 = Runner("Andrey", speed=9)
        self.runner3 = Runner("Nick", speed=3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    @unittest.skipIf(is_frozen == False, "Тесты в этом кейсе заморожены")
    def test_race_usain_nick(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        result = tournament.start()
        self.all_results[max(result)] = result[max(result)].name
        self.assertFalse(result[max(result)].name == "Usain")

    @unittest.skipIf(is_frozen == False, "Тесты в этом кейсе заморожены")
    def test_race_andrey_nick(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        result = tournament.start()
        self.all_results[max(result)] = result[max(result)].name
        self.assertFalse(result[max(result)].name == "Andrey")

    @unittest.skipIf(is_frozen == False, "Тесты в этом кейсе заморожены")
    def test_race_all(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        result = tournament.start()
        self.all_results[max(result)] = result[max(result)].name
        self.assertTrue(result[max(result)].name == "Nick")


if __name__ == "__main__":
    unittest.main()