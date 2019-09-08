
class GuessedCombination():
    def __init__(self, valuator):
        self.valuator = valuator
        self.numberOfColors = valuator.numberOfColors
        self.combinations = []

    def evaluateAndAddCombination(self, colorCombination):
        validation = self.valuator.evaluateCombination(colorCombination)
        validatedCombination = self.ValidatedCombination(colorCombination, validation)
        self.combinations.append(validatedCombination)

    def __str__(self):
        representation = "GuessedCombination: Valuator: \n"\
                         + "\t"+ str(self.valuator)
        for combi in self.combinations:
            representation += "\n\t"+ combi.__str__()
        return representation

    class ValidatedCombination():
        def __init__(self, colorCombination, validation):
            self.colorCombination = colorCombination
            self.validation = validation

        def __str__(self):
            representation = "ValidatedCombination: Combination: "+ str(self.colorCombination) +", Validation: "+ str(self.validation)
            return representation