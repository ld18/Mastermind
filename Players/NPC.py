
import random
from itertools import permutations
from Players.AbstractPlayer import AbstractPlayer
from GameLogic.Colorcombination import Colorcombination

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
        newCombination = self.__generateNewCombinatio()
        while self.__checkForDeadLoss(newCombination) \
                or self.__checkForDuplicate(newCombination):
            newCombination = self.__generateNewCombinatio()
        return newCombination


    def __generateNewCombinatio(self):
        newCombination = random.sample(range(0, self.__numberOfColors), self.__lengthOfGuess)
        try:
            allRightColorsCombination = self.__attempts.getCombinationWithAllRightColors()
            newPossibleCombinations = list(permutations(allRightColorsCombination.colorCombination))
            for index, newPossibleCombination in enumerate(newPossibleCombinations):
                newPossibleCombination = list(newPossibleCombination)
                if not self.__checkForDuplicate(newPossibleCombination) and index > 0:
                    newCombination = newPossibleCombination
                    #print("__generateNewCombinatio "+ str(newCombination))
                    break
        except ValueError:
            pass
        return newCombination


    def __checkForDeadLoss(self, combination):
        try:
            allWrongCombinations = self.__attempts.getCombinationsWithNoRightColor()
            for wrongCombination in allWrongCombinations:
                if Colorcombination(combination).hasAnyColorInCommon(wrongCombination):
                    #print("__checkForDeadLoss "+ str(combination))
                    return True
        except ValueError:
            pass
        return False


    def __checkForDuplicate(self, combination):
        if self.__attempts.checkIfCombinationExist(Colorcombination(combination)):
            #print("__checkForDuplicate " + str(combination))
            return True
        return False