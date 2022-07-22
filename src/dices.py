import random

# Class representing a die

class dice:
    sides = []
    predefinedSides = {
        'default' : [1,2,3,4,5,6],
        'red' :     [4,4,4,4,4,9],
        'yellow' :  [3,3,3,3,8,8],
        'blue' :    [2,2,2,7,7,7],
        'magenta' : [1,1,6,6,6,6],
        'olive' :   [0,5,5,5,5,5]
    }

    def __init__(self, pSides = [1,2,3,4,5,6], predefined = 'default') -> None:
        if(self.predefinedSides.__contains__(predefined)):
            self.sides = self.predefinedSides[predefined]
        else:
            self.sides= pSides
    
    def throwMultiple(self, numberOfThrows=1) -> list:
        return random.choices(self.sides, k=numberOfThrows)
    
    def throwSingle(self) -> int:
        return random.choices(self.sides)[0]