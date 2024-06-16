#!/usr/bin/env python3
# part 1
#pos_counts = []
#with open('3.txt') as f:
#    for line in f:
#        line = line.strip()
#        if not pos_counts:
#            for _ in line:
#                pos_counts.append({'num_zeros': 0, 'num_ones': 0})
#        for c, d in zip(line, pos_counts):
#            if c == '0':
#                d['num_zeros'] += 1
#            else:
#                d['num_ones'] += 1
#epsilon, gamma = [], []
#for pos in pos_counts:
#    if pos['num_zeros'] > pos['num_ones']:
#        epsilon.append('1')
#        gamma.append('0')
#    else:
#        epsilon.append('0')
#        gamma.append('1')
#epsilon = int(''.join(epsilon), 2)
#gamma = int(''.join(gamma), 2)
#print(epsilon * gamma)

def read_nums():
    with open('3.txt') as f:
        return [line.strip() for line in f]

def get_pos_counts(nums, pos):
    num_zeros, num_ones = 0, 0
    for num in nums:
        if num[pos] == '0':
            num_zeros += 1
        else:
            num_ones += 1
    return num_zeros, num_ones

def filter_by_pos(nums, character, position):
    return [num for num in nums if num[position] == character]

def get_c02_num():
    nums = read_nums()
    for i in range(len(nums)):
        num_zeros, num_ones = get_pos_counts(nums, i)
        c = '0' if num_zeros <= num_ones else '1'
        nums = filter_by_pos(nums, c, i)
        if len(nums) == 1:
            return int(''.join(nums[0]), 2)

def get_oxygen_num():
    nums = read_nums()
    for i in range(len(nums)):
        num_zeros, num_ones = get_pos_counts(nums, i)
        c = '0' if num_zeros > num_ones else '1'
        nums = filter_by_pos(nums, c, i)
        if len(nums) == 1:
            return int(''.join(nums[0]), 2)

print(get_c02_num() * get_oxygen_num())
