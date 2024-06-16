#!/usr/bin/env python3

def part1():
    count = 0
    prev = None
    with open('1.txt') as f:
        for line in f:
            current = int(line)
            if prev is not None and current > prev:
                count += 1
            prev = current
    print(count)

def read_nums():
    with open('1.txt') as f:
        return [int(line) for line in f]

def part2():
    count = 0
    nums = read_nums()
    for prev, cur in zip(nums, nums[3:]):
        if cur > prev:
            count += 1
    print(count)
part2()
