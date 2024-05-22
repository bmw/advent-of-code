#!/usr/bin/env python3
import dataclasses
import itertools

@dataclasses.dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

def get_head_positions():
    positions = [Point(0,0)]
    with open('input') as f:
        for line in f:
            direction, count = line.strip().split()
            delta = {'U': Point(0, 1), 'D': Point(0, -1),
                     'L': Point(-1, 0), 'R': Point(1, 0)}[direction]
            for _ in range(int(count)):
                positions.append(positions[-1] + delta)
    return positions

def next_follower_position(leader_position, follower_position):
    difference = leader_position - follower_position
    move_x = move_y = False
    if abs(difference.x) + abs(difference.y) >= 3:
        move_x = move_y = True
    if move_x or abs(difference.x) >= 2:
        if difference.x > 0:
            follower_position = Point(follower_position.x + 1, follower_position.y)
        else:
            follower_position = Point(follower_position.x - 1, follower_position.y)
    if move_y or abs(difference.y) >= 2:
        if difference.y > 0:
            follower_position = Point(follower_position.x, follower_position.y + 1)
        else:
            follower_position = Point(follower_position.x, follower_position.y - 1)
    return follower_position

def next_knot_positions(prev_positions):
    positions = [Point(0,0)]
    for prev_position in prev_positions:
        new_position = next_follower_position(prev_position, positions[-1])
        if new_position != positions[-1]:
            positions.append(new_position)
    return positions

def part1(head_positions):
    return len(set(next_knot_positions(head_positions)))

def part2(prev_positions):
    for _ in range(9):
        prev_positions = next_knot_positions(prev_positions)
    return len(set(prev_positions))

def main():
    head_positions = get_head_positions()
    print('Part 1:', part1(head_positions))
    print('Part 2:', part2(head_positions))

if __name__ == '__main__':
    main()
