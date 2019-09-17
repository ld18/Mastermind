
from GameLogic.Validator import Validator
from twisted.trial import unittest

class ValuatorTest(unittest.TestCase):

    def testFunction_Constructor(self):
        #valid construcotrs
        for numColors in range(1, 10):
            for guessLenght in range(1, numColors + 1):
                #print(str(guessLenght) +" "+ str(numColors))
                sud = Validator(guessLenght, numColors)

    def testError_Constructor(self):
        #invalid construcotrs
        for numColors in range(-2, 1):
            for guessLenght in range(-2, 1):
                with self.assertRaises(ValueError):
                    #print(str(guessLenght) +" "+ str(numColors))
                    sud = Validator(guessLenght, numColors)

        #wrong number of colors
        with self.assertRaises(ValueError):
            sud = Validator(4, -1)
        with self.assertRaises(ValueError):
            sud = Validator(4, 0)
        with self.assertRaises(ValueError):
            sud = Validator(4, 3)

        #wrong colorvalues
        with self.assertRaises(ValueError):
            sud = Validator(-1, 4)
        with self.assertRaises(ValueError):
            sud = Validator(0, 4)
        with self.assertRaises(ValueError):
            sud = Validator(5, 4)

    def testFunction_checkCombination(self):
        sud = Validator(4, 8)
        #valid combination
        for startValueOfCombi in range(0, 5):
            combi = list(range(startValueOfCombi, startValueOfCombi + 4))
            #print(str(startValueOfCombi) +" "+ str(startValueOfCombi + 4) +" "+ str(combi) +" "+ str(len(combi)))
            sud.checkCombination(combi)

    def testError_checkCombination(self):
        sud = Validator(4, 8)
        #numbers and dimension to low
        for startValueOfCombi in range(-1, 4):
            for endValueOfCombi in range(-1, 4):
                combi = list(range(startValueOfCombi, endValueOfCombi))
                with self.assertRaises(ValueError):
                    #print(str(startValueOfCombi) +" "+ str(endValueOfCombi) +" "+ str(combi) +" "+ str(len(combi)))
                    sud.checkCombination(combi)
        #numbers and dimension to high
        for startValueOfCombi in range(4, 6):
            for endValueOfCombi in range(4, 6):
                combi = list(range(startValueOfCombi, endValueOfCombi))
                with self.assertRaises(ValueError):
                    #print(str(startValueOfCombi) +" "+ str(endValueOfCombi) +" "+ str(combi) +" "+ str(len(combi)))
                    sud.checkCombination(combi)

        combi = [1, 1, 1, 1]
        with self.assertRaises(ValueError):
            sud.checkCombination(combi)
        combi = [1, 1, 2, 1]
        with self.assertRaises(ValueError):
            sud.checkCombination(combi)
        combi = [1, 2, 1, 3]
        with self.assertRaises(ValueError):
            sud.checkCombination(combi)

    def testFunction_checkEvaluation(self):
        sud = Validator(4, 8)
        #valid evaluations
        for startValueOfEval in range(0, 5):
            for endValueOfEval in range(0, 5):
                if (startValueOfEval + endValueOfEval) <= 4:
                    #print(str(startValueOfEval) +" "+ str(endValueOfEval))
                    sud.checkEvaluation(startValueOfEval, endValueOfEval)

    def testError_checkEvaluation(self):
        sud = Validator(4, 8)
        #invalid evaluations
        for startValueOfEval in range(-2, 0):
            for endValueOfEval in range(-2, 0):
                #print(str(startValueOfEval) +" "+ str(endValueOfEval))
                with self.assertRaises(ValueError):
                    sud.checkEvaluation(startValueOfEval, endValueOfEval)

        for startValueOfEval in range(4, 6):
            for endValueOfEval in range(1, 6):
                #print(str(startValueOfEval) +" "+ str(endValueOfEval))
                with self.assertRaises(ValueError):
                    sud.checkEvaluation(startValueOfEval, endValueOfEval)

        for startValueOfEval in range(1, 6):
            for endValueOfEval in range(4, 6):
                #print(str(startValueOfEval) +" "+ str(endValueOfEval))
                with self.assertRaises(ValueError):
                    sud.checkEvaluation(startValueOfEval, endValueOfEval)

if __name__ == '__main__':
    unittest.main()
