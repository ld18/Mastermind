
from GameLogic.Validator import Validator
from GameLogic.Evaluator import Evaluator
from GameLogic.EvaluatedCombination import EvaluatedCombination
from GameLogic.Attempts import Attempts
from GameLogic.Colorcombination import Colorcombination
from GameLogic.FinalScore import FinalScore
from Players.HumanPlayer import HumanPlayer
from Players.NPC_hardCoded import NPC_hardCoded
from Players.NPC_random import NPC_random
from Players.NPC_csp import NPC_csp

class GameCoordinator():

    def __init__(self, lengthOfGuess, numberOfColors, masterCombination, maxNumberOfAttempts):
        self.__gameIsRunning = False
        self.__validator = Validator(lengthOfGuess, numberOfColors)
        self.__masterCombination = masterCombination
        self.__validator.validateCombination(masterCombination)
        self.__evaluator = Evaluator(masterCombination)
        self.__attempts = Attempts()
        self.__maxNumberOfAttempts = maxNumberOfAttempts
        self.__validator.validateMaxNumberOfAttempts(maxNumberOfAttempts)
        #self.player = HumanPlayer()
        #self.player = NPC_random(lengthOfGuess, numberOfColors, self.__attempts)
        #self.player = NPC_hardCoded(lengthOfGuess, numberOfColors, self.__attempts)
        self.player = NPC_csp(lengthOfGuess, numberOfColors, self.__attempts)


    def playGame(self):
        if not self.__gameIsRunning:
            self.__gameStart()
            while self.__gameIsRunning:
                if self.__attempts.getNumberOfAttempts() < self.__maxNumberOfAttempts:
                    self.__playRound()
                else:
                    self.__gameLost()
                    return FinalScore(False, self.__attempts.getNumberOfAttempts(), self.__validator.validateForNoObviousErrors(self.__attempts))
            return FinalScore(True, self.__attempts.getNumberOfAttempts(), self.__validator.validateForNoObviousErrors(self.__attempts))


    def __gameStart(self):
        self.__attempts.clearAttempts()
        self.__gameIsRunning = True
        print("\nStarted a new MindMaster Game.")
        print("Setup is "+ str(self.__validator) +", you have a maximum number of "+ str(self.__maxNumberOfAttempts) +" attempts.")
        self.player.introduceYourself()


    def __endGame(self):
        self.__gameIsRunning = False
        self.player.debriefing(self.__validator.validateForNoObviousErrors(self.__attempts))


    def __playRound(self):
        gameIsFinished = self.__getAndProcessCombination()
        if gameIsFinished:
            self.__gameWon()
        else:
            print(str(self.__attempts.getLastAttempt()) +" {"+ str(self.__attempts.getNumberOfAttempts()) +"/"+ str(self.__maxNumberOfAttempts) +"}")


    def __gameLost(self):
        self.__endGame()
        print("\nYou lost the game.")
        print("You have reached the maximum number of "+ str(self.__attempts.getNumberOfAttempts()) +" tries.")
        print("You best attempt was "+ str(self.__attempts.getBestAttempt()) +".")


    def __gameWon(self):
        self.__endGame()
        try:
            self.__validator.validateAttempts(self.__attempts)
        except ValueError:
            print("\n Game has ended, but there was an error.")

        print("\nYou won the game.")
        print("The MasterCombination was: " + str(self.__masterCombination) + ". You needed " + str(
            self.__attempts.getNumberOfAttempts()) + " of " + str(self.__maxNumberOfAttempts) + " tries.")
        if self.__validator.validateForNoObviousErrors(self.__attempts):
            print("\nBut you could have done better, believe me ..")


    def __getAndProcessCombination(self):
        newCombination = self.__getNewUserCombination()
        evaluation = self.__evaluator.evaluateCombination(newCombination)
        self.__attempts.addEvaluatedCombination(EvaluatedCombination(newCombination, evaluation))
        return evaluation.gameFinished


    def __getNewUserCombination(self):
        while(True):
            try:
                userCmbi = Colorcombination(self.player.readInputIn())
                self.__validator.validateCombination(userCmbi)
                break
            except ValueError as e:
                print(str(e) +". Combination not valid, do it again. Just write the color values seperated by a whitespace and hit enter.")
        return userCmbi
