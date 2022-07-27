import pandas
import abc

class playable:
    @abc.abstractmethod
    def play(self) -> int:
        return


class game:

    history = pandas.DataFrame(columns=['p0', 'p1', 'winner'])

    player0: playable
    player1: playable

    nOfRounds: int

    def __init__(self, player0: playable, player1: playable, nOfRounds = 10) -> None:
        self.nOfRounds = nOfRounds
        self.player0 = player0
        self.player1 = player1

    def playRound(self) -> tuple[int, int, int]:
        result0 = self.player0.play()
        result1 = self.player1.play()

        return result0, result1, result0-result1


    def playGame(self) -> pandas.DataFrame:
        for i in range(self.nOfRounds):
            self.history.append(self.playRound())
        return self.history
        
