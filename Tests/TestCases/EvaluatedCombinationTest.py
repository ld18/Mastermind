
from GameLogic.Evaluation import Evaluation
from GameLogic.EvaluatedCombination import EvaluatedCombination
from twisted.trial import unittest

class Testcases(unittest.TestCase):


    def testAll(self):
        self.testFunction_eq()


    def testFunction_eq(self):
        #equal evaluations
        evaluatedCombi = EvaluatedCombination([0, 1, 2, 3], Evaluation(0, 0, False))
        self.assertEqual(evaluatedCombi == evaluatedCombi, True)
        evaluatedCombi = EvaluatedCombination([0, 1, 2, 7], Evaluation(1, 0, False))
        self.assertEqual(evaluatedCombi == evaluatedCombi, True)
        evaluatedCombi = EvaluatedCombination([4, 1, 2, 7], Evaluation(1, 1, False))
        self.assertEqual(evaluatedCombi == evaluatedCombi, True)
        evaluatedCombi = EvaluatedCombination([4, 1, 5, 7], Evaluation(1, 2, False))
        self.assertEqual(evaluatedCombi == evaluatedCombi, True)

        #unequal evaluations
        evaluatedCombi = EvaluatedCombination([0, 1, 2, 3], Evaluation(0, 0, True))
        self.assertEqual(evaluatedCombi == EvaluatedCombination([0, 1, 2, 3], Evaluation(0, 1, True)), False)
        self.assertEqual(evaluatedCombi == EvaluatedCombination([0, 1, 2, 3], Evaluation(0, 1, False)), False)

        evaluatedCombi = EvaluatedCombination([0, 1, 2, 3], Evaluation(0, 0, True))
        self.assertEqual(evaluatedCombi == EvaluatedCombination([0, 1, 5, 3], Evaluation(0, 0, True)), False)
        self.assertEqual(evaluatedCombi == EvaluatedCombination([0, 1, 5, 3], Evaluation(0, 0, False)), False)

        evaluatedCombi = EvaluatedCombination([0, 1, 2, 3], Evaluation(0, 0, True))
        self.assertEqual(evaluatedCombi == EvaluatedCombination([0, 1, 5, 3], Evaluation(1, 0, True)), False)
        self.assertEqual(evaluatedCombi == EvaluatedCombination([0, 1, 5, 3], Evaluation(1, 0, False)), False)

        evaluatedCombi = EvaluatedCombination([0, 1, 2, 3], Evaluation(0, 0, True))
        self.assertEqual(evaluatedCombi == EvaluatedCombination([7, 5, 6, 4], Evaluation(1, 6, True)), False)
        self.assertEqual(evaluatedCombi == EvaluatedCombination([7, 5, 6, 4], Evaluation(1, 6, False)), False)


if __name__ == '__main__':
    unittest.main()
