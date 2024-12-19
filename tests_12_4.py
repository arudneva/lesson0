import logging
import unittest


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name



class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            logging.info('"test_walk" выполнен успешно')
            runner = Runner("Mike")
            for i in range(10):
                runner.walk()

            self.assertEqual(runner.distance, 50)

        except:
            logging.warning("Неверная скорость для Runner")

    def test_run(self):
        try:
            logging.info('"test_run" выполнен успешно')
            runner = Runner("Bob")
            for i in range(10):
                runner.run()

            self.assertEqual(runner.distance, 100)

        except:
            logging.warning("Неверный тип данных для объекта Runner")

    def test_challenge(self):
        runner1 = Runner("Robby")
        runner2 = Runner("Bobby")
        for i in range(10):
            runner1.walk()
            runner2.run()

        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO, filemode= "w", filename= "runner_tests.log", encoding= "UTF-8", format = "%(asctime)s | %(levelname)s | %(message)s")

    unittest.main()

first = Runner('Вося', 10)
second = Runner('Илья', 5)
third = Runner('Арсен', 10)
#
# t = Tournament(101, first, second)
# print(t.start())