#!/usr/bin/env python3

def find_locations(elevation_map, value):
    locations = []
    for i, line in enumerate(elevation_map):
        for j, c in enumerate(line):
            if c == value:
                locations.append((i, j))
    return locations

def bfs_to_end(elevation_map, start):
    visited = set((start,))
    i = 0
    locations = [start]
    next_locations = []
    num_steps = 0
    while i < len(locations):
        x, y = locations[i]
        c = elevation_map[x][y]
        if c == 'E':
            return num_steps
        elif c == 'S':
            c = 'a'
        for x_delta, y_delta in ((1,0),(-1,0),(0,1),(0,-1),):
            new_x, new_y = x + x_delta, y + y_delta
            if 0 <= new_x < len(elevation_map) and 0 <= y + y_delta < len(elevation_map[x]):
                new_c = elevation_map[new_x][new_y]
                new_tuple = (new_x, new_y)
                if new_c == 'E':
                    new_c = 'z'
                if new_tuple not in visited and ord(new_c) <= ord(c) + 1:
                    visited.add(new_tuple)
                    next_locations.append((new_x, new_y))
        i += 1
        if i >= len(locations):
            i = 0
            locations, next_locations = next_locations, []
            num_steps += 1
    return float('inf')

def part1(elevation_map):
    start = find_locations(elevation_map, 'S')[0]
    return bfs_to_end(elevation_map, start)

def part2(elevation_map):
    starts = find_locations(elevation_map, 'a')
    starts.append(find_locations(elevation_map, 'S')[0])
    return min(bfs_to_end(elevation_map, start) for start in starts)

def main():
    for filename in ('example', 'input'):
        with open(filename) as f:
            elevation_map = f.read().splitlines()
        print(f"Answers for '{filename}':")
        print('Part 1:', part1(elevation_map))
        print('Part 2:', part2(elevation_map))

if __name__ == '__main__':
    main()
