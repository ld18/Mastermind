
from termcolor import colored

class Evaluation():
    def __init__(self, rightColorWrongPlace, rightColorRightPlace, gameFinished):
        self.rightColorWrongPlace = rightColorWrongPlace
        self.rightColorRightPlace = rightColorRightPlace
        self.gameFinished = gameFinished


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
        representation = "("
        if self.rightColorWrongPlace > 0:
            representation += str(self.rightColorWrongPlace)
        else:
            representation += "-"
        representation += "w|"
        if self.rightColorRightPlace > 0:
            representation += colored(str(self.rightColorRightPlace) +"r", 'red')
        else:
            representation += "-r"
        representation += ")"
        return representation
