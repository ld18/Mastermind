
from termcolor import colored

class Evaluation():
    def __init__(self, rightColorWrongPlace, rightColorRightPlace, gameFinished):
        self.rightColorWrongPlace = rightColorWrongPlace
        self.rightColorRightPlace = rightColorRightPlace
        self.gameFinished = gameFinished


    def getNumberOfRightColors(self):
        return self.rightColorWrongPlace + self.rightColorRightPlace


    def __eq__(self, other):
        if self.rightColorWrongPlace != other.rightColorWrongPlace\
                or self.rightColorRightPlace != other.rightColorRightPlace \
                or self.gameFinished != other.gameFinished:
            return False
        return True


    def __gt__(self, other):
        if self.rightColorRightPlace > other.rightColorRightPlace:
            return True
        elif self.rightColorWrongPlace > other.rightColorWrongPlace:
            return True
        return False


    def __str__(self):
        representation = "(" + str(self.rightColorWrongPlace) + "w|" + str(self.rightColorRightPlace) + "r)"
        return representation
