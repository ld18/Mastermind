
from GameLogic.Validator import Validator

class Evaluator():
    def __init__(self, masterColorCombination, numberOfColors):
        self.__masterColorCombination = masterColorCombination
        self.__vaidator = Validator(len(masterColorCombination), numberOfColors)
        self.__vaidator.checkCombination(masterColorCombination)


    def evaluateCombination(self, colorCombination):
        self.__vaidator.checkCombination(colorCombination)
        rightColorRightPlacePoints = rightColorWrongPlacePoints = 0
        for masterColor, color in zip(self.__masterColorCombination, colorCombination):
            if masterColor == color:
                rightColorRightPlacePoints += 1
            elif masterColor in colorCombination:
                    rightColorWrongPlacePoints += 1

        self.__vaidator.checkEvaluation(rightColorWrongPlacePoints, rightColorRightPlacePoints)
        return (rightColorWrongPlacePoints, rightColorRightPlacePoints)


    def __str__(self):
        representation = "Evaluator: Master combination: " + str(self.__masterColorCombination) + ", " + str(self.__vaidator)
        return representation

