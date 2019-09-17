
class AttemptCollection():
    def __init__(self, evaluator):
        self.__evaluator = evaluator
        self.__combinations = []


    def evaluateAndAddCombination(self, colorCombination):
        validation = self.__evaluator.evaluateCombination(colorCombination)
        validatedCombination = self.__ValidatedCombination(colorCombination, validation)
        self.__combinations.append(validatedCombination)


    def getBestAttempt(self):
        pass

    def getLastAttempt(self):
        pass


    def __str__(self):
        representation = "AttemptCollection: \n\t"+ str(self.__evaluator)
        for combi in self.__combinations:
            representation += "\n\t\t"+ combi.__str__()
        return representation

    class __ValidatedCombination():
        def __init__(self, colorCombination, validation):
            self.colorCombination = colorCombination
            self.validation = validation

        def __str__(self):
            representation = "Combination: "+ str(self.colorCombination) +", Validation: "+ str(self.validation)
            return representation