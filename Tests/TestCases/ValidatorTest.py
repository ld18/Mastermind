
from GameLogic.Validator import Validator
from GameLogic.Evaluation import Evaluation
from GameLogic.Attempts import Attempts
from GameLogic.Colorcombination import Colorcombination
from GameLogic.EvaluatedCombination import EvaluatedCombination
from twisted.trial import unittest

class Testcases(unittest.TestCase):


    def testAll(self):
        self.testFunction_Constructor()
        self.testError_Constructor()
        self.testFunction_checkCombination()
        self.testError_checkCombination()
        self.testError_checkCombination()
        self.testFunction_checkEvaluation()
        self.testError_checkEvaluation()
        self.testError_validateForNoObviousRrrors()


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
            sud.validateCombination(Colorcombination(combi))


    def testError_checkCombination(self):
        sud = Validator(4, 8)
        #numbers and dimension to low
        for startValueOfCombi in range(-1, 4):
            for endValueOfCombi in range(-1, 4):
                combi = list(range(startValueOfCombi, endValueOfCombi))
                with self.assertRaises(ValueError):
                    #print(str(startValueOfCombi) +" "+ str(endValueOfCombi) +" "+ str(combi) +" "+ str(len(combi)))
                    sud.validateCombination(Colorcombination(combi))
        #numbers and dimension to high
        for startValueOfCombi in range(4, 6):
            for endValueOfCombi in range(4, 6):
                combi = list(range(startValueOfCombi, endValueOfCombi))
                with self.assertRaises(ValueError):
                    #print(str(startValueOfCombi) +" "+ str(endValueOfCombi) +" "+ str(combi) +" "+ str(len(combi)))
                    sud.validateCombination(Colorcombination(combi))

        combi = [1, 1, 1, 1]
        with self.assertRaises(ValueError):
            sud.validateCombination(Colorcombination(combi))
        combi = [1, 1, 2, 1]
        with self.assertRaises(ValueError):
            sud.validateCombination(Colorcombination(combi))
        combi = [1, 2, 1, 3]
        with self.assertRaises(ValueError):
            sud.validateCombination(Colorcombination(combi))


    def testFunction_checkEvaluation(self):
        sud = Validator(4, 8)
        #valid evaluations
        for startValueOfEval in range(0, 5):
            for endValueOfEval in range(0, 5):
                if (startValueOfEval + endValueOfEval) <= 4:
                    #print(str(startValueOfEval) +" "+ str(endValueOfEval))
                    sud.validateEvaluation(Evaluation(startValueOfEval, endValueOfEval, True))
                    sud.validateEvaluation(Evaluation(startValueOfEval, endValueOfEval, False))


    def testError_checkEvaluation(self):
        sud = Validator(4, 8)
        #invalid evaluations
        for startValueOfEval in range(-2, 0):
            for endValueOfEval in range(-2, 0):
                #print(str(startValueOfEval) +" "+ str(endValueOfEval))
                with self.assertRaises(ValueError):
                    sud.validateEvaluation(Evaluation(startValueOfEval, endValueOfEval, True))
                    sud.validateEvaluation(Evaluation(startValueOfEval, endValueOfEval, False))

        for startValueOfEval in range(4, 6):
            for endValueOfEval in range(1, 6):
                #print(str(startValueOfEval) +" "+ str(endValueOfEval))
                with self.assertRaises(ValueError):
                    sud.validateEvaluation(Evaluation(startValueOfEval, endValueOfEval, True))
                    sud.validateEvaluation(Evaluation(startValueOfEval, endValueOfEval, False))

        for startValueOfEval in range(1, 6):
            for endValueOfEval in range(4, 6):
                #print(str(startValueOfEval) +" "+ str(endValueOfEval))
                with self.assertRaises(ValueError):
                    sud.validateEvaluation(Evaluation(startValueOfEval, endValueOfEval, True))
                    sud.validateEvaluation(Evaluation(startValueOfEval, endValueOfEval, False))


    def testError_validateForNoObviousRrrors(self):
        sud = Validator(4, 8)
        attempts = Attempts()

        evaluatedCombi = EvaluatedCombination(Colorcombination([4, 5, 6, 7]), Evaluation(0, 0, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        debriefing = sud.validateForNoObviousErrors(attempts)
        if debriefing.obiuseError:
            self.fail()

        evaluatedCombi = EvaluatedCombination(Colorcombination([5, 6, 7, 0]), Evaluation(1, 0, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        debriefing = sud.validateForNoObviousErrors(attempts)
        if not debriefing.obiuseError:
            self.fail()

        attempts.clearAttempts()

        evaluatedCombi = EvaluatedCombination(Colorcombination([5, 1, 7, 0]), Evaluation(1, 1, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        debriefing = sud.validateForNoObviousErrors(attempts)
        if debriefing.obiuseError:
            self.fail()

        evaluatedCombi = EvaluatedCombination(Colorcombination([5, 6, 7, 0]), Evaluation(1, 0, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        debriefing = sud.validateForNoObviousErrors(attempts)
        if debriefing.obiuseError:
            self.fail()

        evaluatedCombi = EvaluatedCombination(Colorcombination([5, 1, 2, 0]), Evaluation(1, 2, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        debriefing = sud.validateForNoObviousErrors(attempts)
        if debriefing.obiuseError:
            self.fail()

        evaluatedCombi = EvaluatedCombination(Colorcombination([4, 5, 6, 7]), Evaluation(0, 0, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        debriefing = sud.validateForNoObviousErrors(attempts)
        if debriefing.obiuseError:
            self.fail()

        evaluatedCombi = EvaluatedCombination(Colorcombination([1, 2, 5, 0]), Evaluation(3, 0, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        debriefing = sud.validateForNoObviousErrors(attempts)
        if not debriefing.obiuseError:
            self.fail()

        attempts.clearAttempts()

        evaluatedCombi = EvaluatedCombination(Colorcombination([5, 1, 7, 0]), Evaluation(1, 1, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        debriefing = sud.validateForNoObviousErrors(attempts)
        if debriefing.obiuseError:
            self.fail()

        evaluatedCombi = EvaluatedCombination(Colorcombination([1, 3, 2, 0]), Evaluation(3, 1, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        debriefing = sud.validateForNoObviousErrors(attempts)
        if debriefing.obiuseError:
            self.fail()

        evaluatedCombi = EvaluatedCombination(Colorcombination([5, 1, 2, 0]), Evaluation(1, 2, False))
        attempts.addEvaluatedCombination(evaluatedCombi)
        debriefing = sud.validateForNoObviousErrors(attempts)
        if not debriefing.obiuseError:
            self.fail()


if __name__ == '__main__':
    unittest.main()
