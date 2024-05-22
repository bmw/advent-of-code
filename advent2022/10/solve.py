#!/usr/bin/env python3

def get_values_by_cycle(program):
    value = 1
    values = [value]
    for line in program:
        values.append(value)
        if line.startswith('addx'):
            arg = int(line.split()[1])
            values.append(value)
            value += arg
    return values

def part1(values_by_cycle):
    ans = 20 * values_by_cycle[20]
    for i in range(60, len(values_by_cycle), 40):
        ans += i * values_by_cycle[i]
    return ans

def part2(values_by_cycle):
    for i in range(1, len(values_by_cycle), 40):
        output = []
        for j in range(40):
            value = values_by_cycle[i + j]
            if value - 1 <= j <= value + 1:
                output.append('#')
            else:
                output.append('.')
        print(''.join(output))

def main():
    for filename in ('example', 'input'):
        with open(filename) as f:
            values_by_cycle = get_values_by_cycle(f.readlines())
        print(f"Answers for '{filename}':")
        print('Part 1:', part1(values_by_cycle))
        print('Part 2:')
        part2(values_by_cycle)

if __name__ == '__main__':
    main()
