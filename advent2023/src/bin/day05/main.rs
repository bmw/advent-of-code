mod num_map;

use std::cmp::{max, min};
use std::error;
use std::ops::Range;
use num_map::NumMap;

type Map = Vec<MapRange>;
type SeedRanges = Vec<Range<u64>>;

#[derive(Clone, Copy, Debug)]
struct MapRange {
    dest_start: u64,
    src_start: u64,
    len: u64,
}

impl MapRange {
    fn new(dest_start: u64, src_start: u64, len: u64) -> Self {
        Self {
            dest_start,
            src_start,
            len,
        }
    }

    fn dest_contains(&self, num: u64) -> bool {
        num >= self.dest_start && num < self.dest_end()
    }

    fn dest_end(&self) -> u64 {
        self.dest_start + self.len
    }

    fn src_contains(&self, num: u64) -> bool {
        num >= self.src_start && num < self.src_end()
    }

    fn src_end(&self) -> u64 {
        self.src_start + self.len
    }
}

impl TryFrom<&str> for MapRange {
    type Error = Box<dyn error::Error>;
    fn try_from(value: &str) -> Result<Self, Self::Error> {
        let mut v = Vec::new();
        for i in value.split_whitespace() {
            v.push(i.parse()?);
        }
        assert_eq!(v.len(), 3);
        Ok(MapRange::new(v[0], v[1], v[2]))
    }
}

fn build_map(map_lines: &[&str]) -> Map {
    map_lines
        .iter()
        .map(|line| MapRange::try_from(*line).unwrap())
        .collect()
}

fn apply_map(map: &[MapRange], seeds: &mut [u64]) {
    for seed in seeds {
        if let Some(range) = map.iter().find(|r| r.src_contains(*seed)) {
            *seed = *seed - range.src_start + range.dest_start;
        }
    }
}

fn find_intersection(map1: &Map, map2: &Map) -> Option<(usize, usize)> {
    for (i, r1) in map1.iter().enumerate() {
        for (j, r2) in map2.iter().enumerate() {
            if r1.src_contains(r2.src_start) || r2.src_contains(r1.src_start) {
                return Some((i, j));
            }
        }
    }
    None
}

fn merge_if_no_overlap(new_map: &mut Map, old_map: &Map) {
    for mut old_ranges in old_map.iter().map(|r| vec![*r]) {
        while let Some((new_i, old_i)) = find_intersection(new_map, &old_ranges) {
            let old_range = old_ranges.swap_remove(old_i);
            let new_range = new_map[new_i];
            let overlap_start = max(old_range.src_start, new_range.src_start);
            let overlap_end = min(old_range.src_end(), new_range.src_end());
            let overlap_len = overlap_end - overlap_start;
            if old_range.len - overlap_len > 0 {
                if old_range.src_start < new_range.src_start {
                    let len = new_range.src_start - old_range.src_start;
                    old_ranges.push(MapRange::new(
                        old_range.dest_start,
                        old_range.src_start,
                        len,
                    ));
                }
                if old_range.src_end() > new_range.src_end() {
                    let len = old_range.src_end() - new_range.src_end();
                    let offset = new_range.src_end() - old_range.src_start;
                    let new_dst = old_range.dest_start + offset;
                    old_ranges.push(MapRange::new(new_dst, new_range.src_end(), len));
                }
            }
        }
        new_map.extend(old_ranges);
    }
}

fn update_map(old_map: &Map, new_map_lines: &[&str]) -> Map {
    let new_map = build_map(new_map_lines);
    let mut merged_map = Map::new();
    for new_range in &new_map {
        for old_range in old_map {
            if old_range.dest_contains(new_range.src_start)
                || new_range.src_contains(old_range.dest_start)
            {
                let overlap_start = max(old_range.dest_start, new_range.src_start);
                let overlap_end = min(old_range.dest_end(), new_range.src_end());
                let overlap_len = overlap_end - overlap_start;
                let old_offset = overlap_start - old_range.dest_start;
                let new_offset = overlap_start - new_range.src_start;
                merged_map.push(MapRange::new(
                    new_range.dest_start + new_offset,
                    old_range.src_start + old_offset,
                    overlap_len,
                ));
            }
        }
    }
    merge_if_no_overlap(&mut merged_map, &old_map);
    merge_if_no_overlap(&mut merged_map, &new_map);
    merged_map
}

fn seeds_to_test(seed_ranges: &SeedRanges, map: &NumMap) -> Vec<u64> {
    let mut v = Vec::new();
    for entry in map.iter() {
        for seed_range in seed_ranges {
            if seed_range.contains(&entry.src) || (entry.src..entry.src + entry.len).contains(&seed_range.start)
            {
                v.push(max(entry.src, seed_range.start));
            }
        }
    }
    for seed_range in seed_ranges {
        v.push(seed_range.start);
    }
    v
}

fn do_part<T: Fn(&str) -> SeedRanges>(input: &str, seed_fn: T) -> u64 {
    let mut iter = input.lines().filter(|line| !line.is_empty()).peekable();
    let seed_ranges = seed_fn(iter.next().unwrap());
    let mut map = NumMap::default();

    let _ = iter.next();
    while iter.peek().is_some() {
        let map_lines: Vec<&str> = iter
            .by_ref()
            .take_while(|line| line.as_bytes()[0].is_ascii_digit())
            .collect();
        let tmp_map = NumMap::try_from(&map_lines).unwrap();
        map = map.merged_maps(&tmp_map);
    }
    let mut seeds = seeds_to_test(&seed_ranges, &map);
    seeds.iter().map(|&v| map.map_value(v)).min().unwrap()
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
