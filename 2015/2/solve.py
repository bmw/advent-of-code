#!/usr/bin/env python3
import collections
import math
import os

Dimensions = collections.namedtuple('Dimensions', 'length width height')

def get_dimensions(input_line):
    return Dimensions(*(int(i) for i in input_line.strip().split('x')))

def needed_paper(dimensions):
    sides = [
        dimensions.length * dimensions.width,
        dimensions.width * dimensions.height,
        dimensions.length * dimensions.height
    ]
    return min(sides) + sum(2 * side for side in sides)

def part1(puzzle_input):
    total = 0
    for line in puzzle_input.splitlines():
        total += needed_paper(get_dimensions(line))
    return total

def needed_ribbon(dimensions):
    sorted_dimensions = sorted(dimensions)
    return 2 * sum(sorted_dimensions[:2]) + math.prod(dimensions)

def part2(puzzle_input):
    total = 0
    for line in puzzle_input.splitlines():
        total += needed_ribbon(get_dimensions(line))
    return total

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
