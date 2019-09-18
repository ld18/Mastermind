
from GameLogic.Validator import Validator
from GameLogic.Evaluator import Evaluator
from GameLogic.EvaluatedCombination import EvaluatedCombination
from GameLogic.Attempts import Attempts
from Players.HumanPlayer import HumanPlayer

class GameCoordinator():

    def __init__(self, lengthOfGuess, numberOfColors, masterCombination):
        self.__gameIsRunning = False
        self.__player = HumanPlayer()
        self.__masterCombination = masterCombination
        self.__validator = Validator(lengthOfGuess, numberOfColors)
        self.__validator.checkCombination(self.__masterCombination)
        self.__evaluator = Evaluator(self.__masterCombination)
        self.__attempts = Attempts()


    def prepareForNewGame(self):
        self.__attempts.clearAttempts()
        self.__gameIsRunning = True


    def playGame(self):
        if self.__gameIsRunning:
            print("Start a new MindMaster Game. Setup is "+ str(self.__validator) +".")
            while self.__gameIsRunning:
                self.__playRound()
                if self.__gameIsRunning:
                    print(self.__attempts.getLastAttempt())


    def __playRound(self):
        if self.__gameIsRunning:
            gameIsFinished = self.__getAndProcessCombination()
            if gameIsFinished:
                self.__gameIsRunning = False
                print("You won the game. The MasterCombination was: " + str(self.__masterCombination))
                print("You needed " + str(self.__attempts.getNumberOfAttempts()) + " tries.")


    def __getAndProcessCombination(self):
        newCombination = self.__getNewUserCombination()
        evaluation = self.__evaluator.evaluateCombination(newCombination)
        self.__attempts.addEvaluatedCombination(EvaluatedCombination(newCombination, evaluation))
        return evaluation.gameFinished


    def __getNewUserCombination(self):
        while(True):
            try:
                userCmbi = self.__player.readInputIn()
                self.__validator.checkCombination(userCmbi)
                break
            except ValueError as e :
                print(str(e) +". Combination not valid, do it again. ")
        return userCmbi
