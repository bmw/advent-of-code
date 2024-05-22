#!/usr/bin/env python3
import os

def next_location(x, y, instruction):
    if instruction == '^':
        return x, y + 1
    elif instruction == 'v':
        return x, y - 1
    elif instruction == '<':
        return x - 1, y
    else:
        assert instruction == '>', instruction
        return x + 1, y

def part1(puzzle_input):
    location = (0,0)
    visited = set((location,))
    for instruction in puzzle_input.strip():
        location = next_location(*location, instruction)
        visited.add(location)
    return len(visited)

def part2(puzzle_input):
    santa_location = (0,0)
    robo_location = (0,0)
    visited = set((santa_location,))
    for i, instruction in enumerate(puzzle_input.strip()):
        if i % 2 == 0:
            santa_location = next_location(*santa_location, instruction)
            visited.add(santa_location)
        else:
            robo_location = next_location(*robo_location, instruction)
            visited.add(robo_location)
    return len(visited)

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
