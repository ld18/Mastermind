
from Players.AbstractPlayer import AbstractPlayer

class TestPlayer(AbstractPlayer):

    def __init__(self, sequenceOfCombinations):
        self.__sequenceOfCombinations = sequenceOfCombinations
        self.__indexOfSequence = -1


    def readInputIn(self):
        self.__indexOfSequence += 1
        return self.__sequenceOfCombinations[self.__indexOfSequence]