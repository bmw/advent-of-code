use std::collections::HashMap;

#[derive(Clone, Copy, Debug)]
enum Direction {
    Left,
    Right,
}
fn parse_route_line(input: &str) -> Vec<Direction> {
    input
        .chars()
        .map(|c| {
            if c == 'L' {
                Direction::Left
            } else {
                assert_eq!(c, 'R');
                Direction::Right
            }
        })
        .collect()
}

fn parse(input: &str) -> (Vec<Direction>, HashMap<&str, (&str, &str)>) {
    let mut iter = input.lines();
    let route = parse_route_line(iter.next().unwrap());

    let network = iter
        .skip(1)
        .map(|s| {
            let mut iter = s.split_whitespace();
            let key = iter.next().unwrap();
            // skip equals sign
            iter.next();
            let value1 = iter.next().unwrap();
            // remove leading ( and trailing ,
            let value1 = &value1[1..value1.len() - 1];
            let value2 = iter.next().unwrap();
            // remove trailing )
            let value2 = &value2[..value2.len() - 1];
            (key, (value1, value2))
        })
        .collect();
    (route, network)
}

fn part1(input: &str) -> u64 {
    let (route, network) = parse(input);
    let mut route_iter = route.iter().cycle();
    let mut position = "AAA";
    let mut step_count = 0;
    while position != "ZZZ" {
        position = match route_iter.next().unwrap() {
            Direction::Left => network[position].0,
            Direction::Right => network[position].1,
        };
        step_count += 1;
    }

    step_count
}

fn part2(input: &str) -> u64 {
    let (route, network) = parse(input);
    let mut route_iter = route.iter().cycle();
    let mut positions: Vec<&str> = network
        .keys()
        .filter_map(|k| if k.ends_with('A') { Some(*k) } else { None })
        .collect();
    let mut step_count = 0;
    // too slow, gotta find cycle len and overlap..
    while positions.iter().any(|p| !p.ends_with('Z')) {
        let direction = route_iter.next().unwrap();
        for position in positions.iter_mut() {
            *position = match direction {
                Direction::Left => network[position].0,
                Direction::Right => network[position].1,
            };
        }
        step_count += 1;
    }
    step_count
}

fn main() {
    let file_contents = vec![include_str!("example"), include_str!("input")];
    advent2023::calculate_and_print(&file_contents, part1, part2);
}

#[cfg(test)]
mod day08 {
    use super::*;

    #[test]
    fn test_part1() {
        assert_eq!(part1(include_str!("example")), 2);
        assert_eq!(part1(include_str!("example2")), 6);
        assert_eq!(part1(include_str!("input")), 12169);
    }

    #[test]
    fn test_part2() {
        assert_eq!(part2(include_str!("example3")), 6);
        //assert_eq!(part2(include_str!("input")), 248909434);
    }
}
