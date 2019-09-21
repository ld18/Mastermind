
import random
from Players.AbstractPlayer import AbstractPlayer

class NPC(AbstractPlayer):

    def __init__(self, lengthOfGuess, numberOfColors, attempts):
        self.__lengthOfGuess = lengthOfGuess
        self.__numberOfColors = numberOfColors
        self.__attempts = attempts
        self.strategy = self.strategy_automaticImprovedRandom


    def readInputIn(self):
        return self.strategy()


    def strategy_Random(self):
        while True:
            if input("Press enter to generate a new random combination. ") == "":
                return random.sample(range(0, self.__numberOfColors), self.__lengthOfGuess)


    def strategy_automaticRandom(self):
        return random.sample(range(0, self.__numberOfColors), self.__lengthOfGuess)


    def strategy_automaticImprovedRandom(self):
        newCombination = random.sample(range(0, self.__numberOfColors), self.__lengthOfGuess)
        allWrongCombinations = []
        try:
            allWrongCombinations = self.__attempts.getCombinationsWithNoRightColor()
        except ValueError:
            pass
        while self.__attempts.checkIfCombinationExist(newCombination) \
                or newCombination in allWrongCombinations:
            newCombination = random.sample(range(0, self.__numberOfColors), self.__lengthOfGuess)
        return newCombination