
from GameCoordinator import GameCoordinator
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


if __name__ == '__main__':
    unittest.main()
