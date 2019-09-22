
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


    def validateCombination(self, combination):
        if not isinstance(combination.colorCombination, list):
            raise ValueError('combination is not a list')
        if not all(isinstance(color, int) for color in combination.colorCombination):
            raise ValueError('combination is not a int list')
        if len(combination) < 1:
            raise ValueError('combination is below 1 (' + str(combination) + ")")
        if len(combination) != self.__lengthOfGuess:
            raise ValueError('combination is the right size (' + str(combination) + ", " + str(self.__lengthOfGuess) + ")")
        if not all(0 <= color < self.__numberOfColors for color in combination.colorCombination):
            raise ValueError('a color in the combination is out of range (' + str(combination) + ", " + str(self.__numberOfColors) + ")")
        if len(combination) != len(set(combination.colorCombination)):
            raise ValueError('combination contains several times the same value (' + str(combination) + ")")


    def validateAttempts(self, attempts):
        raise NotImplementedError()


    def validateForNoObviousRrrors(self, attempts):
        raise NotImplementedError()


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

