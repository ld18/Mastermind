
class Validator():
    def __init__(self, lengthOfGuess, numberOfColors):
        self.__lengthOfGuess = lengthOfGuess
        self.__numberOfColors = numberOfColors
        self.__validateInitialParameter()


    def __validateInitialParameter(self):
        if not isinstance(self.__lengthOfGuess, int):
            raise ValueError('__lengthOfGuess is not a int')
        if not isinstance(self.__numberOfColors, int):
            raise ValueError('__numberOfColors is not a int')
        if self.__numberOfColors <= 0:
            raise ValueError('__numberOfColors is below zero (' + str(self.__numberOfColors) + ")")
        if self.__lengthOfGuess <= 0:
            raise ValueError('__lengthOfGuess is below zero (' + str(self.__lengthOfGuess) + ")")
        if self.__lengthOfGuess > self.__numberOfColors:
            raise ValueError('__lengthOfGuess is below or equal to __numberOfColors (' + str(self.__lengthOfGuess) + ", " + str(self.__numberOfColors) + ")")


    def validateCombination(self, colorCombination):
        if not isinstance(colorCombination, list):
            raise ValueError('colorCombination is not a list')
        if not all(isinstance(color, int) for color in colorCombination):
            raise ValueError('colorCombination is not a int list')
        if len(colorCombination) < 1:
            raise ValueError('colorCombination is below 1 ('+ str(colorCombination) +")")
        if len(colorCombination) != self.__lengthOfGuess:
            raise ValueError('colorCombination is the right size (' + str(colorCombination) +", " + str(self.__lengthOfGuess) + ")")
        if not all(0 <= color < self.__numberOfColors for color in colorCombination):
            raise ValueError('a color in the colorCombination is out of range (' + str(colorCombination) +", " + str(self.__numberOfColors) + ")")
        if len(colorCombination) != len(set(colorCombination)):
            raise ValueError('colorCombination contains several times the same value ('+ str(colorCombination) +")")


    def validateEvaluation(self, evaluation):
        if not isinstance(evaluation.rightColorWrongPlace, int):
            raise ValueError('rightColorWrongPlace is not a int')
        if not isinstance(evaluation.rightColorRightPlace, int):
            raise ValueError('rightColorRightPlace is not a int')
        if not 0 <= evaluation.rightColorWrongPlace <= self.__lengthOfGuess:
            raise ValueError('rightColorWrongPlace is out of range (' + str(evaluation.rightColorWrongPlace) +", " + str(self.__lengthOfGuess) + ")")
        if not 0 <= evaluation.rightColorRightPlace <= self.__lengthOfGuess:
            raise ValueError('rightColorRightPlace is out of range (' + str(evaluation.rightColorRightPlace) +", " + str(self.__lengthOfGuess) + ")")
        if not 0 <= (evaluation.rightColorWrongPlace + evaluation.rightColorRightPlace) <= self.__lengthOfGuess:
            raise ValueError('rightColorRightPlace and rightColorWrongPlace combined are out of range (' + str(evaluation.rightColorWrongPlace) +", " + str(evaluation.rightColorRightPlace) +", " + str(self.__lengthOfGuess) + ")")


    def validateMaxNumberOfAttempts(self, maxNumberOfAttempts):
        if not isinstance(maxNumberOfAttempts, int):
            raise ValueError('maxNumberOfAttempts is not a int')
        if maxNumberOfAttempts < 1:
            raise ValueError('maxNumberOfAttempts is below 1 ('+ str(maxNumberOfAttempts) +")")


    def __str__(self):
        representation = str(self.__lengthOfGuess) + " of " + str(self.__numberOfColors) +" colors"
        return representation

