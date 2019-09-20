
class Attempts():
    def __init__(self):
        self.__combinations = []


    def addEvaluatedCombination(self, evaluatedCombination):
        self.__combinations.append(evaluatedCombination)


    def checkIfCombinationExist(self, combination):
        return any(combi.colorCombination == combination for combi in self.__combinations)


    def clearAttempts(self):
        self.__combinations = []


    def getNumberOfAttempts(self):
        return len(self.__combinations)


    def getBestAttempt(self):
        return max(self.__combinations, key =lambda x: x.evaluation)


    def getLastAttempt(self):
        return self.__combinations[-1]


    def __str__(self):
        representation = "All Attempts:"
        for combi in self.__combinations:
            representation += "\n\t\t"+ str(combi)
        return representation
