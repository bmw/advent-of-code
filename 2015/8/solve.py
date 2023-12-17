#!/usr/bin/env python3
import os

def part1(puzzle_input):
    total = 0
    for line in puzzle_input.splitlines():
        line = line.strip()
        total += len(line) - len(eval(line))
    return total

def part2(puzzle_input):
    total = 0
    for line in puzzle_input.splitlines():
        line = line.strip()
        new_str = '"' + line.replace('\\', '\\\\').replace('"', '\\"') + '"'
        total += len(new_str) - len(line)
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
