mod num_map;

use std::cmp::max;
use std::ops::Range;
use num_map::NumMap;

type SeedRanges = Vec<Range<u64>>;

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
    let seeds = seeds_to_test(&seed_ranges, &map);
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
