import random
from game import playable

# Class representing a die

class dice(playable):
    historyArray = [None] * 10
    historyPointer = 0
    sides = []
    predefinedSides = {
        'default' : [1,2,3,4,5,6],
        'red' :     [4,4,4,4,4,9],
        'yellow' :  [3,3,3,3,8,8],
        'blue' :    [2,2,2,7,7,7],
        'magenta' : [1,1,6,6,6,6],
        'olive' :   [0,5,5,5,5,5]
    }

    def __init__(self, pSides = predefinedSides['default'], predefined = 'default') -> None:
        if(self.predefinedSides.__contains__(predefined)):
            self.sides = self.predefinedSides[predefined]
        else:
            self.sides= pSides
    
    def play(self) -> int:
        return self.roll()
    
    def rollMultiple(self, numberOfThrows=1) -> list:
        return random.choices(self.sides, k=numberOfThrows)
    
    def roll(self) -> int:
        result = random.choices(self.sides)[0]
        self.historyArray[self.historyPointer] = result
        self.historyPointer = (self.historyPointer +1) % 10
        return result

    def history(self) -> list:
        return self.historyArray[self.historyPointer:10] + self.historyArray[0:self.historyPointer]


if (__name__ == '__main__'):
    red = dice(predefined='red')
    yellow = dice(predefined='yellow')
    blue = dice(predefined='blue')
    magenta = dice(predefined='magenta')
    olive = dice(predefined='olive')

    red.roll()
    red.roll()
    red.roll()
    print(red.history())