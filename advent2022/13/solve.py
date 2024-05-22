#!/usr/bin/env python3
import functools
import os

def list_pairs(puzzle_input):
    lines = puzzle_input.splitlines()
    for i in range(0, len(lines), 3):
        l1 = eval(lines[i].rstrip())
        l2 = eval(lines[i + 1].rstrip())
        yield l1, l2

def compare(l1, l2):
    i = 0
    while i < min(len(l1), len(l2)):
        v1, v2 = l1[i], l2[i]
        if isinstance(v1, int) and isinstance(v2, int):
            if v1 - v2 != 0:
                return v1 - v2
        else:
            if isinstance(v1, int):
                v1 = [v1]
            elif isinstance(v2, int):
                v2 = [v2]
            result = compare(v1, v2)
            if result != 0:
                return result
        i += 1
    return len(l1) - len(l2)

def part1(puzzle_input):
    ans = 0
    for i, (l1, l2) in enumerate(list_pairs(puzzle_input), 1):
        if compare(l1, l2) < 0:
            ans += i
    return ans

def part2(puzzle_input):
    divider1 = [[2]]
    divider2 = [[6]]
    lists = [divider1, divider2]
    for l1, l2 in list_pairs(puzzle_input):
        lists.append(l1)
        lists.append(l2)
    lists.sort(key=functools.cmp_to_key(compare))
    return (lists.index(divider1) + 1) * (lists.index(divider2) + 1)

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
