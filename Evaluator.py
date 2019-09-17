
from Validator import Validator

class Evaluator():
    def __init__(self, masterColorCombination, numberOfColors):
        self.lengthOfGuess = len(masterColorCombination)
        self.numberOfColors = numberOfColors
        self.masterColorCombination = masterColorCombination
        self.vaidator = Validator(self.lengthOfGuess, self.numberOfColors)
        self.vaidator.checkCombination(masterColorCombination)


    def evaluateCombination(self, colorCombination):
        self.vaidator.checkCombination(colorCombination)
        rightColorRightPlacePoints = rightColorWrongPlacePoints = 0
        for masterColor, color in zip(self.masterColorCombination, colorCombination):
            if masterColor == color:
                rightColorRightPlacePoints += 1
            elif masterColor in colorCombination:
                    rightColorWrongPlacePoints += 1

        self.vaidator.checkEvaluation(rightColorWrongPlacePoints, rightColorRightPlacePoints)
        return (rightColorWrongPlacePoints, rightColorRightPlacePoints)


    def __str__(self):
        representation = "Evaluator: Number of colors =" + str(self.numberOfColors) +" Length of guess: "+ str(self.lengthOfGuess) +", Master combination: "+ str(self.masterColorCombination)
        return representation

