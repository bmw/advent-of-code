use std::error;
use std::ops::Range;

type Map = Vec<MapEntry>;
type SeedRanges = Vec<Range<u64>>;

#[derive(Clone, Debug)]
struct MapEntry {
    src_start: u64,
    dest_start: u64,
    len: u64,
}

impl MapEntry {
    fn src_overlaps_with(&self, range: &Range<u64>) -> bool {
        (self.src_start..self.src_start + self.len).contains(&range.start)
            || range.contains(&self.src_start)
    }
}

impl TryFrom<&str> for MapEntry {
    type Error = Box<dyn error::Error>;
    fn try_from(value: &str) -> Result<Self, Self::Error> {
        let mut v = Vec::new();
        for i in value.split_whitespace() {
            v.push(i.parse()?);
        }
        assert_eq!(v.len(), 3);
        Ok(MapEntry {
            dest_start: v[0],
            src_start: v[1],
            len: v[2],
        })
    }
}

fn build_map(map_lines: &[&str]) -> Map {
    map_lines
        .iter()
        .map(|&line| MapEntry::try_from(line).unwrap())
        .collect()
}

// we modify seed_ranges directly rather than cloning it just because we don't need it anymore
fn apply_map(seed_ranges: &mut SeedRanges, map: &Map) -> SeedRanges {
    let mut output_ranges = Vec::new();
    while let Some(mut range) = seed_ranges.pop() {
        match map.iter().find(|e| e.src_overlaps_with(&range)) {
            Some(entry) => {
                // split off any part before entry
                if range.start < entry.src_start {
                    seed_ranges.push(range.start..entry.src_start);
                    range.start = entry.src_start;
                }
                let entry_src_end = entry.src_start + entry.len;
                // split off any part after entry
                if range.end > entry_src_end {
                    seed_ranges.push(entry_src_end..range.end);
                    range.end = entry_src_end;
                }
                // map range through entry
                let new_start = entry.dest_start + range.start - entry.src_start;
                let new_end = entry.dest_start + range.end - entry.src_start;
                output_ranges.push(new_start..new_end);
            }
            None => {
                output_ranges.push(range);
            }
        }
    }
    output_ranges
}

fn do_part<T: Fn(&str) -> SeedRanges>(input: &str, seed_fn: T) -> u64 {
    let mut iter = input.lines();
    let mut seeds = seed_fn(iter.next().unwrap());

    // we skip the blank line after the seed line
    let mut iter = iter.skip(1).peekable();
    while iter.peek().is_some() {
        let map_lines: Vec<&str> = iter
            .by_ref()
            .skip(1) // skip map header
            .take_while(|line| !line.is_empty())
            .collect();
        let map = build_map(&map_lines);
        seeds = apply_map(&mut seeds, &map);
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
