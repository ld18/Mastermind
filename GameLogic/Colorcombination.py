
from termcolor import colored

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


    def hasAnyOfThisColor(self, colorList):
        tmpColorCombination = Colorcombination(colorList)
        return self.hasAnyColorInCommon(tmpColorCombination)


    def hasAllColorsInCommon(self, other):
        if len(self.colorCombination) != len(other.colorCombination):
            return False
        return len(set(self.colorCombination).intersection(set(other.colorCombination))) == len(self.colorCombination)


    def __str__(self):
        colorsOfColors = ["green", "yellow", "blue", "magenta", "cyan", "grey", "red", "white"]
        representation = "["
        for color in self.colorCombination:
            try:
                representation += colored(str(color), colorsOfColors[color])
            except:
                representation += str(color)
            representation += ", "
        representation = representation[:-2]
        representation += "]"
        return representation