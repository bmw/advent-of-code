#!/usr/bin/env python3
import enum
import os

Command = enum.Enum('Command', 'ON OFF TOGGLE'.split())

def row_bitstring(start, inclusive_end):
    result = 0
    for i in range(start, inclusive_end + 1):
        result |= 2**i
    return result

class Grid:
    def __init__(self):
        self.grid = [0] * 1000

    def execute(self, command, lower_left, upper_right):
        bitstring = row_bitstring(lower_left[1], upper_right[1])
        if command == Command.OFF:
            bitstring = (2**1000 - 1) ^ bitstring
        for i in range(lower_left[0], upper_right[0] + 1):
            if command == Command.ON:
                self.grid[i] |= bitstring
            elif command == Command.OFF:
                self.grid[i] &= bitstring
            else:
                assert command == Command.TOGGLE
                self.grid[i] ^= bitstring

    def num_lights_on(self):
        count = 0
        for row in self.grid:
            while row:
                count += 1
                row &= (row - 1)
        return count


def parse_point_string(s):
    return tuple(int(i) for i in s.split(','))

def parse_line(line):
    if 'on' in line:
        command = Command.ON
    elif 'off' in line:
        command = Command.OFF
    else:
        assert 'toggle' in line
        command = Command.TOGGLE
    split_line = line.split()
    lower_left = parse_point_string(split_line[-3])
    upper_right = parse_point_string(split_line[-1])
    return command, lower_left, upper_right

def part1(puzzle_input):
    grid = Grid()
    for line in puzzle_input.splitlines():
        grid.execute(*parse_line(line))
    return grid.num_lights_on()

def part2(puzzle_input):
    pass

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
