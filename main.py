from Valuator import Valuator
from GuessedCombination import GuessedCombination

validator = Valuator([0, 1, 2, 6], 8)
guesCombi = GuessedCombination(validator)
print(guesCombi)
guesCombi.evaluateAndAddCombination([5, 1, 6, 2])
guesCombi.evaluateAndAddCombination([1, 1, 2, 3])
print(guesCombi)