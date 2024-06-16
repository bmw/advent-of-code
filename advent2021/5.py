#!/usr/bin/env python3
import collections

INPUT = '5.txt'

Point = collections.namedtuple('Point', 'x y'.split())
Segment = collections.namedtuple('Segment', 'start end'.split())

def read_segments():
    segments = []
    with open(INPUT) as f:
        for line in f:
            point1, _, point2 = line.strip().split()
            point1 = Point(*(int(i) for i in point1.split(',')))
            point2 = Point(*(int(i) for i in point2.split(',')))
            segments.append(Segment(point1, point2))
    return segments

def build_coverage_map(segments):
    d = collections.defaultdict(lambda: collections.defaultdict(int))
    for segment in segments:
        if segment.start.x == segment.end.x:
            start, end = min(segment.start.y, segment.end.y), max(segment.start.y, segment.end.y) + 1
            for y in range(start, end):
                d[segment.start.x][y] += 1
        elif segment.start.y == segment.end.y:
            start, end = min(segment.start.x, segment.end.x), max(segment.start.x, segment.end.x) + 1
            for x in range(start, end):
                d[x][segment.start.y] += 1
        elif segment.start.x > segment.end.x:
            multiplier = 1 if segment.start.y > segment.end.y else -1
            for i in range(0, segment.start.x - segment.end.x + 1):
                d[segment.end.x + i][segment.end.y + i * multiplier] += 1
        else:
            multiplier = 1 if segment.end.y > segment.start.y else -1
            for i in range(0, segment.end.x - segment.start.x + 1):
                d[segment.start.x + i][segment.start.y + i * multiplier] += 1
                
    return d

d = build_coverage_map(read_segments())
count = 0
for row in d.values():
    for v in row.values():
        if v >= 2:
            count += 1
print(count)
