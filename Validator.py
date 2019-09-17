
class Validator():
    def __init__(self, lengthOfGuess, numberOfColors):
        self.lengthOfGuess = lengthOfGuess
        self.numberOfColors = numberOfColors
        self.checkInitialParameter()


    def checkInitialParameter(self):
        if not isinstance(self.lengthOfGuess, int):
            raise ValueError('lengthOfGuess is not a list')
        if not isinstance(self.numberOfColors, int):
            raise ValueError('numberOfColors is not a list')
        if self.numberOfColors <= 0:
            raise ValueError('numberOfColors is not valid ('+ str(self.numberOfColors) +")")
        if self.lengthOfGuess <= 0:
            raise ValueError('lengthOfGuess is not valid ('+ str(self.lengthOfGuess) +")")
        if self.lengthOfGuess > self.numberOfColors:
            raise ValueError('numberOfColors is not valid ('+ str(self.lengthOfGuess) +", "+ str(self.numberOfColors) +")")


    def checkCombination(self, colorCombination):
        if not isinstance(colorCombination, list):
            raise ValueError('colorCombination is not a list')
        if len(colorCombination) < 1:
            raise ValueError('colorCombination is not valid ('+ str(colorCombination) +")")
        if len(colorCombination) != self.lengthOfGuess:
            raise ValueError('colorCombination is not valid ('+ str(colorCombination) +", "+ str(self.lengthOfGuess) +")")
        for color in colorCombination:
            if not 0 <= color < self.numberOfColors:
                raise ValueError('colorCombination is not valid ('+ str(colorCombination) +", "+ str(self.numberOfColors) +")")
        if len(colorCombination) != len(set(colorCombination)):
            raise ValueError('colorCombination is not valid ('+ str(colorCombination) +")")


    def checkEvaluation(self, rightColorWrongPlace, rightColorRightPlace):
        if not isinstance(rightColorWrongPlace, int):
            raise ValueError('rightColorWrongPlace is not a list')
        if not isinstance(rightColorRightPlace, int):
            raise ValueError('rightColorRightPlace is not a list')
        if not 0 <= rightColorWrongPlace <= self.lengthOfGuess:
            raise ValueError('rightColorWrongPlace is not valid ('+ str(rightColorWrongPlace) +", "+ str(self.lengthOfGuess) +")")
        if not 0 <= rightColorRightPlace <= self.lengthOfGuess:
            raise ValueError('rightColorRightPlace is not valid ('+ str(rightColorRightPlace) +", "+ str(self.lengthOfGuess) +")")
        if not 0 <= (rightColorWrongPlace + rightColorRightPlace) <= self.lengthOfGuess:
            raise ValueError('rightColorRightPlace and rightColorWrongPlace are not valid ('+ str(rightColorWrongPlace) +", "+ str(rightColorRightPlace) +", "+ str(self.lengthOfGuess) +")")


    def __str__(self):
        representation = "Validator: Number of colors =" + str(self.numberOfColors) +" Length of guess: "+ str(self.lengthOfGuess)
        return representation

