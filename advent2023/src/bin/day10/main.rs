#[macro_use]
extern crate lazy_static;

mod map;

use map::Map;

fn part1(input: &str) -> usize {
    let map = Map::new(input);
    map.track_cycle().len() / 2
}

fn main() {
    let file_contents = vec![include_str!("example"), include_str!("input")];
    advent2023::calculate_and_print(&file_contents, part1, part1);
}

#[cfg(test)]
mod day10 {
    use super::*;

    #[test]
    fn test_part1() {
        assert_eq!(part1(include_str!("example")), 4);
        assert_eq!(part1(include_str!("example2")), 8);
        assert_eq!(part1(include_str!("input")), 6823);
    }

    //#[test]
    //fn test_part2() {
    //    assert_eq!(part2(include_str!("example")), 2);
    //    assert_eq!(part2(include_str!("input")), 864);
    //}
}
