
from GameLogic.Evaluation import Evaluation
from twisted.trial import unittest

class EvaluationTest(unittest.TestCase):

    def testFunction_Constructor(self):
        #valid construcotrs
        for wrongPlace in range(0, 2):
            for rightPlace in range(0, 2):
                #print(str(wrongPlace) +" "+ str(rightPlace))
                sud = Evaluation(wrongPlace, rightPlace)

    def testError_Constructor(self):
        #invalid construcotrs
        for wrongPlace in range(-2, 0):
            for rightPlace in range(-2, 0):
                with self.assertRaises(ValueError):
                    #print(str(wrongPlace) +" "+ str(rightPlace))
                    sud = Evaluation(wrongPlace, rightPlace)

    def test_eq(self):
        #equal evaluations
        self.assertEqual(Evaluation(0, 0) == Evaluation(0, 0), True)
        self.assertEqual(Evaluation(1, 0) == Evaluation(1, 0), True)
        self.assertEqual(Evaluation(0, 4) == Evaluation(0, 4), True)
        self.assertEqual(Evaluation(1, 2) == Evaluation(1, 2), True)
        self.assertEqual(Evaluation(4, 0) == Evaluation(4, 0), True)
        self.assertEqual(Evaluation(1, 1) == Evaluation(1, 1), True)

        #unequal evaluations
        self.assertEqual(Evaluation(1, 0) == Evaluation(0, 0), False)
        self.assertEqual(Evaluation(1, 4) == Evaluation(1, 0), False)
        self.assertEqual(Evaluation(0, 4) == Evaluation(0, 3), False)
        self.assertEqual(Evaluation(1, 2) == Evaluation(1, 0), False)
        self.assertEqual(Evaluation(4, 0) == Evaluation(1, 0), False)
        self.assertEqual(Evaluation(1, 1) == Evaluation(1, 2), False)

    def test_gt(self):
        #equal evaluations
        self.assertEqual(Evaluation(0, 0) < Evaluation(0, 0), False)
        self.assertEqual(Evaluation(1, 0) < Evaluation(1, 0), False)
        self.assertEqual(Evaluation(0, 4) < Evaluation(0, 4), False)
        self.assertEqual(Evaluation(1, 2) < Evaluation(1, 2), False)
        self.assertEqual(Evaluation(4, 0) < Evaluation(4, 0), False)
        self.assertEqual(Evaluation(1, 1) < Evaluation(1, 1), False)

        #unequal evaluations
        self.assertEqual(Evaluation(1, 0) < Evaluation(2, 0), True)
        self.assertEqual(Evaluation(1, 4) < Evaluation(1, 5), True)
        self.assertEqual(Evaluation(0, 2) < Evaluation(0, 3), True)
        self.assertEqual(Evaluation(1, 2) < Evaluation(2, 0), True)
        self.assertEqual(Evaluation(4, 0) < Evaluation(5, 0), True)
        self.assertEqual(Evaluation(1, 1) < Evaluation(1, 2), True)

        self.assertEqual(Evaluation(1, 0) < Evaluation(0, 0), False)
        self.assertEqual(Evaluation(1, 4) < Evaluation(1, 3), False)
        self.assertEqual(Evaluation(0, 2) < Evaluation(0, 1), False)
        self.assertEqual(Evaluation(1, 2) < Evaluation(1, 0), False)
        self.assertEqual(Evaluation(4, 0) < Evaluation(3, 0), False)
        self.assertEqual(Evaluation(1, 1) < Evaluation(1, 0), False)

        self.assertEqual(Evaluation(3, 0) > Evaluation(2, 0), True)
        self.assertEqual(Evaluation(1, 6) > Evaluation(1, 5), True)
        self.assertEqual(Evaluation(0, 2) > Evaluation(0, 1), True)
        self.assertEqual(Evaluation(2, 2) > Evaluation(2, 0), True)
        self.assertEqual(Evaluation(4, 0) > Evaluation(3, 0), True)
        self.assertEqual(Evaluation(1, 2) > Evaluation(1, 1), True)

        self.assertEqual(Evaluation(1, 0) > Evaluation(1, 0), False)
        self.assertEqual(Evaluation(1, 4) > Evaluation(1, 5), False)
        self.assertEqual(Evaluation(0, 1) > Evaluation(0, 2), False)
        self.assertEqual(Evaluation(1, 2) > Evaluation(1, 3), False)
        self.assertEqual(Evaluation(4, 0) > Evaluation(5, 0), False)
        self.assertEqual(Evaluation(1, 0) > Evaluation(1, 1), False)

if __name__ == '__main__':
    unittest.main()
