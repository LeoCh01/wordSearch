import collections
import random


def trie():
    return collections.defaultdict(trie)


class Solver:

    def __init__(self, board, words):
        self.board = board
        self.n = len(board)
        self.words = words
        self.root = trie()
        self.res = {}

    def solve(self):
        self.fill_trie()

        for i in range(self.n):
            for j in range(self.n):
                for d in [(1, 1), (1, 0), (0, 1), (-1, 1)]:
                    self.search_trie(i, j, d)

        for i in range(self.n):
            for j in range(self.n):
                c = self.board[i][j]
                print(self.res[(i, j)] if (i, j) in self.res else f'\033[90m{c}\033[0m', end='  ')
            print()
        print()

    def search_trie(self, x, y, d):
        n = self.root
        col = random.randint(91, 97)
        cur = {}

        while n and 0 <= x < self.n and 0 <= y < self.n:
            if self.board[x][y] in n:
                cur[(x, y)] = f'\033[{col}m{self.board[x][y]}\033[0m'
                n = n[self.board[x][y]]
                x += d[0]
                y += d[1]
                if '#' in n:
                    self.res.update(cur)
            else:
                return

    def fill_trie(self):
        for w in self.words:
            n = self.root
            for c in w:
                n = n[c]
            n = n['#']
