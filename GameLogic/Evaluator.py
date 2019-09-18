
from GameLogic.Validator import Validator
from GameLogic.Evaluation import Evaluation

class Evaluator():
    def __init__(self, masterColorCombination, numberOfColors):
        self.__masterColorCombination = masterColorCombination
        self.__vaidator = Validator(len(masterColorCombination), numberOfColors)
        self.__vaidator.checkCombination(masterColorCombination)


    def evaluateCombination(self, colorCombination):
        self.__vaidator.checkCombination(colorCombination)
        evaluation = Evaluation(0, 0)
        for masterColor, color in zip(self.__masterColorCombination, colorCombination):
            if masterColor == color:
                evaluation.rightColorRightPlace += 1
            elif masterColor in colorCombination:
                evaluation.rightColorWrongPlace += 1
        self.__vaidator.checkEvaluation(evaluation)
        return evaluation


    def __str__(self):
        representation = "Evaluator: Master combination: " + str(self.__masterColorCombination) + ", " + str(self.__vaidator)
        return representation

