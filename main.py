
from GameLogic.Evaluator import Evaluator
from GameLogic.Attempts import Attempts

evaluator = Evaluator([0, 1, 2, 6], 8)
guesCombi = Attempts(evaluator)
print(guesCombi)
guesCombi.evaluateAndAddCombination([4, 5, 6, 7])
guesCombi.evaluateAndAddCombination([4, 5, 7, 6])
guesCombi.evaluateAndAddCombination([4, 5, 0, 6])
guesCombi.evaluateAndAddCombination([4, 0, 7, 6])
guesCombi.evaluateAndAddCombination([0, 5, 7, 6])
guesCombi.evaluateAndAddCombination([0, 5, 1, 6])
guesCombi.evaluateAndAddCombination([0, 5, 4, 6])
print(guesCombi)
print(guesCombi.getBestAttempt())