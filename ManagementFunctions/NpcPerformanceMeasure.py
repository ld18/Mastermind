
import random
import io
import sys
import constraint
from ManagementFunctions.GameCoordinator import GameCoordinator
from GameLogic.Colorcombination import Colorcombination
from Players.NPC_random import NPC_random
from Players.NPC_hardCoded import NPC_hardCoded
from Players.NPC_csp import NPC_csp

numberOfColors = 8
lengthOfGuess = 4
maximumNumberOfGuesses = 100
numberOfGamesToPlay = 1000

def startPerformanceTests(sud, resetNPC = None):
    numberOfWins = 0
    totalNumberOfAttempts = 0
    numberOfObviousErrors = 0

    text_trap = io.StringIO()
    sys.stdout = text_trap
    for count in range(numberOfGamesToPlay):
        setNewRandomMasterCombination(sud)
        resetEnvironment(sud, resetNPC)
        finalScore = sud.playGame()
        if finalScore.gameWon:
            numberOfWins += 1
        totalNumberOfAttempts += finalScore.numberOfAttempts
        if finalScore.obviousError:
            numberOfObviousErrors += 1
    sys.stdout = sys.__stdout__
    print("\tnumberOfWins: "+ str(numberOfWins) +"/" +str(numberOfGamesToPlay)
          +", totalNumberOfAttempts:"+ str(totalNumberOfAttempts)
          +", numberOfAttempts:"+ str(totalNumberOfAttempts/numberOfGamesToPlay)+" per game"
          +", numberOfObviousErrors:"+ str(numberOfObviousErrors) +"/" +str(numberOfGamesToPlay)
          )


def setNewRandomMasterCombination(sud):
    masterCombination = Colorcombination(random.sample(range(0, numberOfColors), lengthOfGuess))
    sud.setMasterCombination(masterCombination)


def resetEnvironment(sud, resetNPC):
    sud.attempts.clearAttempts()
    if resetNPC != None:
        resetNPC()


def testAllNPCs():
    masterCombination = Colorcombination(random.sample(range(0, numberOfColors), lengthOfGuess))
    gameCoordinator = GameCoordinator(lengthOfGuess, numberOfColors, masterCombination, maximumNumberOfGuesses)
    print("\nStart all performance tests.\n")

    print("NPC_random performance test")
    npc = NPC_random(lengthOfGuess, numberOfColors, gameCoordinator.attempts)
    npc.strategy = npc.strategy_automaticRandom
    gameCoordinator.player = npc
    startPerformanceTests(gameCoordinator)

    print("NPC_hardCoded performance test")
    npc = NPC_hardCoded(lengthOfGuess, numberOfColors, gameCoordinator.attempts)
    npc.strategy = npc.strategy_automaticImprovedRandom
    gameCoordinator.player = npc
    startPerformanceTests(gameCoordinator)

    print("NPC_csp performance test ")
    npc = NPC_csp(lengthOfGuess, numberOfColors, gameCoordinator.attempts)
    npc.strategy = npc.strategy_getNextPossibleCombination
    npc.cspSolvingStrategy = constraint.BacktrackingSolver()
    gameCoordinator.player = npc
    startPerformanceTests(gameCoordinator, npc.resetProblems)

    print("\nSucessfully performed all performance tests.")


if __name__ == '__main__':
    testAllNPCs()