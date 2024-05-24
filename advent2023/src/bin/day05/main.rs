use std::cmp::min;
use std::collections::BTreeMap;
use std::ops::Range;

type Map = BTreeMap<u64, MapValue>;
type SeedRanges = Vec<Range<u64>>;

#[derive(Clone, Copy, Debug)]
struct MapValue {
    dest: u64,
    len: u64,
}

fn build_map(map_lines: &[&str]) -> Map {
    let mut map = Map::new();
    for line in map_lines {
        let v: Vec<_> = line
            .split_whitespace()
            .map(|s| s.parse().unwrap())
            .collect();
        assert_eq!(v.len(), 3);
        map.insert(
            v[1],
            MapValue {
                dest: v[0],
                len: v[2],
            },
        );
    }
    map
}

fn apply_map(input_ranges: &SeedRanges, map: &Map) -> SeedRanges {
    let mut output_ranges = Vec::new();
    for range in input_ranges {
        let mut range = range.clone();
        let mut iter = map.iter().peekable();
        while range.start != range.end {
            match iter.peek() {
                // either the range comes before the current map entry...
                Some((&src, _)) if range.start < src => {
                    let end = min(range.end, src);
                    output_ranges.push(range.start..end);
                    range.start = end;
                }
                // overlaps with the current map entry...
                Some((&src, &MapValue { mut dest, len }))
                    if range.start >= src && range.start < src + len =>
                {
                    let offset = range.start - src;
                    dest += offset;
                    let len = min(range.end - range.start, len - offset);
                    output_ranges.push(dest..dest + len);
                    range.start += len;
                    iter.next();
                }
                // comes after the current map entry...
                Some(_) => {
                    iter.next();
                }
                // or there are no map entries left
                None => {
                    output_ranges.push(range.clone());
                    range.start = range.end;
                }
            }
        }
    }
    output_ranges
}

fn do_part<T: Fn(&str) -> SeedRanges>(input: &str, seed_fn: T) -> u64 {
    let mut iter = input.lines().filter(|line| !line.is_empty()).peekable();
    let mut seeds = seed_fn(iter.next().unwrap());

    let _ = iter.next();
    while iter.peek().is_some() {
        let map_lines: Vec<&str> = iter
            .by_ref()
            .take_while(|line| line.as_bytes()[0].is_ascii_digit())
            .collect();
        seeds = apply_map(&seeds, &build_map(&map_lines));
    }
    seeds.iter().map(|r| r.start).min().unwrap()
}

fn seed_line_to_ints(line: &str) -> Vec<u64> {
    line.split_whitespace()
        .skip(1)
        .map(|i| i.parse().unwrap())
        .collect()
}

fn parse_part1_seeds(line: &str) -> SeedRanges {
    seed_line_to_ints(line)
        .iter()
        .map(|&i| (i..i + 1))
        .collect()
}

fn part1(input: &str) -> u64 {
    do_part(input, parse_part1_seeds)
}

fn parse_part2_seeds(line: &str) -> SeedRanges {
    seed_line_to_ints(line)
        .chunks(2)
        .map(|chunk| (chunk[0]..chunk[0] + chunk[1]))
        .collect()
}

fn part2(input: &str) -> u64 {
    do_part(input, parse_part2_seeds)
}

fn main() {
    let file_contents = vec![include_str!("example"), include_str!("input")];
    advent2023::calculate_and_print(&file_contents, part1, part2);
}

#[cfg(test)]
mod day05 {
    use super::*;

    #[test]
    fn test_part1() {
        assert_eq!(part1(include_str!("example")), 35);
        assert_eq!(part1(include_str!("input")), 379811651);
    }

    #[test]
    fn test_part2() {
        assert_eq!(part2(include_str!("example")), 46);
        assert_eq!(part2(include_str!("input")), 27992443);
    }
}
