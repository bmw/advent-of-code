#!/usr/bin/env python3
import hashlib
import os

def part1(puzzle_input):
    i = 1
    while True:
        key = puzzle_input + str(i)
        digest = hashlib.md5(key.encode()).hexdigest()
        if digest.startswith('00000'):
            return i
        i += 1

def part2(puzzle_input):
    i = 1
    while True:
        key = puzzle_input + str(i)
        digest = hashlib.md5(key.encode()).hexdigest()
        if digest.startswith('000000'):
            return i
        i += 1

def main():
    puzzle_input = 'iwrupvqb'
    print('Part 1:', part1(puzzle_input))
    print('Part 2:', part2(puzzle_input))

if __name__ == '__main__':
    main()
