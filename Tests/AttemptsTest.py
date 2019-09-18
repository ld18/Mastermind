
from GameLogic.Evaluator import Evaluator
from GameLogic.Attempts import Attempts
from GameLogic.Evaluation import Evaluation
from GameLogic.EvaluatedCombination import EvaluatedCombination
from twisted.trial import unittest

class EvaluationTest(unittest.TestCase):

    def testFunction_getBestAttempt(self):
        evaluator = Evaluator([0, 1, 2, 3])
        attempts = Attempts()

        evaluatedCombi = EvaluatedCombination([4, 5, 6, 7], Evaluation(0, 0, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getLastAttempt() == evaluatedCombi, True)
        self.assertEqual(attempts.getBestAttempt() == EvaluatedCombination([4, 5, 6, 7], Evaluation(0, 0, False)), True)

        evaluatedCombi = EvaluatedCombination([5, 6, 7, 0], Evaluation(1, 0, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getLastAttempt() == evaluatedCombi, True)
        self.assertEqual(attempts.getBestAttempt() == EvaluatedCombination([5, 6, 7, 0], Evaluation(1, 0, False)), True)

        evaluatedCombi = EvaluatedCombination([5, 1, 7, 0], Evaluation(1, 1, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getLastAttempt() == evaluatedCombi, True)
        self.assertEqual(attempts.getBestAttempt() == EvaluatedCombination([5, 1, 7, 0], Evaluation(1, 1, False)), True)

        evaluatedCombi = EvaluatedCombination([5, 6, 7, 0], Evaluation(1, 0, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getLastAttempt() == evaluatedCombi, True)
        self.assertEqual(attempts.getBestAttempt() == EvaluatedCombination([5, 1, 7, 0], Evaluation(1, 1, False)), True)

        evaluatedCombi = EvaluatedCombination([5, 1, 2, 0], Evaluation(1, 2, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getLastAttempt() == evaluatedCombi, True)
        self.assertEqual(attempts.getBestAttempt() == EvaluatedCombination([5, 1, 2, 0], Evaluation(1, 2, False)), True)


    def testFunction_EvaluatedCombination_eq(self):
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
