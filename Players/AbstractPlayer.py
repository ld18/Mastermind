
import abc

class AbstractPlayer(abc.ABC):

    def __init__(self):
        super().__init__()

    @abc.abstractmethod
    def readInputIn(self):
        pass