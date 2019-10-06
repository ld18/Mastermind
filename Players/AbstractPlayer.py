
import abc

class AbstractPlayer(abc.ABC):

    def __init__(self):
        super().__init__()

    @abc.abstractmethod
    def readInputIn(self):
        pass


    @abc.abstractmethod
    def introduceYourself(self):
        pass


    def debriefing(self, obviousError):
        pass