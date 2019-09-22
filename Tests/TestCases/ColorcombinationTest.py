
from GameLogic.Colorcombination import Colorcombination
from twisted.trial import unittest

class Testcases(unittest.TestCase):


    def testAll(self):
        self.test_eq()
        self.test_hasAnyColorInCommon()


    def test_eq(self):
        #equal evaluations
        self.assertEqual(Colorcombination([]) == Colorcombination([]), True)
        self.assertEqual(Colorcombination([1]) == Colorcombination([1]), True)
        self.assertEqual(Colorcombination([1, 2]) == Colorcombination([1, 2]), True)
        self.assertEqual(Colorcombination([1, 5, 8]) == Colorcombination([1, 5, 8]), True)
        self.assertEqual(Colorcombination([9, 3, 1, 0]) == Colorcombination([9, 3, 1, 0]), True)

        #unequal evaluations
        self.assertEqual(Colorcombination([]) == Colorcombination([1]), False)
        self.assertEqual(Colorcombination([2]) == Colorcombination([1]), False)
        self.assertEqual(Colorcombination([-1]) == Colorcombination([1]), False)
        self.assertEqual(Colorcombination([2, 1]) == Colorcombination([1, 2]), False)
        self.assertEqual(Colorcombination([2, 1]) == Colorcombination([2, 1, 9]), False)
        self.assertEqual(Colorcombination([2, 1, 9]) == Colorcombination([2, 1]), False)


    def test_hasAnyColorInCommon(self):
        self.assertEqual(Colorcombination([1]).hasAnyColorInCommon(Colorcombination([1])), True)
        self.assertEqual(Colorcombination([1]).hasAnyColorInCommon(Colorcombination([1, 2, 3, 45])), True)
        self.assertEqual(Colorcombination([1]).hasAnyColorInCommon(Colorcombination([2, 4, -1, 1])), True)
        self.assertEqual(Colorcombination([1, 5]).hasAnyColorInCommon(Colorcombination([1, 4, 7, 2, 5, 6])), True)

        self.assertEqual(Colorcombination([1]).hasAnyColorInCommon(Colorcombination([])), False)
        self.assertEqual(Colorcombination([]).hasAnyColorInCommon(Colorcombination([])), False)
        self.assertEqual(Colorcombination([]).hasAnyColorInCommon(Colorcombination([1])), False)
        self.assertEqual(Colorcombination([1]).hasAnyColorInCommon(Colorcombination([])), False)
        self.assertEqual(Colorcombination([]).hasAnyColorInCommon(Colorcombination([1])), False)
        self.assertEqual(Colorcombination([1]).hasAnyColorInCommon(Colorcombination([2])), False)
        self.assertEqual(Colorcombination([1]).hasAnyColorInCommon(Colorcombination([2, 3, 45])), False)
        self.assertEqual(Colorcombination([5]).hasAnyColorInCommon(Colorcombination([2, 4, -1, 1])), False)
        self.assertEqual(Colorcombination([1, 5]).hasAnyColorInCommon(Colorcombination([0, 4, 7, 2, 9, 6])), False)


    def test_hasAllColorsInCommon(self):
        self.assertEqual(Colorcombination([]).hasAllColorsInCommon(Colorcombination([])), True)
        self.assertEqual(Colorcombination([1]).hasAllColorsInCommon(Colorcombination([1])), True)
        self.assertEqual(Colorcombination([1, 2]).hasAllColorsInCommon(Colorcombination([1, 2])), True)
        self.assertEqual(Colorcombination([2, 1]).hasAllColorsInCommon(Colorcombination([1, 2])), True)
        self.assertEqual(Colorcombination([1, 2]).hasAllColorsInCommon(Colorcombination([2, 1])), True)
        self.assertEqual(Colorcombination([1, 2, 3, 4]).hasAllColorsInCommon(Colorcombination([1, 2, 4, 3])), True)
        self.assertEqual(Colorcombination([1, 2, 3, 4]).hasAllColorsInCommon(Colorcombination([4, 3, 1, 2])), True)
        self.assertEqual(Colorcombination([1, 2, 3, 4]).hasAllColorsInCommon(Colorcombination([2, 4, 1, 3])), True)

        self.assertEqual(Colorcombination([1]).hasAllColorsInCommon(Colorcombination([])), False)
        self.assertEqual(Colorcombination([]).hasAllColorsInCommon(Colorcombination([1])), False)
        self.assertEqual(Colorcombination([1, 2]).hasAllColorsInCommon(Colorcombination([1, 2, 3])), False)
        self.assertEqual(Colorcombination([2, 1]).hasAllColorsInCommon(Colorcombination([3, 1, 2])), False)
        self.assertEqual(Colorcombination([3, 1, 2]).hasAllColorsInCommon(Colorcombination([2, 1])), False)
        self.assertEqual(Colorcombination([1, 2, 3, 4]).hasAllColorsInCommon(Colorcombination([1, 5, 4, 3])), False)
        self.assertEqual(Colorcombination([1, 2, 3, 5]).hasAllColorsInCommon(Colorcombination([4, 3, 1, 2])), False)
        self.assertEqual(Colorcombination([1, 2, 3, 4]).hasAllColorsInCommon(Colorcombination([2, 4, 1, 3, 0])), False)
        self.assertEqual(Colorcombination([1, 2, 3, 6, 4]).hasAllColorsInCommon(Colorcombination([2, 4, 1, 3])), False)


if __name__ == '__main__':
    unittest.main()
