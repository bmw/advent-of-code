const DIGITS: [&str; 9] = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
];

fn part1(input: &str) -> u32 {
    input
        .lines()
        .map(|line| {
            let mut iter = line.matches(char::is_numeric).map(|v| v.parse().unwrap());
            let first: u32 = iter.next().unwrap();
            let last = iter.last().unwrap_or(first);
            first * 10 + last
        })
        .sum()
}

fn convert_digit(input: &str) -> u32 {
    for (i, digit) in (1..).zip(DIGITS) {
        if input == digit {
            return i;
        }
    }
    input.parse().unwrap()
}

fn part2(input: &str) -> u32 {
    input
        .lines()
        .map(|line| {
            DIGITS
                .iter()
                .flat_map(|s| line.match_indices(s))
                .chain(line.match_indices(char::is_numeric))
                .fold([(usize::MAX, ""), (usize::MIN, "")], |acc, item| {
                    [item.min(acc[0]), item.max(acc[1])]
                })
                .iter()
                .fold(0, |acc, (_, v)| acc * 10 + convert_digit(v))
        })
        .sum()
}

fn main() {
    let file_contents = vec![
        include_str!("example"),
        include_str!("example2"),
        include_str!("input"),
    ];
    advent2023::calculate_and_print(&file_contents, part1, part2);
}

#[cfg(test)]
mod day01 {
    use super::*;

    #[test]
    fn test_part1() {
        assert_eq!(part1(include_str!("example")), 142);
        assert_eq!(part1(include_str!("input")), 54630);
    }

    #[test]
    fn test_part2() {
        assert_eq!(part2(include_str!("example2")), 281);
        assert_eq!(part2(include_str!("input")), 54770);
    }
}
