
from GameCoordinator import GameCoordinator
from GameLogic.Colorcombination import Colorcombination

gc = GameCoordinator(4, 8, Colorcombination([0, 1, 2, 3]), 100)
gc.playGame()