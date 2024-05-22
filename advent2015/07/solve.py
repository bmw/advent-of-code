#!/usr/bin/env python3
import os

# dict mapping var to input str
# read all to str
# parse and convert to int, recurse as needed to get values

def resolve_gate(state, wire):
    value = state[wire]
    if 'AND' in value:
        left, right = value.split(' AND ')
        state[wire] = resolve(state, left) & resolve(state, right)
    elif 'OR' in value:
        left, right = value.split(' OR ')
        state[wire] = resolve(state, left) | resolve(state, right)
    elif 'NOT' in value:
        # len('NOT ') = 4
        state[wire] = 65535 - resolve(state, value[4:])
    elif 'LSHIFT' in value:
        var, count = value.split(' LSHIFT ')
        count = int(count)
        state[wire] = resolve(state, var) << count
    elif 'RSHIFT' in value:
        var, count = value.split(' RSHIFT ')
        count = int(count)
        state[wire] = resolve(state, var) >> count
    else:
        state[wire] = resolve(state, value)

    return state[wire]

def resolve_wire(state, wire):
    assert wire in state, wire
    try:
        state[wire] = int(state[wire])
        return state[wire]
    except ValueError:
        pass
    return resolve_gate(state, wire)

def resolve(state, wire_or_int):
    try:
        return int(wire_or_int)
    except ValueError:
        pass
    return resolve_wire(state, wire_or_int)

def resolve_all(state):
    for wire in state:
        resolve_wire(state, wire)

def process_input(puzzle_input):
    state = {}
    for line in puzzle_input.splitlines():
        val, wire = line.strip().split(' -> ')
        assert wire not in state
        state[wire] = val
    return state

def part1(puzzle_input):
    state = process_input(puzzle_input)
    resolve_all(state)
    return state['a']

def part2(puzzle_input):
    a = part1(puzzle_input)
    state = process_input(puzzle_input)
    state['b'] = a
    resolve_all(state)
    return state['a']

def main():
    with open('input') as f:
        puzzle_input = f.read()
    print(f"Answers for input:")
    print('Part 1:', part1(puzzle_input))
    print('Part 2:', part2(puzzle_input))

if __name__ == '__main__':
    main()
