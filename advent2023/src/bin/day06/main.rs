fn parse_line_part1<'a>(iter: &mut impl Iterator<Item = &'a str>) -> Vec<u64> {
    iter.next()
        .unwrap()
        .split_whitespace()
        .skip(1)
        .map(|s| s.parse().unwrap())
        .collect()
}

fn parse_part1(input: &str) -> (Vec<u64>, Vec<u64>) {
    let mut iter = input.lines();
    let times = parse_line_part1(&mut iter);
    let distances = parse_line_part1(&mut iter);
    (times, distances)
}

fn ways2win(total_time: u64, distance: u64) -> u64 {
    let is_way_to_win = |hold_time| hold_time * (total_time - hold_time) > distance;
    let min = (1..total_time)
        .find(|&hold_time| is_way_to_win(hold_time))
        .unwrap();
    let max = (1..total_time)
        .rfind(|&hold_time| is_way_to_win(hold_time))
        .unwrap();
    max + 1 - min
}

fn part1(input: &str) -> u64 {
    let (times, distances) = parse_part1(input);
    times
        .into_iter()
        .zip(distances)
        .map(|(time, distance)| ways2win(time, distance))
        .product()
}

fn parse_line_part2<'a>(iter: &mut impl Iterator<Item = &'a str>) -> u64 {
    iter.next()
        .unwrap()
        .split_once(':')
        .unwrap()
        .1
        .replace(char::is_whitespace, "")
        .parse()
        .unwrap()
}

fn parse_part2(input: &str) -> (u64, u64) {
    let mut iter = input.lines();
    let time = parse_line_part2(&mut iter);
    let distance = parse_line_part2(&mut iter);
    (time, distance)
}

fn part2(input: &str) -> u64 {
    let (time, distance) = parse_part2(input);
    ways2win(time, distance)
}

fn main() {
    let file_contents = vec![include_str!("example"), include_str!("input")];
    advent2023::calculate_and_print(&file_contents, part1, part2);
}

#[cfg(test)]
mod day06 {
    use super::*;

    #[test]
    fn test_part1() {
        assert_eq!(part1(include_str!("example")), 288);
        assert_eq!(part1(include_str!("input")), 4403592);
    }

    #[test]
    fn test_part2() {
        assert_eq!(part2(include_str!("example")), 71503);
        assert_eq!(part2(include_str!("input")), 38017587);
    }
}
