#!/usr/bin/env python3
import collections

def is_visible(heights, i, j):
    current_height = heights[i][j]
    return (all(heights[k][j] < current_height for k in range(i)) or
            all(heights[k][j] < current_height for k in range(i + 1, len(heights))) or
            all(heights[i][k] < current_height for k in range(j)) or
            all(heights[i][k] < current_height for k in range(j + 1, len(heights[i]))))

def part1(heights):
    return sum(1 for i, row in enumerate(heights)
                 for j in range(len(row))
                 if is_visible(heights, i, j))

def visible_trees(heights, i, j, i_step, j_step):
    current_height = heights[i][j]
    i += i_step
    j += j_step
    count = 0
    while 0 <= i < len(heights) and 0 <= j < len(heights[i]):
        count += 1
        if heights[i][j] >= current_height:
            break
        i += i_step
        j += j_step
    return count

def scenic_score(heights, i, j):
    score = 1
    for i_step, j_step in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        score *= visible_trees(heights, i, j, i_step, j_step)
    return score

def part2(heights):
    return max(scenic_score(heights, i, j)
               for i, row in enumerate(heights)
               for j in range(len(row)))

def main():
    with open('input') as f:
        problem_input = f.read()
    heights = [[int(c) for c in line] for line in problem_input.splitlines()]
    print('Part 1:', part1(heights))
    print('Part 2:', part2(heights))

if __name__ == '__main__':
    main()
