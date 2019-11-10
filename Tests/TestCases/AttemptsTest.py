
from GameLogic.Evaluator import Evaluator
from GameLogic.Attempts import Attempts
from GameLogic.Evaluation import Evaluation
from GameLogic.EvaluatedCombination import EvaluatedCombination
from GameLogic.Colorcombination import Colorcombination
from twisted.trial import unittest

class Testcases(unittest.TestCase):

    def testAll(self):
        self.testFunction_addEvaluatedCombination()
        self.testFunction_checkIfCombinationExist()
        self.testFunction_getBestAttempt()
        self.testFunction_getLastAttempt()
        self.testFunction_getCombinationsWithNoRightColor()
        self.testFunction_getCombinationsWithAllRightColor()


    def testFunction_addEvaluatedCombination(self):
        evaluator = Evaluator(Colorcombination([0, 1, 2, 3]))
        attempts = Attempts()

        evaluatedCombi = EvaluatedCombination(Colorcombination([4, 5, 6, 7]), Evaluation(0, 0, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getNumberOfAttempts() == 1, True)

        evaluatedCombi = EvaluatedCombination(Colorcombination([5, 6, 7, 0]), Evaluation(1, 0, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getNumberOfAttempts() == 2, True)

        evaluatedCombi = EvaluatedCombination(Colorcombination([5, 1, 7, 0]), Evaluation(1, 1, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getNumberOfAttempts() == 3, True)

        evaluatedCombi = EvaluatedCombination(Colorcombination([5, 6, 7, 0]), Evaluation(1, 0, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getNumberOfAttempts() == 4, True)

        evaluatedCombi = EvaluatedCombination(Colorcombination([5, 1, 2, 0]), Evaluation(1, 2, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getNumberOfAttempts() == 5, True)

        attempts.clearAttempts()
        self.assertEqual(attempts.getNumberOfAttempts() == 0, True)


    def testFunction_checkIfCombinationExist(self):
        attempts = Attempts()


        self.assertEqual(attempts.checkIfCombinationExist(Colorcombination([0, 0, 1])), False)
        attempts.addEvaluatedCombination(EvaluatedCombination(Colorcombination([0, 0, 1]), Evaluation(0, 0, False)))
        self.assertEqual(attempts.checkIfCombinationExist(Colorcombination([0, 0, 1])), True)

        self.assertEqual(attempts.checkIfCombinationExist(Colorcombination([0, 1, 0])), False)
        attempts.addEvaluatedCombination(EvaluatedCombination(Colorcombination([0, 1, 0]), Evaluation(1, 0, False)))
        self.assertEqual(attempts.checkIfCombinationExist(Colorcombination([0, 1, 0])), True)

        self.assertEqual(attempts.checkIfCombinationExist(Colorcombination([0, 1, 1])), False)
        attempts.addEvaluatedCombination(EvaluatedCombination(Colorcombination([0, 1, 1]), Evaluation(1, 1, False)))
        self.assertEqual(attempts.checkIfCombinationExist(Colorcombination([0, 1, 1])), True)

        self.assertEqual(attempts.checkIfCombinationExist(Colorcombination([1, 0, 0])), False)
        attempts.addEvaluatedCombination(EvaluatedCombination(Colorcombination([1, 0, 0]), Evaluation(1, 0, False)))
        self.assertEqual(attempts.checkIfCombinationExist(Colorcombination([1, 0, 0])), True)

        self.assertEqual(attempts.checkIfCombinationExist(Colorcombination([0, 0, 0])), False)
        self.assertEqual(attempts.checkIfCombinationExist(Colorcombination([0, 0, 1])), True)
        self.assertEqual(attempts.checkIfCombinationExist(Colorcombination([0, 1, 0])), True)
        self.assertEqual(attempts.checkIfCombinationExist(Colorcombination([0, 1, 1])), True)
        self.assertEqual(attempts.checkIfCombinationExist(Colorcombination([1, 0, 0])), True)
        self.assertEqual(attempts.checkIfCombinationExist(Colorcombination([1, 0, 1])), False)
        self.assertEqual(attempts.checkIfCombinationExist(Colorcombination([1, 1, 0])), False)
        self.assertEqual(attempts.checkIfCombinationExist(Colorcombination([1, 1, 1])), False)


        attempts.clearAttempts()
        attempts.addEvaluatedCombination(EvaluatedCombination(Colorcombination([0, 2, 3, 1]), Evaluation(1, 0, False)))
        self.assertEqual(attempts.checkIfCombinationExist(Colorcombination([0, 2, 3, 1])), True)
        self.assertEqual(attempts.checkIfCombinationExist(Colorcombination([0, 2, 1, 3])), False)
        self.assertEqual(attempts.checkIfCombinationExist(Colorcombination([0, 3, 2, 1])), False)
        self.assertEqual(attempts.checkIfCombinationExist(Colorcombination([0, 3, 1, 2])), False)
        self.assertEqual(attempts.checkIfCombinationExist(Colorcombination([0, 1, 2, 3])), False)
        self.assertEqual(attempts.checkIfCombinationExist(Colorcombination([0, 1, 3, 2])), False)
        self.assertEqual(attempts.checkIfCombinationExist(Colorcombination([2, 0, 3, 1])), False)


    def testFunction_getBestAttempt(self):
        evaluator = Evaluator(Colorcombination([0, 1, 2, 3]))
        attempts = Attempts()

        with self.assertRaises(ValueError):
            attempts.getBestAttempt()
        with self.assertRaises(ValueError):
            attempts.getLastAttempt()

        evaluatedCombi = EvaluatedCombination(Colorcombination([4, 5, 6, 7]), Evaluation(0, 0, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getBestAttempt() == EvaluatedCombination(Colorcombination([4, 5, 6, 7]), Evaluation(0, 0, False)), True)

        evaluatedCombi = EvaluatedCombination(Colorcombination([5, 6, 7, 0]), Evaluation(1, 0, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getBestAttempt() == EvaluatedCombination(Colorcombination([5, 6, 7, 0]), Evaluation(1, 0, False)), True)

        evaluatedCombi = EvaluatedCombination(Colorcombination([5, 1, 7, 0]), Evaluation(1, 1, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getBestAttempt() == EvaluatedCombination(Colorcombination([5, 1, 7, 0]), Evaluation(1, 1, False)), True)

        evaluatedCombi = EvaluatedCombination(Colorcombination([5, 6, 7, 0]), Evaluation(1, 0, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getBestAttempt() == EvaluatedCombination(Colorcombination([5, 1, 7, 0]), Evaluation(1, 1, False)), True)

        evaluatedCombi = EvaluatedCombination(Colorcombination([5, 1, 2, 0]), Evaluation(1, 2, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getBestAttempt() == EvaluatedCombination(Colorcombination([5, 1, 2, 0]), Evaluation(1, 2, False)), True)


    def testFunction_getLastAttempt(self):
        evaluator = Evaluator(Colorcombination([0, 1, 2, 3]))
        attempts = Attempts()

        evaluatedCombi = EvaluatedCombination(Colorcombination([4, 5, 6, 7]), Evaluation(0, 0, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getLastAttempt() == evaluatedCombi, True)

        evaluatedCombi = EvaluatedCombination(Colorcombination([5, 6, 7, 0]), Evaluation(1, 0, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getLastAttempt() == evaluatedCombi, True)

        evaluatedCombi = EvaluatedCombination(Colorcombination([5, 1, 7, 0]), Evaluation(1, 1, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getLastAttempt() == evaluatedCombi, True)

        evaluatedCombi = EvaluatedCombination(Colorcombination([5, 6, 7, 0]), Evaluation(1, 0, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getLastAttempt() == evaluatedCombi, True)

        evaluatedCombi = EvaluatedCombination(Colorcombination([5, 1, 2, 0]), Evaluation(1, 2, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getLastAttempt() == evaluatedCombi, True)


    def testFunction_getCombinationsWithNoRightColor(self):
        evaluator = Evaluator(Colorcombination([0, 1, 2, 3]))
        attempts = Attempts()

        evaluatedCombi = EvaluatedCombination(Colorcombination([5, 6, 7, 0]), Evaluation(1, 0, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getCombinationsWithNoRightColor() == [], True)

        evaluatedCombi = EvaluatedCombination(Colorcombination([4, 5, 6, 7]), Evaluation(0, 0, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getCombinationsWithNoRightColor() == [Colorcombination([4, 5, 6, 7])], True)

        evaluatedCombi = EvaluatedCombination(Colorcombination([5, 1, 7, 0]), Evaluation(1, 1, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getCombinationsWithNoRightColor() == [Colorcombination([4, 5, 6, 7])], True)

        evaluatedCombi = EvaluatedCombination(Colorcombination([5, 6, 7, 0]), Evaluation(1, 0, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getCombinationsWithNoRightColor() == [Colorcombination([4, 5, 6, 7])], True)

        evaluatedCombi = EvaluatedCombination(Colorcombination([0, 1, 2, 5]), Evaluation(0, 1, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getCombinationsWithNoRightColor() == [Colorcombination([4, 5, 6, 7])], True)

        evaluatedCombi = EvaluatedCombination(Colorcombination([4, 6, 5, 7]), Evaluation(0, 0, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getCombinationsWithNoRightColor() == [Colorcombination([4, 5, 6, 7]), Colorcombination([4, 6, 5, 7])], True)

        evaluatedCombi = EvaluatedCombination(Colorcombination([4, 6, 5, 7]), Evaluation(0, 0, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getCombinationsWithNoRightColor() == [Colorcombination([4, 5, 6, 7]), Colorcombination([4, 6, 5, 7])], True)

        evaluatedCombi = EvaluatedCombination(Colorcombination([0, 1, 2, 3]), Evaluation(0, 4, True))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getCombinationsWithNoRightColor() == [Colorcombination([4, 5, 6, 7]), Colorcombination([4, 6, 5, 7])], True)


    def testFunction_getCombinationsWithAllRightColor(self):
        evaluator = Evaluator(Colorcombination([0, 1, 2, 3]))
        attempts = Attempts()

        evaluatedCombi = EvaluatedCombination(Colorcombination([5, 6, 7, 0]), Evaluation(1, 0, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        with self.assertRaises(ValueError):
            attempts.getCombinationWithAllRightColors()

        evaluatedCombi = EvaluatedCombination(Colorcombination([0, 1, 2, 3]), Evaluation(1, 3, True))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getCombinationWithAllRightColors() == Colorcombination([0, 1, 2, 3]), True)

        evaluatedCombi = EvaluatedCombination(Colorcombination([4, 6, 5, 7]), Evaluation(0, 0, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getCombinationWithAllRightColors() == Colorcombination([0, 1, 2, 3]), True)

        evaluatedCombi = EvaluatedCombination(Colorcombination([0, 1, 3, 2]), Evaluation(0, 4, True))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getCombinationWithAllRightColors() == Colorcombination([0, 1, 2, 3]), True)

        attempts.clearAttempts()

        evaluatedCombi = EvaluatedCombination(Colorcombination([0, 1, 3, 2]), Evaluation(0, 4, True))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getCombinationWithAllRightColors() == Colorcombination([0, 1, 3, 2]), True)

        evaluatedCombi = EvaluatedCombination(Colorcombination([5, 6, 7, 0]), Evaluation(1, 0, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getCombinationWithAllRightColors() == Colorcombination([0, 1, 3, 2]), True)

        evaluatedCombi = EvaluatedCombination(Colorcombination([0, 1, 2, 3]), Evaluation(1, 3, True))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getCombinationWithAllRightColors() == Colorcombination([0, 1, 3, 2]), True)

        evaluatedCombi = EvaluatedCombination(Colorcombination([4, 6, 5, 7]), Evaluation(0, 0, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        self.assertEqual(attempts.getCombinationWithAllRightColors() == Colorcombination([0, 1, 3, 2]), True)


if __name__ == '__main__':
    unittest.main()
