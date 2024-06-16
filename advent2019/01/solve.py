#!/usr/bin/env python3

INPUTS_TO_EXPECTED_OUTPUTS = {
    #'example': (None, None),
    'input': (3381405, 5069241),
}

def fuel_for_mass(mass):
    return mass // 3 - 2

def fuel_per_module(puzzle_input):
    for line in puzzle_input.splitlines():
        yield fuel_for_mass(int(line))

def part1(puzzle_input):
    return sum(fuel_per_module(puzzle_input))

def fuel_for_fuel_partials(fuel):
    while fuel > 0:
        yield fuel
        fuel = fuel_for_mass(fuel)

def fuel_with_fuel_mass(fuel):
    return sum(fuel_for_fuel_partials(fuel))

def part2(puzzle_input):
    return sum(fuel_with_fuel_mass(fuel)
               for fuel in fuel_per_module(puzzle_input))

def do_part(part_num, puzzle_input, expected_answer):
    answer = eval(f'part{part_num}')(puzzle_input)
    print(f'  part {part_num}:', answer)
    if expected_answer is not None:
        assert answer == expected_answer

def main():
    for filename, expected in INPUTS_TO_EXPECTED_OUTPUTS.items():
        with open(filename) as f:
            puzzle_input = f.read()
        print(f'answers for {filename}:')
        for i in range(2):
            do_part(i + 1, puzzle_input, expected[i])

if __name__ == '__main__':
    main()
