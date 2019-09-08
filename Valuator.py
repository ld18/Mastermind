from _json import make_scanner


class Valuator():
    def __init__(self, masterColorCombination, numberOfColors):
        self.lengthOfGuess = len(masterColorCombination)
        self.numberOfColors = numberOfColors
        self.masterColorCombination = masterColorCombination
        self.checkInitialParameter()


    def evaluateCombination(self, colorCombination):
        self.checkCombination(colorCombination)
        evaluation = self.calculateEvaluation(colorCombination)
        self.checkEvaluation(evaluation)
        return evaluation


    def calculateEvaluation(self, colorCombination):
        rightColorRightPlacePoints = rightColorWrongPlacePoints = 0
        for masterColor, color in zip(self.masterColorCombination, colorCombination):
            if masterColor == color:
                rightColorRightPlacePoints += 1
            elif masterColor in colorCombination:
                    rightColorWrongPlacePoints += 1
        return (rightColorWrongPlacePoints, rightColorRightPlacePoints)


    def checkInitialParameter(self):
        if not 1 <= self.numberOfColors:
            raise ValueError('numberOfColors is not valid ('+ str(self.numberOfColors) +")")
        if not self.lengthOfGuess <= self.numberOfColors:
            raise ValueError('numberOfColors is not valid ('+ str(self.lengthOfGuess) +", "+ str(self.numberOfColors) +")")
        self.checkCombination(self.masterColorCombination)


    def checkCombination(self, colorCombination):
        if not isinstance(colorCombination, list):
            raise ValueError('colorCombination is not a list')
        if not len(colorCombination) > 0:
            raise ValueError('colorCombination is not valid ('+ str(colorCombination) +")")
        if not len(colorCombination) == self.lengthOfGuess:
            raise ValueError('colorCombination is not valid ('+ str(colorCombination) +", "+ str(self.lengthOfGuess) +")")
        for color in colorCombination:
            if not 0 <= color < self.numberOfColors:
                raise ValueError('colorCombination is not valid ('+ str(colorCombination) +", "+ str(self.numberOfColors) +")")


    def checkEvaluation(self, evaluation):
        if not 0 <= evaluation[0] < self.numberOfColors:
            raise ValueError('rightColorWrongPlace is not valid ('+ str(evaluation) +", "+ str(self.numberOfColors) +")")
        if not 0 <= evaluation[1] < self.numberOfColors:
            raise ValueError('rightColorRightPlace is not valid ('+ str(evaluation) +", "+ str(self.numberOfColors) +")")
        if not 0 <= (evaluation[0] + evaluation[1]) < self.numberOfColors:
            raise ValueError('rightColorRightPlace and rightColorWrongPlace are not valid ('+ str(evaluation) +", "+ str(self.numberOfColors) +")")


    def __str__(self):
        representation = "Valuator: Number of colors =" + str(self.numberOfColors) +" Length of guess: "+ str(self.lengthOfGuess) +", Master combination: "+ str(self.masterColorCombination)
        return representation

