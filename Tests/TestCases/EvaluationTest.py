
from GameLogic.Evaluation import Evaluation
from twisted.trial import unittest

class Testcases(unittest.TestCase):

    def testAll(self):
        self.test_eq()
        self.test_gt()


    def test_eq(self):
        #equal evaluations
        self.assertEqual(Evaluation(0, 0, True) == Evaluation(0, 0, True), True)
        self.assertEqual(Evaluation(1, 0, True) == Evaluation(1, 0, True), True)
        self.assertEqual(Evaluation(0, 4, True) == Evaluation(0, 4, True), True)
        self.assertEqual(Evaluation(1, 2, True) == Evaluation(1, 2, True), True)
        self.assertEqual(Evaluation(4, 0, True) == Evaluation(4, 0, True), True)
        self.assertEqual(Evaluation(1, 1, True) == Evaluation(1, 1, True), True)
        self.assertEqual(Evaluation(0, 0, False) == Evaluation(0, 0, False), True)
        self.assertEqual(Evaluation(1, 0, False) == Evaluation(1, 0, False), True)
        self.assertEqual(Evaluation(0, 4, False) == Evaluation(0, 4, False), True)
        self.assertEqual(Evaluation(1, 2, False) == Evaluation(1, 2, False), True)
        self.assertEqual(Evaluation(4, 0, False) == Evaluation(4, 0, False), True)
        self.assertEqual(Evaluation(1, 1, False) == Evaluation(1, 1, False), True)

        #unequal evaluations
        self.assertEqual(Evaluation(1, 0, True) == Evaluation(0, 0, True), False)
        self.assertEqual(Evaluation(1, 4, True) == Evaluation(1, 0, True), False)
        self.assertEqual(Evaluation(0, 4, True) == Evaluation(0, 3, True), False)
        self.assertEqual(Evaluation(1, 2, True) == Evaluation(1, 0, True), False)
        self.assertEqual(Evaluation(4, 0, True) == Evaluation(1, 0, True), False)
        self.assertEqual(Evaluation(1, 1, True) == Evaluation(1, 2, True), False)
        self.assertEqual(Evaluation(1, 0, False) == Evaluation(0, 0, False), False)
        self.assertEqual(Evaluation(1, 4, False) == Evaluation(1, 0, False), False)
        self.assertEqual(Evaluation(0, 4, False) == Evaluation(0, 3, False), False)
        self.assertEqual(Evaluation(1, 2, False) == Evaluation(1, 0, False), False)
        self.assertEqual(Evaluation(4, 0, False) == Evaluation(1, 0, False), False)
        self.assertEqual(Evaluation(1, 1, False) == Evaluation(1, 2, False), False)


    def test_gt(self):
        #equal evaluations
        self.assertEqual(Evaluation(0, 0, True) < Evaluation(0, 0, True), False)
        self.assertEqual(Evaluation(1, 0, True) < Evaluation(1, 0, True), False)
        self.assertEqual(Evaluation(0, 4, True) < Evaluation(0, 4, True), False)
        self.assertEqual(Evaluation(1, 2, True) < Evaluation(1, 2, True), False)
        self.assertEqual(Evaluation(4, 0, True) < Evaluation(4, 0, True), False)
        self.assertEqual(Evaluation(1, 1, True) < Evaluation(1, 1, True), False)

        #unequal evaluations
        self.assertEqual(Evaluation(1, 0, True) < Evaluation(2, 0, True), True)
        self.assertEqual(Evaluation(1, 4, True) < Evaluation(1, 5, True), True)
        self.assertEqual(Evaluation(0, 2, True) < Evaluation(0, 3, True), True)
        self.assertEqual(Evaluation(1, 2, True) < Evaluation(2, 0, True), True)
        self.assertEqual(Evaluation(4, 0, True) < Evaluation(5, 0, True), True)
        self.assertEqual(Evaluation(1, 1, True) < Evaluation(1, 2, True), True)

        self.assertEqual(Evaluation(1, 0, True) < Evaluation(0, 0, True), False)
        self.assertEqual(Evaluation(1, 4, True) < Evaluation(1, 3, True), False)
        self.assertEqual(Evaluation(0, 2, True) < Evaluation(0, 1, True), False)
        self.assertEqual(Evaluation(1, 2, True) < Evaluation(1, 0, True), False)
        self.assertEqual(Evaluation(4, 0, True) < Evaluation(3, 0, True), False)
        self.assertEqual(Evaluation(1, 1, True) < Evaluation(1, 0, True), False)

        self.assertEqual(Evaluation(3, 0, True) > Evaluation(2, 0, True), True)
        self.assertEqual(Evaluation(1, 6, True) > Evaluation(1, 5, True), True)
        self.assertEqual(Evaluation(0, 2, True) > Evaluation(0, 1, True), True)
        self.assertEqual(Evaluation(2, 2, True) > Evaluation(2, 0, True), True)
        self.assertEqual(Evaluation(4, 0, True) > Evaluation(3, 0, True), True)
        self.assertEqual(Evaluation(1, 2, True) > Evaluation(1, 1, True), True)

        self.assertEqual(Evaluation(1, 0, True) > Evaluation(1, 0, True), False)
        self.assertEqual(Evaluation(1, 4, True) > Evaluation(1, 5, True), False)
        self.assertEqual(Evaluation(0, 1, True) > Evaluation(0, 2, True), False)
        self.assertEqual(Evaluation(1, 2, True) > Evaluation(1, 3, True), False)
        self.assertEqual(Evaluation(4, 0, True) > Evaluation(5, 0, True), False)
        self.assertEqual(Evaluation(1, 0, True) > Evaluation(1, 1, True), False)


if __name__ == '__main__':
    unittest.main()
