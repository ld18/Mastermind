
import random
from ManagementFunctions.GameCoordinator import GameCoordinator
from GameLogic.Colorcombination import Colorcombination

numberOfColors = 8
lengthOfGuess = 4
maximumNumberOfGuesses = 100
masterCombination = Colorcombination(random.sample(range(0, numberOfColors), lengthOfGuess))
#masterCombination = Colorcombination([0, 1, 2, 3])

gc = GameCoordinator(lengthOfGuess, numberOfColors, masterCombination, maximumNumberOfGuesses)
gc.playGame()
