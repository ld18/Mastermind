
from GameLogic.Evaluator import Evaluator
from GameLogic.AttemptCollection import AttemptCollection

evaluator = Evaluator([0, 1, 2, 6], 8)
guesCombi = AttemptCollection(evaluator)
print(guesCombi)
guesCombi.evaluateAndAddCombination([4, 5, 6, 7])
guesCombi.evaluateAndAddCombination([4, 5, 7, 6])
guesCombi.evaluateAndAddCombination([4, 5, 0, 6])
guesCombi.evaluateAndAddCombination([4, 0, 7, 6])
guesCombi.evaluateAndAddCombination([0, 5, 7, 6])
print(guesCombi)
