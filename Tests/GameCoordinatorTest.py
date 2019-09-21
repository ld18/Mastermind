
from GameCoordinator import GameCoordinator
from GameLogic.FinalScore import FinalScore
from Players.TestPlayer import TestPlayer
from twisted.trial import unittest

class EvaluationTest(unittest.TestCase):

    def testFunction_Constructor(self):
        #valid construcotrs
        sud = GameCoordinator(1, 2, [0], 1)
        sud = GameCoordinator(2, 2, [0, 1], 2)

        sud = GameCoordinator(1, 1, [0], 1)
        sud = GameCoordinator(1, 2, [0], 1)

        sud = GameCoordinator(1, 2, [0], 1)
        sud = GameCoordinator(1, 2, [1], 1)
        sud = GameCoordinator(2, 2, [0, 1], 1)
        sud = GameCoordinator(2, 2, [1, 0], 1)

        sud = GameCoordinator(1, 2, [0], 2)

        sud = GameCoordinator(4, 8, [0, 1, 2, 3], 10)
        sud = GameCoordinator(4, 8, [7, 6, 5, 4], 10)
        sud = GameCoordinator(1, 8, [7], 1)
        sud = GameCoordinator(1, 3, [2], 55)


    def testError_Constructor(self):
        #invalid construcotrs
        with self.assertRaises(ValueError):
            sud = GameCoordinator(-1, 1, [0], 1)
        with self.assertRaises(ValueError):
            sud = GameCoordinator(0, 1, [0], 1)
        with self.assertRaises(ValueError):
            sud = GameCoordinator(2, 1, [0], 1)

        with self.assertRaises(ValueError):
            sud = GameCoordinator(1, -1, [0], 1)
        with self.assertRaises(ValueError):
            sud = GameCoordinator(1, 0, [0], 1)

        with self.assertRaises(ValueError):
            sud = GameCoordinator(1, 1, 0, 1)
        with self.assertRaises(ValueError):
            sud = GameCoordinator(1, 1, 'v', 1)
        with self.assertRaises(ValueError):
            sud = GameCoordinator(1, 1, 0, 1)
        with self.assertRaises(ValueError):
            sud = GameCoordinator(1, 1, 'v', 1)
        with self.assertRaises(ValueError):
            sud = GameCoordinator(1, 1, [], 1)
        with self.assertRaises(ValueError):
            sud = GameCoordinator(1, 1, [-1], 1)
        with self.assertRaises(ValueError):
            sud = GameCoordinator(1, 1, [1], 1)
        with self.assertRaises(ValueError):
            sud = GameCoordinator(1, 1, [0, 0], 1)
        with self.assertRaises(ValueError):
            sud = GameCoordinator(1, 1, [0, 1], 1)

        with self.assertRaises(ValueError):
            sud = GameCoordinator(1, 2, [0], -1)
        with self.assertRaises(ValueError):
            sud = GameCoordinator(1, 2, [0], 0)


    def testError_playGame(self):
        sud = GameCoordinator(4, 8, [0, 1, 2, 3], 4)
        tp = TestPlayer([
            [0, 1, 2, 3]])
        sud.player = tp
        finalScore = sud.playGame()
        self.assertEqual(finalScore == FinalScore(True, 1), True)

        tp = TestPlayer([
            [0, 1, 2, 4],
            [0, 1, 2, 3]])
        sud.player = tp
        finalScore = sud.playGame()
        self.assertEqual(finalScore == FinalScore(True, 2), True)

        tp = TestPlayer([
            [0, 1, 2, 44],
            [0, 1, 2, 7],
            [0, 1, 2, 3]])
        sud.player = tp
        finalScore = sud.playGame()
        self.assertEqual(finalScore == FinalScore(True, 2), True)

        tp = TestPlayer([
            [0, 1, 2, 44],
            [0, 1, 2, 7],
            [0, -1, 2, 7],
            [0, 6, 2, 6],
            [0, 1, 2, 3]])
        sud.player = tp
        finalScore = sud.playGame()
        self.assertEqual(finalScore == FinalScore(True, 2), True)

        tp = TestPlayer([
            [0, 1, 2, 7],
            [0, 4, 2, 6],
            [0, 4, 1, 6],
            [0, 1, 2, 3]])
        sud.player = tp
        finalScore = sud.playGame()
        self.assertEqual(finalScore == FinalScore(True, 4), True)

        tp = TestPlayer([
            [0, 1, 2, 7],
            [0, 4, 2, 6],
            [0, 4, 1, 6],
            [0, 1, 2, 6]])
        sud.player = tp
        finalScore = sud.playGame()
        self.assertEqual(finalScore == FinalScore(False, 4), True)

if __name__ == '__main__':
    unittest.main()
