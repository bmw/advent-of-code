#!/usr/bin/env python3
import itertools
import os

def get_rock_paths(puzzle_input):
    paths = []
    for line in puzzle_input.splitlines():
        paths.append([])
        for point in line.split(' -> '):
            paths[-1].append(tuple(int(i) for i in point.split(',')))
    return paths

def get_extrema(rock_paths):
    xs = sorted(point[0] for path in rock_paths for point in path)
    max_y = max(point[1] for path in rock_paths for point in path)
    return ((xs[0], xs[-1]), (0, max_y))

def build_rock_map(rock_paths, extrema):
    grid = [[False] * (extrema[0][1] + extrema[0][0] + 1) for _ in range(extrema[1][1] + 1)]
    for path in rock_paths:
        for start, end in itertools.pairwise(path):
            start = (start[0], start[1])
            end = (end[0], end[1])
            if start[0] == end[0]:
                if end[1] < start[1]:
                    start, end = end, start
                x = start[0]
                for y in range(start[1], end[1] + 1):
                    grid[y][x] = True
            else:
                assert start[1] == end[1]
                if end[0] < start[0]:
                    start, end = end, start
                y = start[1]
                for x in range(start[0], end[0] + 1):
                    grid[y][x] = True
    return grid

class Cave:
    def __init__(self, rock_map):
        self._rock_map = rock_map

    @classmethod
    def from_input(cls, puzzle_input):
        rock_paths = get_rock_paths(puzzle_input)
        extrema = get_extrema(rock_paths)
        rock_map = build_rock_map(rock_paths, extrema)
        return cls(rock_map)

    def simulate_sand(self):
        x, y = 500, 0
        while y < len(self._rock_map) - 1:
            y += 1
            if self._rock_map[y][x]:
                if x != 0 and not self._rock_map[y][x - 1]:
                    x -= 1
                elif x < len(self._rock_map[0]) - 1 and not self._rock_map[y][x + 1]:
                    x += 1
                else:
                    self._rock_map[y - 1][x] = True
                    return x, y - 1
        return x, float('inf')

    def add_floor(self):
        self._rock_map.append([False] * len(self._rock_map[0]))
        self._rock_map.append([True] * len(self._rock_map[0]))

def part1(puzzle_input):
    cave = Cave.from_input(puzzle_input)
    calls = 0
    while cave.simulate_sand()[1] != float('inf'):
        calls += 1
    return calls

def part2(puzzle_input):
    cave = Cave.from_input(puzzle_input)
    cave.add_floor()
    calls = 1
    while cave.simulate_sand() != (500, 0):
        calls += 1
    return calls

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
