

class FinalScore():

    def __init__(self, gameWon, numberOfAttempts, obviousError):
        self.gameWon = gameWon
        self.numberOfAttempts = numberOfAttempts
        self.obviousError = obviousError


    def __eq__(self, other):
        if self.gameWon != other.gameWon\
                or self.numberOfAttempts != other.numberOfAttempts\
                or self.obviousError != other.obviousError:
            return False
        return True


    def __str__(self):
        representation = "Defeat "
        if self.gameWon:
            representation = "Victory "
        representation += "after " + str(self.numberOfAttempts) +" attempts"
        representation += "with "
        if self.obviousError:
            representation += "some "
        else:
            representation += "no "
        representation += "obvious Errors."
        return representation
