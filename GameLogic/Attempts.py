
class Attempts():
    def __init__(self, evaluator):
        self.__evaluator = evaluator
        self.__combinations = []


    def evaluateAndAddCombination(self, colorCombination):
        evaluation = self.__evaluator.evaluateCombination(colorCombination)
        evaluatedCombination = self.EvaluatedCombination(colorCombination, evaluation)
        self.__combinations.append(evaluatedCombination)


    def getBestAttempt(self):
        return max(self.__combinations, key =lambda x: x.evaluation)


    def getLastAttempt(self):
        return self.__combinations[-1]


    def __str__(self):
        representation = "Attempts: \n\t"+ str(self.__evaluator)
        for combi in self.__combinations:
            representation += "\n\t\t"+ str(combi)
        return representation



    class EvaluatedCombination():
        def __init__(self, colorCombination, evaluation):
            self.colorCombination = colorCombination
            self.evaluation = evaluation


        def __eq__(self, other):
            if self.colorCombination != other.colorCombination or self.evaluation != other.evaluation:
                return False
            return True


        def __str__(self):
            representation = "Combination: "+ str(self.colorCombination) +", Validation: "+ str(self.evaluation)
            return representation