

class FinalScore():

    def __init__(self, gameWon, numberOfAttempts):
        self.gameWon = gameWon
        self.numberOfAttempts = numberOfAttempts


    def __eq__(self, other):
        if self.gameWon != other.gameWon\
                or self.numberOfAttempts != other.numberOfAttempts:
            return False
        return True


    def __str__(self):
        representation = "Defeat "
        if self.gameWon:
            representation = "Victory "
        representation += "after " + str(self.numberOfAttempts) +" attempts"
        return representation
