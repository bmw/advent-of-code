#!/usr/bin/env python3
import os

def next_sequence(sequence):
    new_sequence = []
    current_char = None
    current_char_count = 0
    for c in sequence:
        if c == current_char:
            current_char_count += 1
        else:
            if current_char is not None:
                new_sequence.append(str(current_char_count))
                new_sequence.append(current_char)
            current_char = c
            current_char_count = 1
    new_sequence.append(str(current_char_count))
    new_sequence.append(current_char)
    return ''.join(new_sequence)

def len_after_n_applications(puzzle_input, n):
    for _ in range(n):
        puzzle_input = next_sequence(puzzle_input)
    return len(puzzle_input)

def part1(puzzle_input):
    return len_after_n_applications(puzzle_input, 40)

def part2(puzzle_input):
    return len_after_n_applications(puzzle_input, 50)

def main():
    for puzzle_input in ('1', '1113122113'):
        print(f"Answers for '{puzzle_input}':")
        print('Part 1:', part1(puzzle_input))
        print('Part 2:', part2(puzzle_input))

if __name__ == '__main__':
    main()
