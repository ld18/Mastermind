
import random

class NPC():

    def __init__(self, lengthOfGuess, numberOfColors):
        self.__lengthOfGuess = lengthOfGuess
        self.__numberOfColors = numberOfColors
        self.__strategy = self.strategy_Random

    def readInputIn(self):
        return self.__strategy()

    def strategy_Random(self):
        while True:
            if input("Press enter to generate a new random combination. ") == "":
                return random.sample(range(0, self.__numberOfColors), self.__lengthOfGuess)
