#!/usr/bin/env python3
import dataclasses
import sys

INPUT = '4.txt'

@dataclasses.dataclass
class BoardNumber:
    number: int
    marked: bool = False

class Board:
    def __init__(self, board):
        self._board = []
        for row in board:
            self._board.append([BoardNumber(n, False) for n in row])

    def is_complete(self):
        for row in self._board:
            if all(number.marked for number in row):
                return True
        for col in range(len(self._board)):
            if all(row[col].marked for row in self._board):
                return True
        return False

    def mark(self, n):
        marked = False
        for row in self._board:
            for number in row:
                if number.number == n:
                    marked = True
                    number.marked = True
        if marked:
            return self.is_complete()
        else:
            return False

    def score(self, last_number):
        unmarked_sum = 0
        for row in self._board:
            for number in row:
                if not number.marked:
                    unmarked_sum += number.number
        return unmarked_sum * last_number

    @classmethod
    def build_board(cls, lines):
        board = []
        for line in lines:
            board.append([int(i) for i in line.strip().split()])
        return cls(board)

# part 1
#with open(INPUT) as f:
#    drawn_numbers = [int(i) for i in f.readline().strip().split(',')]
#    lines = f.readlines()
#    boards = []
#    for i in range(1, len(lines), 6):
#        boards.append(Board.build_board(lines[i:i+5]))
#
#for number in drawn_numbers:
#    for board in boards:
#        if board.mark(number):
#            print(board.score(number))
#            sys.exit(0)
with open(INPUT) as f:
    drawn_numbers = [int(i) for i in f.readline().strip().split(',')]
    lines = f.readlines()
    boards = []
    for i in range(1, len(lines), 6):
        boards.append(Board.build_board(lines[i:i+5]))

complete_boards, incomplete_boards = [], boards
for number in drawn_numbers:
    completed_boards, incomplete_boards = [], []
    for board in boards:
        if board.mark(number):
            completed_boards.append(board)
        else:
            incomplete_boards.append(board)
    if incomplete_boards:
        boards = incomplete_boards
    else:
        print(completed_boards[-1].score(number))
        sys.exit(0)
