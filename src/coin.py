import random

class coin:
    values = ['heads', 'tails']

    def __init__(self) -> None:
        pass

    def throw(self) -> str:
        return random.choice(self.values)