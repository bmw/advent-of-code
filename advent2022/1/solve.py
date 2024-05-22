#!/usr/bin/env python3

def read_elves():
    current = 0
    with open('input') as f:
        for line in f:
            line = line.strip()
            if line:
                current += int(line)
            else:
                yield current
                current = 0
    yield current

def part1():
    print(max(read_elves()))


def part2():
    print(sum(sorted(read_elves(), reverse=True)[:3]))
