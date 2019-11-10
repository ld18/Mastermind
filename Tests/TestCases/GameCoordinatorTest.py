
from ManagementFunctions.GameCoordinator import GameCoordinator
from GameLogic.FinalScore import FinalScore
from GameLogic.Colorcombination import Colorcombination
from Players.TestPlayer import TestPlayer
from twisted.trial import unittest

class Testcases(unittest.TestCase):

    def testAll(self):
        self.testFunction_Constructor()
        self.testError_Constructor()
        self.testError_playGame()


    def testFunction_Constructor(self):
        #valid construcotrs
        sud = GameCoordinator(1, 2, Colorcombination([0]), 1)
        sud = GameCoordinator(2, 2, Colorcombination([0, 1]), 2)

        sud = GameCoordinator(1, 1, Colorcombination([0]), 1)
        sud = GameCoordinator(1, 2, Colorcombination([0]), 1)

        sud = GameCoordinator(1, 2, Colorcombination([0]), 1)
        sud = GameCoordinator(1, 2, Colorcombination([1]), 1)
        sud = GameCoordinator(2, 2, Colorcombination([0, 1]), 1)
        sud = GameCoordinator(2, 2, Colorcombination([1, 0]), 1)

        sud = GameCoordinator(1, 2, Colorcombination([0]), 2)

        sud = GameCoordinator(4, 8, Colorcombination([0, 1, 2, 3]), 10)
        sud = GameCoordinator(4, 8, Colorcombination([7, 6, 5, 4]), 10)
        sud = GameCoordinator(1, 8, Colorcombination([7]), 1)
        sud = GameCoordinator(1, 3, Colorcombination([2]), 55)


    def testError_Constructor(self):
        #invalid construcotrs
        with self.assertRaises(ValueError):
            sud = GameCoordinator(-1, 1, Colorcombination([0]), 1)
        with self.assertRaises(ValueError):
            sud = GameCoordinator(0, 1, Colorcombination([0]), 1)
        with self.assertRaises(ValueError):
            sud = GameCoordinator(2, 1, Colorcombination([0]), 1)

        with self.assertRaises(ValueError):
            sud = GameCoordinator(1, -1, Colorcombination([0]), 1)
        with self.assertRaises(ValueError):
            sud = GameCoordinator(1, 0, Colorcombination([0]), 1)

        with self.assertRaises(AttributeError):
            sud = GameCoordinator(1, 1, 0, 1)
        with self.assertRaises(AttributeError):
            sud = GameCoordinator(1, 1, 'v', 1)
        with self.assertRaises(AttributeError):
            sud = GameCoordinator(1, 1, 0, 1)
        with self.assertRaises(AttributeError):
            sud = GameCoordinator(1, 1, 'v', 1)
        with self.assertRaises(AttributeError):
            sud = GameCoordinator(1, 1, [], 1)

        with self.assertRaises(ValueError):
            sud = GameCoordinator(1, 1, Colorcombination([]), 1)
        with self.assertRaises(ValueError):
            sud = GameCoordinator(1, 1, Colorcombination([-1]), 1)
        with self.assertRaises(ValueError):
            sud = GameCoordinator(1, 1, Colorcombination([1]), 1)
        with self.assertRaises(ValueError):
            sud = GameCoordinator(1, 1, Colorcombination([0, 0]), 1)
        with self.assertRaises(ValueError):
            sud = GameCoordinator(1, 1, Colorcombination([0, 1]), 1)

        with self.assertRaises(ValueError):
            sud = GameCoordinator(1, 2, Colorcombination([0]), -1)
        with self.assertRaises(ValueError):
            sud = GameCoordinator(1, 2, Colorcombination([0]), 0)


    def testError_playGame(self):
        sud = GameCoordinator(4, 8, Colorcombination([0, 1, 2, 3]), 4)
        tp = TestPlayer([
            [0, 1, 2, 3]])
        sud.player = tp
        finalScore = sud.playGame()
        self.assertEqual(finalScore == FinalScore(True, 1, False), True)

        tp = TestPlayer([
            [0, 1, 2, 4],
            [0, 1, 2, 3]])
        sud.player = tp
        finalScore = sud.playGame()
        self.assertEqual(finalScore == FinalScore(True, 2, False), True)

        tp = TestPlayer([
            [0, 1, 2, 44],
            [0, 1, 2, 7],
            [0, 1, 2, 3]])
        sud.player = tp
        finalScore = sud.playGame()
        self.assertEqual(finalScore == FinalScore(True, 2, False), True)

        tp = TestPlayer([
            [0, 1, 2, 44],
            [0, 1, 2, 7],
            [0, -1, 2, 7],
            [0, 6, 2, 6],
            [0, 1, 2, 3]])
        sud.player = tp
        finalScore = sud.playGame()
        self.assertEqual(finalScore == FinalScore(True, 2, False), True)

        tp = TestPlayer([
            [0, 1, 2, 7],
            [0, 4, 2, 6],
            [0, 4, 1, 6],
            [0, 1, 2, 3]])
        sud.player = tp
        finalScore = sud.playGame()
        self.assertEqual(finalScore == FinalScore(True, 4, False), True)

        tp = TestPlayer([
            [0, 1, 2, 7],
            [0, 4, 2, 6],
            [0, 4, 1, 6],
            [0, 1, 2, 6]])
        sud.player = tp
        finalScore = sud.playGame()
        self.assertEqual(finalScore == FinalScore(False, 4, False), True)


if __name__ == '__main__':
    unittest.main()