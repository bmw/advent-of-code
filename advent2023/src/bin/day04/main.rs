use std::collections::HashSet;

fn parse_nums(s: &str) -> HashSet<u32> {
    s.split_whitespace().map(|i| i.parse().unwrap()).collect()
}

fn part1(input: &str) -> u32 {
    input
        .lines()
        .map(|line| {
            let (_card_title, numbers) = line.split_once(':').unwrap();
            let (winning_nums, your_nums) = numbers.split_once('|').unwrap();
            let winning_nums = parse_nums(winning_nums);
            let your_nums = parse_nums(your_nums);

            your_nums.iter().fold(0, |acc, num| {
                if !winning_nums.contains(num) {
                    acc
                } else if acc == 0 {
                    1
                } else {
                    acc * 2
                }
            })
        })
        .sum()
}

fn main() {
    let file_contents = vec![include_str!("example"), include_str!("input")];
    advent2023::calculate_and_print(&file_contents, part1, part1);
}

#[cfg(test)]
mod day04 {
    use super::*;

    #[test]
    fn test_part1() {
        assert_eq!(part1(include_str!("example")), 13);
        assert_eq!(part1(include_str!("input")), 19855);
    }

    //#[test]
    //fn test_part2() {
    //    assert_eq!(part2(include_str!("example2")), 281);
    //    assert_eq!(part2(include_str!("input")), 54770);
    //}
}
