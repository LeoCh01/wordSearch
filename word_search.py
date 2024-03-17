import random
import string


def parser(t):
    with open(t) as f:
        lst = f.read().split('\n')
    return lst


class WordSearch:
    all_words = parser('words.txt')
    longest_word = len(max(all_words, key=len))

    def __init__(self, k):
        self.words = random.sample(WordSearch.all_words, k)
        self.words.sort(reverse=True, key=len)
        self.n = max(int(len(''.join(self.words)) ** 0.5 * 1.5), len(max(self.words, key=len)) + 2)
        self.board = []
        self.board_hidden = []

    def board_gen(self):
        self.clear_board()
        # direction = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
        direction = [(1, 1), (1, 0), (0, 1), (-1, 1)]

        for w in self.words:
            l = len(w)
            while True:
                x, y, d = random.randint(0, self.n - 1), random.randint(0, self.n - 1), random.choice(direction)

                if 0 <= x + d[0] * l < self.n - 1 and 0 <= y + d[1] * l < self.n - 1:
                    pts = list(zip([x + d[0] * i for i in range(l)], [y + d[1] * j for j in range(l)], w))
                    if all(self.board[i][j] == '0' or self.board_hidden[i][j] == c for i, j, c in pts):
                        col = random.randint(91, 97)
                        for i, j, c in pts:
                            self.board[i][j] = f'\033[{col}m{c}\033[0m'
                            self.board_hidden[i][j] = c
                        break

        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == '0':
                    c = random.choice(string.ascii_lowercase)
                    self.board[i][j] = f'\033[90m{c}\033[0m'
                    self.board_hidden[i][j] = c

    def print_board(self, show=False):
        print('word count: ', len(self.words))
        print('char count: ', len(''.join(self.words)))
        print('board size: ', f'{self.n ** 2} ({self.n} x {self.n})', '\n')
        for i, w in enumerate(self.words, 1):
            print('{:20s}'.format(w), end='')
            if i % 4 == 0:
                print()
        print()
        board = self.board if show else self.board_hidden
        for row in board:
            print('  '.join(f'\033[90m{c}\033[0m' for c in row))
        print()

    def clear_board(self):
        self.board = [['0'] * self.n for _ in range(self.n)]
        self.board_hidden = [['0'] * self.n for _ in range(self.n)]

    def get_data(self):
        return self.board_hidden, self.words
