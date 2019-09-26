

class Debriefing():

    def __init__(self, obiuseError, comment):
        self.obiuseError = obiuseError
        self.comment = comment


    def __str__(self):
        comment =""
        if self.obiuseError:
            comment += "\nBut you could have done better, believe me ..\n"
            comment += self.comment + "\nThere maybe even be more of this kind!"
        return comment
