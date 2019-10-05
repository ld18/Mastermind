
import random
import constraint
from Players.AbstractPlayer import AbstractPlayer

class NPC_csp(AbstractPlayer):

    def __init__(self, lengthOfGuess, numberOfColors, attempts):
        self.__lengthOfGuess = lengthOfGuess
        self.__numberOfColors = numberOfColors
        self.__attempts = attempts
        self.strategy = self.getBestAttempt
        self.__cspProblem = self.__createBasicCSP()


    def readInputIn(self):
        return self.strategy()


    def getBestAttempt(self):
        while True:
            if input("Press enter to generate a new random combination. ") == "":
                return random.sample(range(0, self.__numberOfColors), self.__lengthOfGuess)


    def __createBasicCSP(self):
        cspProblem = constraint.Problem()
        self.__cspVariables = []
        cspVariablesIntervals = list(range(self.__numberOfColors))
        for count in range(self.__lengthOfGuess):
            newVariable = "c_"+ str(count)
            self.__cspVariables.append(newVariable)
            cspProblem.addVariable(newVariable, cspVariablesIntervals)
        cspProblem.addConstraint(constraint.AllDifferentConstraint())
        return cspProblem


