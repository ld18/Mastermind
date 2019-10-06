
from GameLogic.Evaluation import Evaluation

class Attempts():

    def __init__(self):
        self.__combinations = []


    def addEvaluatedCombination(self, evaluatedCombination):
        self.__combinations.append(evaluatedCombination)


    def getCombinations(self):
        return self.__combinations.copy()


    def checkIfCombinationExist(self, combination):
        return any(combi.colorCombination == combination for combi in self.__combinations)


    def clearAttempts(self):
        self.__combinations = []


    def getNumberOfAttempts(self):
        return len(self.__combinations)


    def getBestAttempt(self):
        if len(self.__combinations) <= 0:
            raise ValueError('__combinations is empty')
        return max(self.__combinations, key =lambda x: x.evaluation)


    def getCombinationsWithNoRightColor(self):
        if len(self.__combinations) <= 0:
            raise ValueError('__combinations is empty')
        allWrongCombinations = []
        for combi in self.__combinations:
            if combi.evaluation == Evaluation(0, 0, False):
                if not combi.colorCombination in allWrongCombinations:
                    allWrongCombinations.append(combi.colorCombination)
        return allWrongCombinations


    def getCombinationWithAllRightColors(self):
        if len(self.__combinations) <= 0:
            raise ValueError('__combinations is empty')
        lenghtOfGuess = len(self.__combinations[0].colorCombination)
        for combi in self.__combinations:
            if combi.evaluation.getNumberOfRightColors() == lenghtOfGuess:
                return combi.colorCombination
        raise ValueError('__combinations has no good attempts')


    def getLastAttempt(self):
        if len(self.__combinations) <= 0:
            raise ValueError('__combinations is empty')
        return self.__combinations[-1]


    def __str__(self):
        representation = "All Attempts:"
        for combi in self.__combinations:
            representation += "\n\t\t"+ str(combi)
        return representation
