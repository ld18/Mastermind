
from GameLogic.Evaluation import Evaluation

class Evaluator():

    def __init__(self, masterCombination):
        self.__masterCombination = masterCombination


    def evaluateCombination(self, colorCombination):
        evaluation = Evaluation(0, 0, False)
        for masterColor, color in zip(self.__masterCombination.colorCombination, colorCombination.colorCombination):
            if masterColor == color:
                evaluation.rightColorRightPlace += 1
            elif masterColor in colorCombination.colorCombination:
                evaluation.rightColorWrongPlace += 1
        if evaluation.rightColorRightPlace == len(self.__masterCombination) \
                and colorCombination == self.__masterCombination:
            evaluation.gameFinished = True
        return evaluation


    def __str__(self):
        representation = "Master combination " + str(self.__masterCombination)
        return representation

