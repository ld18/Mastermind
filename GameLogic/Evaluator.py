
from GameLogic.Evaluation import Evaluation

class Evaluator():
    def __init__(self, masterColorCombination):
        self.__masterColorCombination = masterColorCombination


    def evaluateCombination(self, colorCombination):
        evaluation = Evaluation(0, 0, False)
        for masterColor, color in zip(self.__masterColorCombination, colorCombination):
            if masterColor == color:
                evaluation.rightColorRightPlace += 1
            elif masterColor in colorCombination:
                evaluation.rightColorWrongPlace += 1
        if evaluation.rightColorRightPlace == len(self.__masterColorCombination):
            evaluation.gameFinished = True
        return evaluation


    def __str__(self):
        representation = "Master combination " + str(self.__masterColorCombination)
        return representation

