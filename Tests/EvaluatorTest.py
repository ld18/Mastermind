
from GameLogic.Evaluator import Evaluator
from GameLogic.Evaluation import Evaluation
from twisted.trial import unittest

class EvaluatorTest(unittest.TestCase):

    def testFunction_evaluateCombination(self):
        sud = Evaluator([0, 1, 2, 3])

        #calculate right colors on the right place evaluations
        self.assertEqual(sud.evaluateCombination([0, 1, 2, 3]), Evaluation(0, 4, True))
        self.assertEqual(sud.evaluateCombination([4, 1, 2, 3]), Evaluation(0, 3, False))
        self.assertEqual(sud.evaluateCombination([4, 5, 2, 3]), Evaluation(0, 2, False))
        self.assertEqual(sud.evaluateCombination([4, 5, 6, 3]), Evaluation(0, 1, False))
        self.assertEqual(sud.evaluateCombination([4, 5, 6, 7]), Evaluation(0, 0, False))

        #calculate right colors on the wrong place evaluations
        self.assertEqual(sud.evaluateCombination([3, 2, 1, 0]), Evaluation(4, 0, False))
        self.assertEqual(sud.evaluateCombination([3, 2, 1, 7]), Evaluation(3, 0, False))
        self.assertEqual(sud.evaluateCombination([3, 2, 6, 7]), Evaluation(2, 0, False))
        self.assertEqual(sud.evaluateCombination([3, 5, 6, 7]), Evaluation(1, 0, False))
        self.assertEqual(sud.evaluateCombination([4, 5, 6, 7]), Evaluation(0, 0, False))

        #calculate mixed evaluations
        self.assertEqual(sud.evaluateCombination([2, 1, 7, 4]), Evaluation(1, 1, False))
        self.assertEqual(sud.evaluateCombination([2, 1, 0, 4]), Evaluation(2, 1, False))
        self.assertEqual(sud.evaluateCombination([2, 1, 0, 3]), Evaluation(2, 2, False))
        self.assertEqual(sud.evaluateCombination([2, 1, 6, 3]), Evaluation(1, 2, False))

if __name__ == '__main__':
    unittest.main()
