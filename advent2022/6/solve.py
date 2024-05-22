#!/usr/bin/env python3

def first_marker(problem_input, num_unique):
    for i in range(num_unique, len(problem_input) + 1):
        if len(set(problem_input[i - num_unique:i])) == num_unique:
            return i
    assert False, 'No marker found'

def part1(problem_input):
    return first_marker(problem_input, 4)

def part2(problem_input):
    return first_marker(problem_input, 14)

def main():
    with open('input') as f:
        problem_input = f.read()
    print('Part 1:', part1(problem_input))
    print('Part 2:', part2(problem_input))

if __name__ == '__main__':
    main() 
