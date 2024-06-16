#!/usr/bin/env python3

class Octopus:
    def __init__(self, level):
        self.reset()
        self.level = level

    def increment(self):
        if self.flashed:
            raise ValueError
        self.level += 1
        if self.level > 9:
            self.level = 0
            self.flashed = True

    def reset(self):
        self.flash_handled = False
        self.flashed = False

    def __repr__(self):
        return f'{type(self)}({self.level}, {self.flashed})'

def get_valid_neighbors(i, j, i_len, j_len):
    neighbors = []
    if i > 0:
        neighbors.append((i - 1, j,))
        if j > 0:
            neighbors.append((i - 1, j - 1))
        if j < j_len - 1:
            neighbors.append((i - 1, j + 1))
    if j > 0:
        neighbors.append((i, j - 1))
        if i < i_len - 1:
            neighbors.append((i + 1, j - 1))
    if i < i_len - 1:
        neighbors.append((i + 1, j))
        if j < j_len - 1:
            neighbors.append((i + 1, j + 1))
    if j < j_len - 1:
        neighbors.append((i, j + 1))
    return neighbors

def get_octopuses():
    octopuses = []
    with open('11.txt') as f:
        for line in f:
            octopuses.append([Octopus(int(i)) for i in line.strip()])
    return octopuses

def handle_flash(octopuses, i, j):
    octopuses[i][j].flash_handled = True
    flashes = 1
    for k, l in get_valid_neighbors(i, j, len(octopuses), len(octopuses[0])):
        octopus = octopuses[k][l]
        if not octopus.flashed:
            octopus.increment()
            if octopus.flashed and not octopus.flash_handled:
                flashes += handle_flash(octopuses, k, l)
    return flashes

def print_octopuses(octopuses, step_num):
    if step_num == -1:
        print('Before any steps:')
    else:
        print(f'After step {step_num + 1}:')
    for row in octopuses:
        for o in row:
            print(o.level, end='')
        print()
    print()

def do_step(octopuses):
    flashes = 0
    for row in octopuses:
        for octopus in row:
            octopus.increment()
    for i, row in enumerate(octopuses):
        for j, octopus in enumerate(row):
            if octopus.flashed and not octopus.flash_handled:
                flashes += handle_flash(octopuses, i, j)
    for row in octopuses:
        for octopus in row:
            octopus.reset()
    return flashes

def count_flashes(octopuses, steps):
    flashes = 0
    for step in range(steps):
        flashes += do_step(octopuses)
    return flashes

def first_all_flash(octopuses):
    expected = len(octopuses) * len(octopuses[0])
    step = 1
    while do_step(octopuses) != expected:
        step += 1
    return step

def main1():
    print(count_flashes(get_octopuses(), 100))

def main2():
    print(first_all_flash(get_octopuses()))

if __name__ == '__main__':
    main2()
