from word_search import WordSearch
from solver import Solver

if __name__ == '__main__':
    t = 0
    ws = WordSearch(15)

    ws.board_gen()
    ws.print_board()

    s = Solver(*ws.get_data())
    s.solve()

