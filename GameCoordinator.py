
from GameLogic.Validator import Validator
from GameLogic.Evaluator import Evaluator
from GameLogic.EvaluatedCombination import EvaluatedCombination
from GameLogic.Attempts import Attempts
from GameLogic.Colorcombination import Colorcombination
from GameLogic.FinalScore import FinalScore
from Players.HumanPlayer import HumanPlayer
from Players.NPC import NPC

class GameCoordinator():

    def __init__(self, lengthOfGuess, numberOfColors, masterCombination, maxNumberOfAttempts):
        self.__gameIsRunning = False
        self.__validator = Validator(lengthOfGuess, numberOfColors)
        self.__masterCombination = masterCombination
        self.__validator.validateCombination(masterCombination)
        self.__evaluator = Evaluator(masterCombination)
        self.__attempts = Attempts(commentate = False)
        self.__maxNumberOfAttempts = maxNumberOfAttempts
        self.__validator.validateMaxNumberOfAttempts(maxNumberOfAttempts)
        self.player = NPC(lengthOfGuess, numberOfColors, self.__attempts)  #HumanPlayer()


    def playGame(self):
        if not self.__gameIsRunning:
            self.__gameStart()
            while self.__gameIsRunning:
                if self.__attempts.getNumberOfAttempts() < self.__maxNumberOfAttempts:
                    self.__playRound()
                else:
                    self.__gameLost()
                    return FinalScore(False, self.__attempts.getNumberOfAttempts())
            return FinalScore(True, self.__attempts.getNumberOfAttempts())


    def __gameStart(self):
        self.__attempts.clearAttempts()
        self.__gameIsRunning = True
        print("Started a new MindMaster Game.")
        print("Setup is "+ str(self.__validator) +", you have a maximum number of "+ str(self.__maxNumberOfAttempts) +" attempts.\n")


    def __playRound(self):
        gameIsFinished = self.__getAndProcessCombination()
        if gameIsFinished:
            self.__gameWon()
        else:
            print(str(self.__attempts.getLastAttempt()) +" {"+ str(self.__attempts.getNumberOfAttempts()) +"/"+ str(self.__maxNumberOfAttempts) +"}")


    def __gameLost(self):
        self.__gameIsRunning = False
        print("\nYou lost the game.")
        print("You have reached the maximum number of "+ str(self.__attempts.getNumberOfAttempts()) +" tries.")
        print("You best attempt was "+ str(self.__attempts.getBestAttempt()) +".")


    def __gameWon(self):
        self.__gameIsRunning = False
        try:
            self.__validator.validateAttempts(self.__attempts)
        except ValueError:
            print("\n Game has ended, but there was an error.")

        print("\nYou won the game.")
        print("The MasterCombination was: " + str(self.__masterCombination) + ". You needed " + str(
            self.__attempts.getNumberOfAttempts()) + " of " + str(self.__maxNumberOfAttempts) + " tries.")
        debriefing = self.__validator.validateForNoObviousErrors(self.__attempts)
        print(debriefing)


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
