

class Colorcombination():

    def __init__(self, colorCombination):
        self.colorCombination = colorCombination


    def __len__(self):
        return len(self.colorCombination)


    def __eq__(self, other):
        if self.colorCombination != other.colorCombination:
            return False
        return True


    def hasAnyColorInCommon(self, other):
        return len(set(self.colorCombination).intersection(set(other.colorCombination))) > 0


    def hasAllColorsInCommon(self, other):
        if len(self.colorCombination) != len(other.colorCombination):
            return False
        return len(set(self.colorCombination).intersection(set(other.colorCombination))) == len(self.colorCombination)


    def __str__(self):
        return str(self.colorCombination)