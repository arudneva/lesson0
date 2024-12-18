import unittest
import tests_12_3

TS = unittest.TestSuite()
TS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))
TS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(TS)

