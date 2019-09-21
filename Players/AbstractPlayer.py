
from abc import ABC, abstractmethod

class AbstractPlayer(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def readInputIn(self):
        pass