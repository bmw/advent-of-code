#!/usr/bin/env python3

def player1_won(move1, move2):
    # Trust me
    return (move1 + 2) % 3 == move2

def part1():
    score = 0
    with open('input') as f:
        for line in f:
            opponent, self = line.strip().split()
            # Covert ABC or XYZ into 012 for rock, paper, scissors
            opponent = ord(opponent) - ord('A')
            self = ord(self) - ord('X')
            score += self + 1
            if player1_won(self, opponent):
                score += 6
            elif not player1_won(opponent, self):
                score += 3
    print(score)

def part2():
    score = 0
    with open('input') as f:
        for line in f:
            opponent, self = line.strip().split()
            # Covert ABC or XYZ into 012 for rock, paper, scissors
            opponent = ord(opponent) - ord('A')
            if self == 'X':
                score += (opponent + 2) % 3
            elif self == 'Y':
                score += opponent
                score += 3
            else:
                score += (opponent + 1) % 3
                score += 6
            # Scores are off by 1 due to 0 based indexing
            score += 1
    print(score)
part2()
