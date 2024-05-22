#!/usr/bin/env python3
import collections
import itertools
import os

def parse_city_distances(puzzle_input):
    distances = collections.defaultdict(dict)
    for line in puzzle_input.splitlines():
        city1, _, city2, _, distance = line.split()
        distance = int(distance)
        distances[city1][city2] = distance
        distances[city2][city1] = distance
    return distances

def all_route_lengths(puzzle_input):
    city_distances = parse_city_distances(puzzle_input)
    route_lengths = []
    for permutation in itertools.permutations(city_distances.keys()):
        current_route = 0
        for city1, city2 in zip(permutation, permutation[1:]):
            current_route += city_distances[city1][city2]
        route_lengths.append(current_route)
    return route_lengths

def part1(puzzle_input):
    return min(all_route_lengths(puzzle_input))

def part2(puzzle_input):
    return max(all_route_lengths(puzzle_input))

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
