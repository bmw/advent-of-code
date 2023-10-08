#!/usr/bin/env python3
import enum
import os

Command = enum.Enum('Command', 'ON OFF TOGGLE'.split())

class Grid:
    def __init__(self):
        self.lights = []
        for _ in range(1000):
            self.lights.append([0] * 1000)

    def execute(self, command, lower_left, upper_right):
        for i in range(lower_left[0], upper_right[0] + 1):
            for j in range(lower_left[1], upper_right[1] + 1):
                if command == Command.ON:
                    self.lights[i][j] = 1
                elif command == Command.OFF:
                    self.lights[i][j] = 0
                else:
                    assert command == Command.TOGGLE
                    self.lights[i][j] ^= 1

    def execute2(self, command, lower_left, upper_right):
        for i in range(lower_left[0], upper_right[0] + 1):
            for j in range(lower_left[1], upper_right[1] + 1):
                if command == Command.ON:
                    self.lights[i][j] += 1
                elif command == Command.OFF:
                    self.lights[i][j] = max(self.lights[i][j] - 1, 0)
                else:
                    assert command == Command.TOGGLE
                    self.lights[i][j] += 2

    def num_lights_on(self):
        count = 0
        for row in self.lights:
            for light in row:
                if light:
                    count += 1
        return count

    def total_brightness(self):
        brightness = 0
        for row in self.lights:
            brightness += sum(row)
        return brightness

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
    grid = Grid()
    for line in puzzle_input.splitlines():
        grid.execute2(*parse_line(line))
    return grid.total_brightness()

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
