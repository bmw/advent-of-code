#!/usr/bin/env python3

fishes = []
with open('6.txt') as f:
    for line in f:
        fishes.extend(int(i) for i in line.strip().split(','))

# part 1
#for _ in range(80):
#    new_fish_count = 0
#    for i in range(len(fishes)):
#        fishes[i] -= 1
#        if fishes[i] == -1:
#            fishes[i] = 6
#            new_fish_count += 1
#    fishes += new_fish_count * [8]
#print(len(fishes))

import functools

@functools.cache
def num_fishes(age, days):
    if days <= 0:
        return 1
    elif age == 0:
        return num_fishes(6, days - 1) + num_fishes(8, days - 1)
    else:
        return num_fishes(age - 1, days - 1)

print(sum(num_fishes(i, 256) for i in fishes))
