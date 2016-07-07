from random import randrange

class Shuffler(object):
    def __init__(self, blocks, blockSize, groups):
        self.blocks = blocks
        self._groups = groups
        self._blockSize = blockSize
        self.deck = self.make_deck()

    @property
    def blockSize(self):
        return self._blockSize

    # BlockSize setter also initializes deck
    @blockSize.setter
    def blockSize(self, value):
        self._blockSize = value
        self.deck = self.make_deck()

    @property
    def groups(self):
        return self._groups

    # Groups setter also initializes deck
    @groups.setter
    def groups(self, value):
        self._groups = value
        self.deck = self.make_deck()

    def is_valid_group_size(self):
        return self.blockSize % self.groups == 0

    # Fisher-Yates shuffle, Durstenfeld in-place implementation
    def shuffle(self):
        items = self.deck[:]    # copy deck for in-place shuffle
        n = len(items)
        while n > 1:
            k = randrange(n)  # 0..n-1
            n = n - 1
            items[k], items[n] = items[n], items[k]
        return items

    def make_deck(self):
        result = []
        for i in range(self.blockSize):
            result.append(i % self.groups + 1)
        return result
