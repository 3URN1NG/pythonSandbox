class card:

    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    suits = ['club', 'diamond', 'heart', 'spade']

    rank = None
    suit = None

    def __init__(self, rank: ranks, suit: suits) -> None:
        if (rank not in self.ranks or suit not in self.suits):
            raise Exception('given rank or suit value was not valid. Given values: {}, {}'.format(rank, suit))

        self.rank = rank
        self.suit = suit

if (__name__ == '__main__'):
    c1 = card('A','spade')