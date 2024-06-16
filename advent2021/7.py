#!/usr/bin/env python3
import sys

with open('7.txt') as f:
    positions = [int(i) for i in f.read().strip().split(',')]

min_index = -1
min_cost = sys.maxsize
for align_position in range(min(positions), max(positions) + 1):
    # part 1
    # cost = sum(abs(current_position - align_position) for current_position in positions)
    #if cost < min_cost:
    #    min_index = align_position
    #    min_cost = cost
    cost = 0
    for current_position in positions:
        distance = abs(current_position - align_position)
        cost += int(distance * (distance + 1) / 2)
    if cost < min_cost:
        min_index = align_position
        min_cost = cost
print(min_cost)
