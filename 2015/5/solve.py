#!/usr/bin/env python3
import os

def is_nice(s):
    naughty_strings = ('ab', 'cd', 'pq', 'xy',)
    for naughty_string in naughty_strings:
        if naughty_string in s:
            return False

    vowel_count = 0
    for vowel in 'aeiou':
        vowel_count += s.count(vowel)
    if vowel_count < 3:
        return False

    for c1, c2 in zip(s, s[1:]):
        if c1 == c2:
            return True
    return False

def part1(puzzle_input):
    nice_count = 0
    for s in puzzle_input.splitlines():
        if is_nice(s):
            nice_count += 1
    return nice_count

def is_nice2(s):
    for i in range(len(s) - 1):
        if s[i:i+2] in s[i+2:]:
            break
    else:
        return False

    for c1, c2 in zip(s, s[2:]):
        if c1 == c2:
            return True
    return False

def part2(puzzle_input):
    nice_count = 0
    for s in puzzle_input.splitlines():
        if is_nice2(s):
            nice_count += 1
    return nice_count

def main():
    for filename in ('example', 'example2', 'input'):
        if os.path.exists(filename):
            with open(filename) as f:
                puzzle_input = f.read()
            print(f"Answers for '{filename}':")
            print('Part 1:', part1(puzzle_input))
            print('Part 2:', part2(puzzle_input))

if __name__ == '__main__':
    main()
