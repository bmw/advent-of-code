#!/usr/bin/env python3
import math


EXAMPLE_PASSES = """BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL
"""

REAL_PASSES = """FBFFBFFRLL
BFFBFBBLRR
FFFBFBFLLR
BBFFFBBRRR
FBFFFFBLLR
BFFFFBFRLL
FBBFFBBRRL
BFBBBBFLLR
BBBFFFBLLL
BBFFFBBLRL
FFFBFFFLRL
FFBFBBBLRL
FFFBBBBLRL
BFFBBBFRLR
FBFFBFBLLR
BBBFBBFLRL
BFFBBFBLLR
FBBFBFFRRL
FBFFBBFLLL
BFBFFBBRLL
FBBFFBFRLR
BFFFFFBLLL
FBFBFBFRLL
BFBBFFBLLR
BBBBFBBLLL
BFFFBBFLLL
FFBBFBFRLL
FFBFFBBLRR
BFFBFFFRRL
FBFBBFBRLR
BBFBFBBRLR
FBBBBFFLRL
BFBBFFBRRR
BFBFFBFLLL
FFBBBFFRLR
FBFBFBBRRR
BBBFFBBLLR
BBFBBBBLRR
BBFFFFBRLL
BFBBBBFLRR
BBBFBBFRRR
BFFFFFBRRL
BBFBBFBRRL
BFFFBBFRRR
BFFBFBFLRL
FFBFFFBRLL
FFBBBFFLRL
FBFFFBFLRL
FFFBFFFLRR
FBFBBFBRRR
BFBFBFFRRR
BBFBBBBLRL
FBFFFFBRLR
FFBBBBFLRL
BBBFFFFRRL
BFBFFBFRRR
FFBBBFFLRR
FFFBFBBRRL
BFBBBBBLRL
BFFFFBFRLR
BBBFFBFRLL
FFFBBBBLLL
FFBFBFFLRR
BFFBFFFLLL
BFFBFBFLLL
BFFBBBFLLR
FBBFBFBRRR
FFFFBBBLLR
FFFBFBBRLR
FBBFBFFLRR
FFFBBBFRRR
FFFBBBFLRL
BFBFBBBRLR
BBFFBFBRLR
FFBFBFFRRL
BBFFFBFRLL
BFFFBBBRLR
FFFBBFFRLL
FBFFFFBLRL
BFFBFBBLLL
BFBBFFFLLL
BFBFBBFRLR
BFBFFFFRRR
FFFFBBFRLL
BFFFBFFRRR
FFBFFFFRRR
BBBFFFFRLL
FBFBBBBRLL
BBBFBBFLLR
FFBFFFFRLL
BBBFBBBRLR
BFFBFFFLRR
FBFBFBBRLL
FBBFBBFRLR
FFBBFFBLRL
BFBFBBBRRL
FBBBBBBLRL
FBFFFBBLRR
BBFBBFBRLR
FBFBBBFRLL
FBBFFFBLLR
BFFFFBFLRR
FBFFBBFRLR
BFFFBFFRLR
FFFBBFFLRR
FFBBFBBRRL
FBFBFFFLRL
FBBBBFBLLR
FBBFBBBRRR
FFFFBBFLRR
FBBFFFBRRL
FBBFBBBLRL
BBBFBFBRRL
FBFBFFFLLL
FFFBFBFLRL
BBFFFBBRLR
BBBFFBFLRR
BFBBBBFLRL
FBFBBBFLLR
FBBFFFFRRL
BFBBBBBRLR
BBFFBBBRLR
BBBBFFFRLL
BBFFFFBRRR
FFBFBBFRLL
BFFFBBFRLL
FFBBBFBLLL
BFBFBFFLRL
BFFFBBFLRR
BFFFBBBRRL
BFFFFFFLLL
FFBFFBFRLR
BFFBBFFLLL
BBFBFBBLLR
FBFBFBBRLR
FFBFBBBRLL
FFBFBBBLLR
BBBFFFBRRR
BBFFBBBRRL
BBFFBBBRLL
FFBBFBBLLL
FBBBFBBLLR
BFBFBFBRLR
FBFFBFBRRL
FBBBBBFRRR
BBFFBBFLRL
BBBBFFBRLL
FFBFFFFLLL
BFFFFBFLLL
FFBFFBBLRL
FBBBBBFLLR
BFBFBBBLLR
BBBFBFFRRR
BFBFFBBRLR
BFFFFFBLLR
BFBFBFBRRL
FFBFFBBRRL
FBBFBFBRLR
BBFFBBFLRR
FBBFFBFLLL
FFFFBFBRRL
BFBBBFFLRL
FFBBFBFLRR
BBBFFFFRLR
FBBBBBFLRR
BBFFBFBLRL
BFBBFFFLLR
BBFFFFBLRR
BFFFFBBLLR
FBBFFBBRLR
FBBBFFBRLR
BBBBFFFRRL
BFFBBBFLRL
FBBBFFBLRR
BFBFBFBLRR
FBBFFBFLLR
BFBFFBFRLR
FBFBFFFRRR
BFFFBFFLLL
FFBBBFFLLR
BBBFFFFLRR
FBBFFFBRRR
FFBFBBBRRL
FFBBBFBLRR
BFFFFFBRLR
FFFBFBBLRL
BFBFFFBRLR
FFBFFBBRLR
BBFBFBBRLL
BBFFBFBRRR
BFFFFFBRRR
FFFBFFBLLL
FFBBFBFLLR
BFFBBBBLLL
BBFFBFBRRL
FFBBFFFLRR
BFFFFFFRRL
FFBFFFBRRR
FFBBBFBLLR
FFBFFFFLRR
BFFFBFBLRL
BFBBFBBLRL
BFFFFFFRLL
BBFBFBFLRL
BBFBFBFLLR
FFBFFBFRLL
FFFFBBBRRL
BFFFBFFRRL
BFFBBFBRLL
FBFFBBBRLR
FFBBFBFRRR
BFFBBBBLRR
BFFBFFBLLL
BBBBFBFLRL
FBBFBBFRRR
FBBFBFBRLL
BBBFBBFLLL
BFFBFFBRLR
FFBBFFBLLL
BFFBBFFRRR
BBFBBFFLLL
BBBBFBFRLR
FFBBFFFLLR
BFFBFBFLRR
FBFFFFBLRR
FBBBFFFLRR
BFBBFBFLLR
BBFFBFFLLR
FFFBFBFLLL
FFBFBBBLLL
FBBFFBBLRR
BFFFBBBRLL
BBFBBFFRLR
FBFBFBFLRR
BBBFBFFRLL
FBFBBBFLRR
BBBBFFBRRL
BBBBFBFLRR
FFBFFBFLRR
BFFBFFBRRL
FFFBFBFRLR
FBBBBFBLRL
FFFBFBBRRR
FFBFFBFRRL
BFFFFBBRRL
BBBFBBBLRL
FBBFFBBLLR
BBFFFFBLLR
FBFFBBFLRL
FFBBFFBRLR
BFBBBFBRRL
BFBFFBFLLR
BBFBBBFRRR
FBFFFBFLLR
FFBBBBBRLR
BFBBBFBLRR
BFBFBFBLLL
FFBFBBFLLR
FFFFBBFRLR
BBFFBBFRRR
FFBBBFFRRL
FFBBFBFLLL
FFFBFBBRLL
BBFBFFBLRR
FFBBFFBLLR
BBFFFBBRLL
FFBFFFBLRL
BBFBFFFRLR
BBFBBFFRRR
FFBBFBFLRL
FFBFFFFLLR
FFFFBBFRRL
BBFFFFFLRR
FBBFFFBRLR
BFBFFFFLLL
BBBBFFFLLL
BBFBFFFRLL
FFFBFFFRRL
BBBBFBBRRR
FFBBBFFLLL
BBBFFFBRLL
FFBFFBBRLL
BFBBFFFLRL
BBFBFFBLLR
BFBFFBFLRR
BFBFBBFRRR
FBFFFBBRLL
BFBBFFBLRR
BBBFBBBRLL
BFFBFFFRRR
BFFFBFBLLR
FFBFBFBRLL
FBFBBBBLRR
FFBFBFBLLL
FBFFFBFLRR
FBFBBBFLLL
FBFFFBFRRL
BBFBBFBLRL
FBBBFFFRLR
FBBBBFFRRL
FFBFBBBLRR
FBBFBBBLRR
BFFFBBBLRR
BFBFBBBLRR
FFFBBFFLLL
BFBBBBBRLL
BBFBFFBRLL
BBFBBBBRLL
BFFBFBFRRL
BFBFBBFLRL
FBBBFBBLLL
FBBBBBFRLL
FFBBFBBLRR
BFBBBBFRRR
BFBFBBFLLR
BFBBFBFRRR
FBBBFBBRLL
FFFBBFFRRR
FBFBBFBRRL
BFBBBFBLRL
FFFBBBBLLR
FBBFBBFLLL
BFFFBFFLRR
FFBFFBFLLL
BFFFFFFRRR
BBFBBBFRRL
FFFFBBFLLL
BBBBFFFLLR
FBFFBBBRRL
BBFBBFBLLL
BBFBBBBRRR
BFFFBFBRRR
BFFBFBFLLR
FFFBFFBRRR
BBFFFBFLRL
FBFFBBBLRR
FFBBFFBRRR
BBFBFFBRLR
BBBFBFFLLR
FBBBBBBRRL
BFFBBFFRRL
FFFBFFBLLR
FFFBBBFLLR
BBBFBFBRLR
FBFFBBFLLR
BFBBFBFLRL
BFBFBFBRRR
BBBFFBBRLL
BBBFBBBLLL
FFBBBBBRRR
BBBFFFFLLL
FBFBFFBRLL
BBFFBBFLLL
BFFFBFBRLL
BBFFBFFRRR
FBFBBBFRRL
BFBBFFFRLL
BBFFBBBLLL
BBFFFBBLLR
FBBBBBFLRL
FFFFBBBLRR
FBBFFBFLRR
FBBBFBFRLL
BFBBBBBLLL
BFBFFBBLLR
BFBBFBBRRR
BBFFFBFRRR
FBBFFFBLLL
BBFBFBFRRL
BFFFFBBRLR
BBBFFBBLRL
BBBBFBBRLL
FFBFBFBLLR
FBFFFFFRRL
FBBBFBBRRR
BBFBFBBLRL
BFFBFFBRLL
BFBBBFFLLR
FFBFBFFLLL
BBFFFFBLRL
BFBFFBBLRR
FBBFFFFRRR
BFFBFFBLRR
FBBFBBBRLL
BFBBBBFLLL
FBFFFBFRLL
BFBBFBBRLL
BFBBBFBLLR
BFFBFBBLLR
FBFBFBBLLL
FFBFFFFRRL
FBBBFFBLLR
BBFBBBBLLR
BFFFFBFRRR
FBFFBFBRLL
BFFBFFFRLL
FBBBBFFLLL
BBBFFBBLRR
FBFBFFBRLR
BBBFFFFLRL
BFFBBFBLRL
FBFBFFFRLR
FFFFBBBRLL
FFFFBBBLRL
FBBFBFBLLL
BFBBBBBLLR
FBFFFBBLRL
BFBFFBFLRL
BFFFFFFLRL
BFFBBBFLRR
BBBFBBBRRR
FBBBBBBLRR
BFFBFBFRLR
BFFBBFFLRR
FBFFFFFLRR
FBFFBFBLRL
FBFBBBBRRL
FFFBBBBRRL
BFFFBFFLRL
BFFBFFBLRL
BBBBFBFRLL
FBBBFBFRLR
BFBFBFFRRL
BBBFFBBLLL
FFBBBBBLLR
FBFBFFBLRL
BFFBBBBRLR
BFFBFBFRRR
FFBFFFFLRL
BBBFBFFRRL
FFBBBBBRRL
BBFBFBFRLR
FBBBBBBRLL
BBBBFBBLLR
FBFBFBFRLR
FFFBFFFLLL
BFBFFFBLRR
FBFFFFBLLL
BFBFFFFRLR
FBBBBBFLLL
BBBBFFBLRL
BFFBFFFRLR
FBFBBFFRRR
BFFBBFFLRL
FBBFBBBLLL
FBFFBFFLLR
BFFBFFBLLR
FFBBFFFRRR
BBBFBFBLRR
BFFBBBBRRR
FFFBBFFLRL
FBBBFBBLRR
BBFBBBFRLR
BBFFFFFRRL
FBFBFBFLRL
BBBBFFFLRR
FFBFFFBLLL
FFFFBBBLLL
FFBBBBBLRR
FBBBFFBLRL
FFBFFBFLLR
FBBBBFFLLR
BFBFFBBLRL
FFBFFBBRRR
BBFFBBFRRL
FFBBBFBRLR
BBBFBBFRLR
FBBFBFBLLR
FBBBFFFRRL
FBFBFFBLLR
BFBBFBBLLL
FBBFFFFRLR
BBFBBBFLRR
FBFFBFBLRR
FBFBFFBRRR
FBFFBFBLLL
BBBFFBFRRL
BBBFFBBRLR
BBFFBFFRLL
FFBFFFBRLR
BFBBFBFLRR
FBBBBFBRRL
FFBFBFFRRR
BFFFFFFLRR
FBBBBFFLRR
FFBBFFBLRR
BBBFFFFLLR
FFFBFFFRLR
FFFBFBFRRL
BFBBBBFRLL
BFBFBBFLLL
FFFBFFBLRL
BFBBFBFRLL
FBFBBFFRRL
BFFFBFBRRL
FFBBBBFLRR
FBFFBFFLRR
FBBBBBBRLR
FBBBFFFRRR
FBBBFFBRLL
BFBBFFBLRL
BFBBBBBLRR
BBFBBBBRLR
BBFFFFBRRL
FFFBBBFLLL
BFFFBBBLRL
FFFFBBFLLR
BBFFFBFRRL
BFFFBFBLRR
BFFFBBBRRR
FBFBBFBLLL
BFBBFFFLRR
FBBBFFFLLL
BFBFFFFLLR
FBFBBFFLRR
BBBFBFBLLL
BBFBFFBLLL
BFBFBFBLRL
BFFBBBFLLL
BFFFFBBRRR
FFBBBBFLLR
FBBBFFBLLL
BFFBBBFRRR
FBFBFFFLLR
FFFBBFBRRL
BBFBFBBLLL
BBBFBFBLLR
FBFFFFBRRR
FBFFFBBLLL
BFFFFBBLRR
BFFBBFBLRR
BFBFFFBRRR
FFFBBFFRRL
FFBBFFFLLL
FFBBBBBLRL
FBBBBBFRRL
FBFFFBFLLL
BBFBBFBLLR
BFBBFBBRRL
BFBBFFBRLL
BBFBBFFRLL
BFFBFBBRRL
FFFBFBBLLR
FFFBBFBLLR
FBFFFFFRLR
FBBBBFFRLR
FBFFBBFRRL
FBFFBBBRLL
BFFBBFBRRL
BFFFFBBLLL
FFBBBFBRRR
BBBFBBBRRL
BBBFFBFLLL
FFFBBBBRLL
BBFBFBFLLL
BBFBFBBRRL
FFBBBBBLLL
FBFFBBFRLL
BBFFBFFRRL
BFBBBFBRLR
FBFFBBBLRL
FFFBFBFRLL
BFBFFFBLLL
FBBBBBBRRR
FBFBBBBRRR
FBBBFBBRLR
BFFFFBBRLL
BBFBFFFRRL
BFBBBFFLRR
FBBBFBFRRL
FBBFFBFLRL
BFBBFFFRRR
BFBBFBFLLL
FBBBBFBRRR
FBBFFBFRLL
FBFFFFFLLR
BBBFBBFLRR
BBFFFBFLLR
BBFFFBFLLL
FBFBBBFLRL
FFBFFFBRRL
BBFBFBFRRR
FBFFBBFRRR
BBBFFBBRRR
BFFFBBFLLR
FFBBFBBLRL
FBFBFBFLLR
FBFBFFFLRR
FFBBBBFLLL
FBFBFFBLRR
BBFFBBFRLR
FBBBFFFLLR
FBFBFFFRRL
BFFBBBBRRL
FBBFFBBLLL
BBFBBFBRLL
FBBBFBBLRL
BFFFFFFLLR
FBBFBFFLRL
FBFFBBBRRR
FFBBBFFRLL
BFFBFBBLRL
FBFBFFBRRL
FFFFBBBRLR
BBBFBFFLLL
FFFBBFBLRR
BFFBFBFRLL
FBFBBFFLRL
BBFFBBFLLR
FBFBFBBLLR
BBFFFBFLRR
BFFFBFBLLL
FBFBFBFRRR
FBBFFBFRRR
FFFBFFFRLL
FFBBFBBRLR
FFFBFFBRRL
BBBFBFBLRL
FBBFBFFRRR
BBBFFFBRRL
FBBFBFFLLR
FBFFFBBRRR
BBBFBBFRRL
BFFBBFFRLL
FFFBBBBLRR
BBBBFFFLRL
FFBBBFBRLL
FFFBFFFRRR
BBFFBFFRLR
BBFFFFFRLR
FBFBBBBLLR
FFBFFBBLLR
FBBBBFFRLL
BFBBBFFRRR
FBFBBFBLRL
FBFBBFFRLL
FBBFFFFLLL
FBBFBFBRRL
FBBBBBFRLR
BFBBFFBLLL
FFBFBFBLRL
FBFFBFFRLR
FFBBBBBRLL
BBFBFFBRRL
BBBBFBBLRL
BFBFBBFRLL
FBBFBFFRLL
FBBBBFBLLL
FFBFBFFRLL
FBFFBFFRRR
FBFFFFFRRR
FBBBFFFLRL
BFBFFFBLRL
FBFFFFBRRL
FFBBFFFLRL
BFFFFFBLRL
FBFFBFFLLL
FBFBBBBRLR
BFFBBBFRLL
BBFBFFFLLR
BBFBFBBLRR
FBFFFBBLLR
FFBBFBFRLR
FBBFFBFRRL
FFFFBBFLRL
FBBFFFBLRR
BFBBBFFRLR
BFBFFFBRLL
FFBBFBBRLL
BFBFFBFRRL
FFBFBBFLRL
BFFBBFFLLR
FBFBFBFRRL
FFFBFFFLLR
BBFBBFFLRR
BBFFBBBLRR
BBBBFBFLLR
FBFBBFFLLL
FBBBFBFLRL
BBFBBFBLRR
BFFBBBBRLL
BBFBBBFLLL
FBFFFBBRLR
FFFBBBFRLL
BFFFFFBLRR
FBFBBBFRLR
FBBFFFFLRR
FFBBFBBLLR
FFFBBFBRLL
FBBFBFFRLR
FBFFBBFLRR
BBBFFFFRRR
FFFFBFBRRR
BBBFFFBLLR
FFBFBFBRRL
BFBBBBFRLR
BBBFFBFRLR
FFFBBBBRLR
FBBFBBFLLR
FFBBBBFRRL
BFFBFBBRRR
FBFFBBBLLR
BFFBBFBLLL
BFBFBBFRRL
FFFBBFBRRR
FFBBBBFRRR
BFBBBFFRLL
BFFBFBBRLL
FFBBBBFRLR
BBFBBBBLLL
BFBFBFBRLL
BFBBFFBRLR
BBBFFBBRRL
BBFFFFBLLL
FBBFFFBRLL
FFFBBBBRRR
BFFFBBFRLR
BBFBFBFLRR
FFBFFBBLLL
FFBBFFFRLL
FBBBFBBRRL
FBBBFBFRRR
FFBBBFFRRR
FBBFBBBRLR
FBBFFFFLLR
FFBFBBFRLR
BFFFFBFLRL
BBFFFFBRLR
BFBBBFBRLL
BBFFFFFRRR
BFBFBBBLRL
BBFBBBBRRL
BBBFFBFLLR
BFFBBBBLRL
FBFBFBBRRL
BFFFBFFLLR
BBBFBFBRRR
BFFFBBFLRL
FBBFBFFLLL
FFFBFFBRLL
FFBFFBFLRL
FBBFBFBLRR
FBBBFFBRRL
BFBBFFFRLR
BFFBFFBRRR
BFBBBBFRRL
BBBFBBFRLL
BBFFBFFLLL
BBBFBFFLRL
FFBBBBFRLL
FBFFFBFRRR
BFBFBBBRLL
FBFBBFFRLR
FBFBBBBLRL
FBBFFBBRLL
FBFBFFFRLL
BBFFBBBLRL
FBFBBFBLRR
FFFBFBFLRR
FBFBFFBLLL
BBFBFBBRRR
BBFBBBFRLL
FBFBBBFRRR
BBFFFFFRLL
FFBFFFFRLR
BFFFFFFRLR
BBBBFBFLLL
FBFFBBBLLL
BFFFBBBLLR
FBBBBFBLRR
BBFFFBBLRR
BFBBFBBRLR
FBFFFFFRLL
FBBBBFFRRR
BBFFFBBLLL
BFFBBFBRRR
BBFBBBFLLR
FBBFBBBRRL
FBFBBFFLLR
BBBFFFBRLR
FFFBFFBRLR
FBBBBBBLLL
BBFFBFBLLL
FBBFBBFRLL
BBBFFFBLRL
BFBBFBBLRR
BBFFBBBRRR
FBFFBFFLRL
FBBFFBBRRR
BBBFFFBLRR
FFFBBFBRLR
BBBBFFBLLR
FFBBBFBLRL
FFBFBBFRRL
FFBFBBFLRR
FBBBFFBRRR
FBBFFFFRLL
BBFFFFFLLL
FFBFBFBRRR
BFBBFBFRRL
BBFBFBFRLL
FFBFFBFRRR
FBBFBBFLRR
FBFFBFBRRR
BBFFFFFLRL
FBBBFFFRLL
BBFBBFFRRL
FFBBBFBRRL
FFBFFFBLLR
FBFBBFBRLL
FFBFFFBLRR
BFFBBBFRRL
BBBBFBBRLR
BFBBFFBRRL
BBFFFFFLLR
BBFFBFBLRR
BBBBFFBRRR
BFBBBFFRRL
FFFFBBBRRR
BFFFFFBRLL
BBFFBFBLLR
BBBFBFBRLL
BBBBFBBRRL
FBBFBBFRRL
BBFFBFFLRL
FFFBBFFRLR
FBBFBFBLRL
BBBBFFBLLL
FFBFBBBRRR
BFBFBFFRLL
BFBBBFBRRR
BBFBFFBLRL
FFFBBBFRRL
BBBFBFFRLR
BBFFBFFLRR
FFBFBBBRLR
BFBFFBFRLL
FBBBFBFLLR
BBFBBFFLLR
BFBFBBBRRR
FBFFBFFRRL
FBBBBBBLLR
BBFBFFBRRR
BBBFBBBLRR
BFBFFFFLRL
BFBFFFFRRL
BBFBFFFLLL
BFBFBFFLLR
FFFBBFFLLR
FFFBBFBLLL
BFBBFBBLLR
BFBFBFBLLR
BBFFBBBLLR
BFBFFBBLLL
FBBBFBFLRR
FBFFFFFLLL
BFFFBBFRRL
BFBFFFFRLL
BBFFBFBRLL
BFBFBFFRLR
FBFFFBBRRL
FBBBBFBRLR
FFBBFFBRLL
BFBBFBFRLR
FFFBFBBLRR
BFBFFFFLRR
BFFFBFFRLL
FFFBBBFLRR
FFBBFFFRLR
BFBBBFBLLL
FFBBFBBRRR
BFBBFFFRRL
FFFBFBFRRR
FBBBBFBRLL
FBFFFBFRLR
BFFBBFBRLR
BBBFFBFRRR
FFBFBFFLRL
FBFBBBBLLL
FBBFFFBLRL
BBBFBFFLRR
FBFFFFBRLL
FFBBFBFRRL
BFBFBBBLLL
FBFFBFBRLR
FBFBBFBLLR
FFBFBFFLLR
BFBFBFFLLL
BBFBFFFLRR
FBBFFBBLRL
BBBBFFFRRR
FFBFBFBRLR
BFBBBBBRRR
FBBFFFFLRL
BFFFBBBLLL
FFBFBFFRLR
BBBBFBFRRL
FBBBFBFLLL
BFBFFFBRRL
BBBFFBFLRL
BBBBFFBLRR
BBBBFBFRRR
BBFBBBFLRL
FFFBBFBLRL
FBFBFBBLRR
BFBFFBBRRL
BBBBFBBLRR
BFFFFBBLRL
FBFBFBFLLL
BBBFBBBLLR
BFBFFFBLLR
FFBFBBFRRR
FBBFBBBLLR
BFBBBBBRRL
BFFBBFFRLR
FFBBFFBRRL
BBBBFFBRLR
BBFFFBBRRL
BBFBBFFLRL
FFBBFFFRRL
BBFBFFFLRL
BFBBBFFLLL
BFFFBFBRLR
FFBFBBFLLL
BBFFBBFRLL
BBFBFFFRRR
BFFBFBBRLR
FFBFBFBLRR
BFFBFFFLLR
FFFBBBFRLR
BFBFFBBRRR
BFFFFBFLLR
FBFFFFFLRL
BFFBBBBLLR
BBBBFFFRLR
FBFBFBBLRL
FFFFBBFRRR
FFFBFBBLLL
BFFBFFFLRL
BFBFBBFLRR
BBFFFBFRLR
BFBFBFFLRR
FFFBFFBLRR
BBFBBFBRRR
FBBFBBFLRL
"""
PASSES = REAL_PASSES

def get_row(partitions):
    min_row, max_row = 0, 127
    for partition in partitions:
        mid = (min_row + max_row) / 2
        if partition == 'F':
            mid = math.floor(mid)
            max_row = mid
        else:
            mid = math.ceil(mid)
            min_row = mid
    return mid

def get_column(partitions):
    min_col, max_col = 0, 7
    for partition in partitions:
        mid = (min_col + max_col) / 2
        if partition == 'L':
            mid = math.floor(mid)
            max_col = mid
        else:
            mid = math.ceil(mid)
            min_col = mid
    return mid

def get_seat_id(partitions):
    return 8 * get_row(partitions[:7]) + get_column(partitions[-3:])

#print(max(get_seat_id(p) for p in PASSES.splitlines()))
ids = sorted([get_seat_id(p) for p in PASSES.splitlines()])
last_id = ids[0]
for i in ids:
    if last_id == i - 2:
        print(i - 1)
    last_id = i
