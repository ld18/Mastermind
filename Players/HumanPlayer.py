
from Players.AbstractPlayer import AbstractPlayer

class HumanPlayer(AbstractPlayer):

    def readInputIn(self):
        rawInput = input("Whats your new guessed combination? ")
        processedInput = [int(x) for x in rawInput.split()]
        #print(rawInput +" "+ str(processedInput))
        return processedInput


    def introduceYourself(self):
        print("You have to type a combination and hit enter. \n"
              "A combination can looks like this (here: lenght of guess = 4, number of colors (at least) = 7: 3 4 6 1 \n")