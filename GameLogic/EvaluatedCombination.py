
class EvaluatedCombination():

    def __init__(self, colorCombination, evaluation):
        self.colorCombination = colorCombination
        self.evaluation = evaluation


    def __eq__(self, other):
        if self.colorCombination != other.colorCombination \
                or self.evaluation != other.evaluation:
            return False
        return True


    def __str__(self):
        representation = str(self.colorCombination) + " " + str(self.evaluation)
        return representation