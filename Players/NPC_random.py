
import random
from Players.AbstractPlayer import AbstractPlayer

class NPC_random(AbstractPlayer):

    def __init__(self, lengthOfGuess, numberOfColors, attempts):
        self.__lengthOfGuess = lengthOfGuess
        self.__numberOfColors = numberOfColors
        self.__attempts = attempts
        self.strategy = self.strategy_automaticRandom

    def introduceYourself(self):
        print("This NPC tries to solve Mastermind by using his luck and random combinations.\n")


    def readInputIn(self):
        return self.strategy()


    def strategy_Random(self):
        while True:
            if input("Press enter to generate a new random combination. ") == "":
                return random.sample(range(0, self.__numberOfColors), self.__lengthOfGuess)


    def strategy_automaticRandom(self):
        return random.sample(range(0, self.__numberOfColors), self.__lengthOfGuess)