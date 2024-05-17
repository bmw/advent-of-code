use std::ops::Range;

#[derive(Clone, Debug)]
struct MapRange {
    dest_start: u64,
    src: Range<u64>,
}

impl MapRange {
    fn new(dest_start: u64, src_start: u64, len: u64) -> Self {
        MapRange {
            dest_start,
            src: (src_start..src_start + len),
        }
    }
}

fn get_seeds(seed_line: &str) -> Vec<u64> {
    seed_line
        .split_whitespace()
        .skip(1)
        .map(|i| i.parse().unwrap())
        .collect()
}

fn build_map<'a>(iter: &mut impl Iterator<Item = &'a str>) -> Vec<MapRange> {
    let iter = iter.take_while(|s| !s.is_empty());
    let mut result = Vec::new();
    for s in iter {
        let values: Vec<u64> = s.split_whitespace().map(|i| i.parse().unwrap()).collect();
        assert_eq!(values.len(), 3);
        result.push(MapRange::new(values[0], values[1], values[2]));
    }
    result
}

fn apply_map<'a>(iter: &mut impl Iterator<Item = &'a str>, seeds: &mut Vec<u64>) {
    let map = build_map(iter);
    for seed in seeds {
        if let Some(range) = map.iter().find(|r| r.src.contains(seed)) {
            *seed = *seed - range.src.start + range.dest_start;
        }
    }
}

fn part1(input: &str) -> u64 {
    let mut iter = input.lines();
    let seed_line = iter.next().unwrap();
    let mut seeds = get_seeds(seed_line);
    // skip blank line after seed line
    _ = iter.next();
    while iter.next().is_some() {
        // the above iter.next() call skips the map header
        apply_map(&mut iter, &mut seeds);
    }
    *seeds.iter().min().unwrap()
}

fn part2(_input: &str) -> u64 {
    42
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

    //#[test]
    //fn test_part2() {
    //    assert_eq!(part2(include_str!("example")), 30);
    //    assert_eq!(part2(include_str!("input")), 10378710);
    //}
}
