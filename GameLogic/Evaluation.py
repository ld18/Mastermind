
class Evaluation():
    def __init__(self, rightColorWrongPlace, rightColorRightPlace):
        if not isinstance(rightColorWrongPlace, int):
            raise ValueError('rightColorWrongPlace is not a int')
        if not isinstance(rightColorRightPlace, int):
            raise ValueError('rightColorRightPlace is not a int')
        if rightColorWrongPlace < 0:
            raise ValueError('rightColorWrongPlace is not valid (' + str(rightColorWrongPlace) + ")")
        if rightColorRightPlace < 0:
            raise ValueError('rightColorRightPlace is not valid (' + str(rightColorRightPlace) + ")")
        self.rightColorWrongPlace = rightColorWrongPlace
        self.rightColorRightPlace = rightColorRightPlace


    def __eq__(self, other):
        if self.rightColorWrongPlace != other.rightColorWrongPlace or self.rightColorRightPlace != other.rightColorRightPlace:
            return False
        return True


    def __gt__(self, other):
        if self.rightColorRightPlace > other.rightColorRightPlace:
            return True
        elif self.rightColorWrongPlace > other.rightColorWrongPlace:
            return True
        return False


    def __str__(self):
        representation = "("+ str(self.rightColorWrongPlace) + "w|" + str(self.rightColorRightPlace) +"r)"
        return representation
