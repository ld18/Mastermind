
from GameLogic.Evaluator import Evaluator
from GameLogic.Attempts import Attempts
from GameLogic.Evaluation import Evaluation
from twisted.trial import unittest

class EvaluationTest(unittest.TestCase):

    def testFunction_getBestAttempt(self):
        evaluator = Evaluator([0, 1, 2, 3], 8)
        attempts = Attempts(evaluator)

        evaluatedCombi =Attempts.EvaluatedCombination([4, 5, 6, 7], Evaluation(0, 0))
        attempts.evaluateAndAddCombination(evaluatedCombi.colorCombination)
        self.assertEqual(attempts.getLastAttempt() == evaluatedCombi, True)
        self.assertEqual(attempts.getBestAttempt() == Attempts.EvaluatedCombination([4, 5, 6, 7], Evaluation(0, 0)), True)

        evaluatedCombi =Attempts.EvaluatedCombination([5, 6, 7, 0], Evaluation(1, 0))
        attempts.evaluateAndAddCombination(evaluatedCombi.colorCombination)
        self.assertEqual(attempts.getLastAttempt() == evaluatedCombi, True)
        self.assertEqual(attempts.getBestAttempt() == Attempts.EvaluatedCombination([5, 6, 7, 0], Evaluation(1, 0)), True)

        evaluatedCombi =Attempts.EvaluatedCombination([5, 1, 7, 0], Evaluation(1, 1))
        attempts.evaluateAndAddCombination(evaluatedCombi.colorCombination)
        self.assertEqual(attempts.getLastAttempt() == evaluatedCombi, True)
        self.assertEqual(attempts.getBestAttempt() == Attempts.EvaluatedCombination([5, 1, 7, 0], Evaluation(1, 1)), True)

        evaluatedCombi =Attempts.EvaluatedCombination([5, 6, 7, 0], Evaluation(1, 0))
        attempts.evaluateAndAddCombination(evaluatedCombi.colorCombination)
        self.assertEqual(attempts.getLastAttempt() == evaluatedCombi, True)
        self.assertEqual(attempts.getBestAttempt() == Attempts.EvaluatedCombination([5, 1, 7, 0], Evaluation(1, 1)), True)

        evaluatedCombi =Attempts.EvaluatedCombination([5, 1, 2, 0], Evaluation(1, 2))
        attempts.evaluateAndAddCombination(evaluatedCombi.colorCombination)
        self.assertEqual(attempts.getLastAttempt() == evaluatedCombi, True)
        self.assertEqual(attempts.getBestAttempt() == Attempts.EvaluatedCombination([5, 1, 2, 0], Evaluation(1, 2)), True)


    def testFunction_EvaluatedCombination_eq(self):
        #equal evaluations
        evaluatedCombi = Attempts.EvaluatedCombination([0, 1, 2, 3], Evaluation(0, 0))
        self.assertEqual(evaluatedCombi == evaluatedCombi, True)
        evaluatedCombi = Attempts.EvaluatedCombination([0, 1, 2, 7], Evaluation(1, 0))
        self.assertEqual(evaluatedCombi == evaluatedCombi, True)
        evaluatedCombi = Attempts.EvaluatedCombination([4, 1, 2, 7], Evaluation(1, 1))
        self.assertEqual(evaluatedCombi == evaluatedCombi, True)
        evaluatedCombi = Attempts.EvaluatedCombination([4, 1, 5, 7], Evaluation(1, 2))
        self.assertEqual(evaluatedCombi == evaluatedCombi, True)

        #unequal evaluations
        evaluatedCombi = Attempts.EvaluatedCombination([0, 1, 2, 3], Evaluation(0, 0))
        self.assertEqual(evaluatedCombi == Attempts.EvaluatedCombination([0, 1, 2, 3], Evaluation(0, 1)), False)
        evaluatedCombi = Attempts.EvaluatedCombination([0, 1, 2, 3], Evaluation(0, 0))
        self.assertEqual(evaluatedCombi == Attempts.EvaluatedCombination([0, 1, 5, 3], Evaluation(0, 0)), False)
        evaluatedCombi = Attempts.EvaluatedCombination([0, 1, 2, 3], Evaluation(0, 0))
        self.assertEqual(evaluatedCombi == Attempts.EvaluatedCombination([0, 1, 5, 3], Evaluation(1, 0)), False)
        evaluatedCombi = Attempts.EvaluatedCombination([0, 1, 2, 3], Evaluation(0, 0))
        self.assertEqual(evaluatedCombi == Attempts.EvaluatedCombination([7, 5, 6, 4], Evaluation(1, 6)), False)

if __name__ == '__main__':
    unittest.main()
