
from Valuator import Valuator
from twisted.trial import unittest

import time

class ValuatorTest(unittest.TestCase):

    def test_Constructor(self):
        #normale konstruktoren
        for numColors in range(1, 10):
            for guessLenght in range(1, numColors + 1):
                masterCombi = list(range(0,guessLenght))
                valuator = Valuator(masterCombi, numColors)

        #leere master combi
        masterCombi = list(range(0, 0))
        with self.assertRaises(ValueError):
            valuator = Valuator(masterCombi, 1)

        #falsche number of colors werte
        masterCombi = list(range(0, 4))
        with self.assertRaises(ValueError):
            valuator = Valuator(masterCombi, -1)
        masterCombi = list(range(0, 4))
        with self.assertRaises(ValueError):
            valuator = Valuator(masterCombi, 0)
        masterCombi = list(range(0, 4))
        with self.assertRaises(ValueError):
            valuator = Valuator(masterCombi, 1)
        masterCombi = list(range(0, 4))
        with self.assertRaises(ValueError):
            valuator = Valuator(masterCombi, 3)


        #falsche colorerte
        masterCombi = list(range(-1, 3))
        with self.assertRaises(ValueError):
            valuator = Valuator(masterCombi, 8)
        masterCombi = list(range(5, 9))
        with self.assertRaises(ValueError):
            valuator = Valuator(masterCombi, 8)

        #doppelte werte
        masterCombi = list(range(0, 2)) * 2
        with self.assertRaises(ValueError):
            valuator = Valuator(masterCombi, 8)


if __name__ == '__main__':
    unittest.main()
