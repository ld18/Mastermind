
from GameLogic.Evaluator import Evaluator
from GameLogic.Evaluation import Evaluation
from twisted.trial import unittest

class EvaluatorTest(unittest.TestCase):

    def testFunction_Constructor(self):
        #valid construcotrs
        for numColors in range(1, 10):
            for guessLenght in range(1, numColors + 1):
                masterCombi = list(range(0, guessLenght))
                #print(str(guessLenght) +" "+ str(numColors) +" "+ str(masterCombi))
                sud = Evaluator(masterCombi, numColors)

    def testFunction_evaluateCombination(self):
        sud = Evaluator([0, 1, 2, 3], 8)

        #calculate right colors on the right place evaluations
        self.assertEqual(sud.evaluateCombination([0, 1, 2, 3]), Evaluation(0, 4))
        self.assertEqual(sud.evaluateCombination([4, 1, 2, 3]), Evaluation(0, 3))
        self.assertEqual(sud.evaluateCombination([4, 5, 2, 3]), Evaluation(0, 2))
        self.assertEqual(sud.evaluateCombination([4, 5, 6, 3]), Evaluation(0, 1))
        self.assertEqual(sud.evaluateCombination([4, 5, 6, 7]), Evaluation(0, 0))

        #calculate right colors on the wrong place evaluations
        self.assertEqual(sud.evaluateCombination([3, 2, 1, 0]), Evaluation(4, 0))
        self.assertEqual(sud.evaluateCombination([3, 2, 1, 7]), Evaluation(3, 0))
        self.assertEqual(sud.evaluateCombination([3, 2, 6, 7]), Evaluation(2, 0))
        self.assertEqual(sud.evaluateCombination([3, 5, 6, 7]), Evaluation(1, 0))
        self.assertEqual(sud.evaluateCombination([4, 5, 6, 7]), Evaluation(0, 0))

        #calculate mixed evaluations
        self.assertEqual(sud.evaluateCombination([2, 1, 7, 4]), Evaluation(1, 1))
        self.assertEqual(sud.evaluateCombination([2, 1, 0, 4]), Evaluation(2, 1))
        self.assertEqual(sud.evaluateCombination([2, 1, 0, 3]), Evaluation(2, 2))
        self.assertEqual(sud.evaluateCombination([2, 1, 6, 3]), Evaluation(1, 2))

if __name__ == '__main__':
    unittest.main()
