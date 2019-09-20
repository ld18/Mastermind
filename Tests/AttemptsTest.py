
from GameLogic.Evaluator import Evaluator
from GameLogic.Attempts import Attempts
from GameLogic.Evaluation import Evaluation
from GameLogic.EvaluatedCombination import EvaluatedCombination
from twisted.trial import unittest

class EvaluationTest(unittest.TestCase):

    def testFunction_addEvaluatedCombination(self):
        evaluator = Evaluator([0, 1, 2, 3])
        attempts = Attempts()

        evaluatedCombi = EvaluatedCombination([4, 5, 6, 7], Evaluation(0, 0, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getNumberOfAttempts() == 1, True)

        evaluatedCombi = EvaluatedCombination([5, 6, 7, 0], Evaluation(1, 0, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getNumberOfAttempts() == 2, True)

        evaluatedCombi = EvaluatedCombination([5, 1, 7, 0], Evaluation(1, 1, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getNumberOfAttempts() == 3, True)

        evaluatedCombi = EvaluatedCombination([5, 6, 7, 0], Evaluation(1, 0, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getNumberOfAttempts() == 4, True)

        evaluatedCombi = EvaluatedCombination([5, 1, 2, 0], Evaluation(1, 2, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getNumberOfAttempts() == 5, True)

        attempts.clearAttempts()
        self.assertEqual(attempts.getNumberOfAttempts() == 0, True)


    def testFunction_checkIfCombinationExist(self):
        attempts = Attempts()

        attempts.addEvaluatedCombination(EvaluatedCombination([0, 0, 1], Evaluation(0, 0, False)))
        attempts.addEvaluatedCombination(EvaluatedCombination([0, 1, 0], Evaluation(1, 0, False)))
        attempts.addEvaluatedCombination(EvaluatedCombination([0, 1, 1], Evaluation(1, 1, False)))
        attempts.addEvaluatedCombination(EvaluatedCombination([1, 0, 0], Evaluation(1, 0, False)))

        self.assertEqual(attempts.checkIfCombinationExist([0, 0, 0]), False)
        self.assertEqual(attempts.checkIfCombinationExist([0, 0, 1]), True)
        self.assertEqual(attempts.checkIfCombinationExist([0, 1, 0]), True)
        self.assertEqual(attempts.checkIfCombinationExist([0, 1, 1]), True)
        self.assertEqual(attempts.checkIfCombinationExist([1, 0, 0]), True)
        self.assertEqual(attempts.checkIfCombinationExist([1, 0, 1]), False)
        self.assertEqual(attempts.checkIfCombinationExist([1, 1, 0]), False)
        self.assertEqual(attempts.checkIfCombinationExist([1, 1, 1]), False)


    def testFunction_getBestAttempt(self):
        evaluator = Evaluator([0, 1, 2, 3])
        attempts = Attempts()

        evaluatedCombi = EvaluatedCombination([4, 5, 6, 7], Evaluation(0, 0, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getBestAttempt() == EvaluatedCombination([4, 5, 6, 7], Evaluation(0, 0, False)), True)

        evaluatedCombi = EvaluatedCombination([5, 6, 7, 0], Evaluation(1, 0, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getBestAttempt() == EvaluatedCombination([5, 6, 7, 0], Evaluation(1, 0, False)), True)

        evaluatedCombi = EvaluatedCombination([5, 1, 7, 0], Evaluation(1, 1, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getBestAttempt() == EvaluatedCombination([5, 1, 7, 0], Evaluation(1, 1, False)), True)

        evaluatedCombi = EvaluatedCombination([5, 6, 7, 0], Evaluation(1, 0, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getBestAttempt() == EvaluatedCombination([5, 1, 7, 0], Evaluation(1, 1, False)), True)

        evaluatedCombi = EvaluatedCombination([5, 1, 2, 0], Evaluation(1, 2, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getBestAttempt() == EvaluatedCombination([5, 1, 2, 0], Evaluation(1, 2, False)), True)


    def testFunction_getLastAttempt(self):
        evaluator = Evaluator([0, 1, 2, 3])
        attempts = Attempts()

        evaluatedCombi = EvaluatedCombination([4, 5, 6, 7], Evaluation(0, 0, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getLastAttempt() == evaluatedCombi, True)

        evaluatedCombi = EvaluatedCombination([5, 6, 7, 0], Evaluation(1, 0, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getLastAttempt() == evaluatedCombi, True)

        evaluatedCombi = EvaluatedCombination([5, 1, 7, 0], Evaluation(1, 1, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getLastAttempt() == evaluatedCombi, True)

        evaluatedCombi = EvaluatedCombination([5, 6, 7, 0], Evaluation(1, 0, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getLastAttempt() == evaluatedCombi, True)

        evaluatedCombi = EvaluatedCombination([5, 1, 2, 0], Evaluation(1, 2, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getLastAttempt() == evaluatedCombi, True)


if __name__ == '__main__':
    unittest.main()
