#!/usr/bin/env python3

# part 1
#hos_pos, depth = 0, 0
#with open('2.txt') as f:
#    for line in f:
#        command, count = line.strip().split()
#        count = int(count)
#        if command == 'forward':
#            hos_pos += count
#        elif command == 'down':
#            depth += count
#        elif command == 'up':
#            depth -= count
#        else:
#            raise ValueError('wat')
#print(hos_pos * depth)
hos_pos, depth, aim = 0, 0, 0 
with open('2.txt') as f:
    for line in f:
        command, count = line.strip().split()
        count = int(count)
        if command == 'forward':
            hos_pos += count
            depth += (aim * count)
        elif command == 'down':
            aim += count
        elif command == 'up':
            aim -= count
        else:
            raise ValueError('wat')
print(hos_pos * depth)
