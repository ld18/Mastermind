
import random
import constraint
from Players.AbstractPlayer import AbstractPlayer
from GameLogic.Evaluator import Evaluator
from GameLogic.Colorcombination import Colorcombination

class NPC_csp(AbstractPlayer):

    def __init__(self, lengthOfGuess, numberOfColors, attempts):
        self.__lengthOfGuess = lengthOfGuess
        self.__numberOfColors = numberOfColors
        self.__attempts = attempts
        self.__cspVariables = []
        self.__cspVariablesStrings = []
        self.__cspProblem = self.__createBasicCSP()
        self.strategy = self.__getNextPossibleCombination


    def introduceYourself(self):
        print("This NPC tries to solve Mastermind by using a constraint satisfaction problem (CSP) approach.\n")


    def readInputIn(self):
        return self.strategy()


    def debriefing(self, obviousError):
        if obviousError:
            raise Exception("There should be no obvious Errors in my game!1")


    def __createBasicCSP(self):
        cspProblem = constraint.Problem()
        cspVariablesIntervals = list(range(self.__numberOfColors))
        for count in range(self.__lengthOfGuess):
            newVariable = "c_"+ str(count)
            self.__cspVariablesStrings.append(newVariable)
            cspProblem.addVariable(newVariable, cspVariablesIntervals)
        cspProblem.addConstraint(constraint.AllDifferentConstraint())
        return cspProblem


    def __getNextPossibleCombination(self):
        lastAttempt = None
        try:
            lastAttempt = self.__attempts.getLastAttempt()
        except ValueError:
            return random.sample(range(0, self.__numberOfColors), self.__lengthOfGuess)

        if self.__lengthOfGuess == 1:
            lambdaConstraint = lambda c_0: self.__validateWithTemporaryMastercombination(Colorcombination([c_0]), lastAttempt.colorCombination) == lastAttempt.evaluation
        elif self.__lengthOfGuess == 2:
            lambdaConstraint = lambda c_0, c_1: self.__validateWithTemporaryMastercombination(Colorcombination([c_0, c_1]), lastAttempt.colorCombination) == lastAttempt.evaluation
        elif self.__lengthOfGuess == 3:
            lambdaConstraint = lambda c_0, c_1, c_2: self.__validateWithTemporaryMastercombination(Colorcombination([c_0, c_1, c_2]), lastAttempt.colorCombination) == lastAttempt.evaluation
        elif self.__lengthOfGuess == 4:
            lambdaConstraint = lambda c_0, c_1, c_2, c_3: self.__validateWithTemporaryMastercombination(Colorcombination([c_0, c_1, c_2, c_3]), lastAttempt.colorCombination) == lastAttempt.evaluation
        elif self.__lengthOfGuess == 5:
            lambdaConstraint = lambda c_0, c_1, c_2, c_3, c_4: self.__validateWithTemporaryMastercombination(Colorcombination([c_0, c_1, c_2, c_3, c_4]), lastAttempt.colorCombination) == lastAttempt.evaluation
        elif self.__lengthOfGuess == 6:
            lambdaConstraint = lambda c_0, c_1, c_2, c_3, c_4, c_5: self.__validateWithTemporaryMastercombination(Colorcombination([c_0, c_1, c_2, c_3, c_4, c_5]), lastAttempt.colorCombination) == lastAttempt.evaluation
        else:
            raise NotImplementedError("This lenght of Guess is not supported yet")
        self.__cspProblem.addConstraint(lambdaConstraint, self.__cspVariablesStrings)

        newCombination = []
        for value in self.__cspProblem.getSolution().values():
            newCombination.append(value)
        return newCombination


    def __validateWithTemporaryMastercombination(self, tmpMasterCombination, colorCombination):
        tmpEvaluator = Evaluator(tmpMasterCombination)
        return tmpEvaluator.evaluateCombination(colorCombination)


