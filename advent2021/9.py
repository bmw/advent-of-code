#!/usr/bin/env python3

def read_points():
    points = []
    with open('9.txt') as f:
        for line in f:
            points.append([int(c) for c in line.strip()])
    return points

def risk_levels(points):
    row_len = len(points)
    col_len = len(points[0])
    for i in range(row_len):
        for j in range(col_len):
            v = points[i][j]
            adjacent = []
            if i - 1 >= 0:
                adjacent.append(points[i - 1][j])
            if j - 1 >= 0:
                adjacent.append(points[i][j - 1])
            if i + 1 < row_len:
                adjacent.append(points[i + 1][j])
            if j + 1 < col_len:
                adjacent.append(points[i][j + 1])
            if min(*adjacent) > v:
                yield v + 1

def _get_basin_points(points, i, j):
    basin_points = {(i,j)}
    v = points[i][j]
    if i - 1 >= 0:
        candidate = points[i - 1][j]
        if candidate > v and candidate < 9:
            basin_points.update(_get_basin_points(points, i - 1, j))
    if j - 1 >= 0:
        candidate = points[i][j - 1]
        if candidate > v and candidate < 9:
            basin_points.update(_get_basin_points(points, i, j - 1))
    if i + 1 < len(points):
        candidate = points[i + 1][j]
        if candidate > v and candidate < 9:
            basin_points.update(_get_basin_points(points, i + 1, j))
    if j + 1 < len(points[0]):
        candidate = points[i][j + 1]
        if candidate > v and candidate < 9:
            basin_points.update(_get_basin_points(points, i, j + 1))
    return basin_points

def get_basin_sizes(points):
    row_len = len(points)
    col_len = len(points[0])
    for i in range(row_len):
        for j in range(col_len):
            v = points[i][j]
            adjacent = []
            if i - 1 >= 0:
                adjacent.append(points[i - 1][j])
            if j - 1 >= 0:
                adjacent.append(points[i][j - 1])
            if i + 1 < row_len:
                adjacent.append(points[i + 1][j])
            if j + 1 < col_len:
                adjacent.append(points[i][j + 1])
            if min(*adjacent) > v:
                yield len(_get_basin_points(points, i, j))

def main1():
    print(sum(risk_levels(read_points())))

def main2():
    product = 1
    for i in sorted(get_basin_sizes(read_points()))[-3:]:
        product *= i
    print(product)

if __name__ == '__main__':
    main2()
