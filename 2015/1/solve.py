#!/usr/bin/env python3
import os

def part1(puzzle_input):
    return puzzle_input.count('(') - puzzle_input.count(')')

def part2(puzzle_input):
    floor = 0
    for i, c in enumerate(puzzle_input, 1):
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
        else:
            assert False, f'Unexpected character {c} at index {i}'

        if floor == -1:
            return i

def main():
    for filename in ('example', 'input'):
        if os.path.exists(filename):
            with open(filename) as f:
                puzzle_input = f.read()
            print(f"Answers for '{filename}':")
            print('Part 1:', part1(puzzle_input))
            print('Part 2:', part2(puzzle_input))

if __name__ == '__main__':
    main()
