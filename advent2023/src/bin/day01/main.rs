use advent2023;

const DIGITS: [&str; 9] = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
];

fn part1(input: &str) -> String {
    input
        .lines()
        .map(|line| {
            let mut iter = line.matches(char::is_numeric).map(|v| v.parse().unwrap());
            let first: u32 = iter.next().unwrap();
            let last = iter.last().unwrap_or(first);
            first * 10 + last
        })
        .sum::<u32>()
        .to_string()
}

fn convert_digit(input: &str) -> u32 {
    for (i, digit) in (1..).zip(DIGITS) {
        if input == digit {
            return i;
        }
    }
    input.parse().unwrap()
}

fn part2(input: &str) -> String {
    input
        .lines()
        .map(|line| {
            DIGITS
                .iter()
                .map(|s| line.match_indices(s))
                .flatten()
                .chain(line.match_indices(char::is_numeric))
                .fold([(usize::MAX, ""), (usize::MIN, "")], |acc, item| {
                    [item.min(acc[0]), item.max(acc[1])]
                })
                .iter()
                .fold(0, |acc, (_, v)| acc * 10 + convert_digit(v))
        })
        .sum::<u32>()
        .to_string()
}

fn main() {
    let file_contents = vec![
        include_str!("example"),
        include_str!("example2"),
        include_str!("input")
    ];
    advent2023::solve_day(&file_contents, part1, part2);
}
