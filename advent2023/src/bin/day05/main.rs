use std::error;
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

fn build_map(map_lines: &[&str]) -> Vec<MapRange> {
    map_lines
        .iter()
        .map(|line| MapRange::try_from(*line).unwrap())
        .collect()
}

fn apply_map(map: &[MapRange], seeds: &mut [u64]) {
    for seed in seeds {
        if let Some(range) = map.iter().find(|r| r.src.contains(seed)) {
            *seed = *seed - range.src.start + range.dest_start;
        }
    }
}

fn do_part(input: &str, seed_fn: impl Fn(&str) -> Vec<u64>) -> u64 {
    let mut iter = input.lines().filter(|line| !line.is_empty()).peekable();
    let mut seeds = seed_fn(iter.next().unwrap());

    while iter.peek().is_some() {
        let map_lines: Vec<&str> = iter
            .by_ref()
            .take_while(|line| line.as_bytes()[0].is_ascii_digit())
            .collect();
        apply_map(&build_map(&map_lines), &mut seeds);
    }
    *seeds.iter().min().unwrap()
}

fn part1(input: &str) -> u64 {
    do_part(input, |seed_line| {
        seed_line
            .split_whitespace()
            .skip(1)
            .map(|i| i.parse().unwrap())
            .collect()
    })
}

fn part2(_input: &str) -> u64 {
    // this is WAY too slow. generating the seeds is pretty bad, but what's really bad is applying
    // the map n times. try merging maps into one that maps initial input to final output? even
    // then, i think i'll need to do something clever to find the min output without trying all
    // inputs
    //do_part(input, |seed_line| {
    //    let v: Vec<_> = seed_line.split_whitespace()
    //        .skip(1)
    //        .map(|i| i.parse().unwrap()).collect();
    //    v.chunks(2)
    //        .flat_map(|chunk| (chunk[0]..chunk[0] + chunk[1]))
    //        .collect()
    //})
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
