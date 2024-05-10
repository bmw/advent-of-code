use std::fs;

const DIGITS: [&str; 9] = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
];

fn part1(input: &str) -> u32 {
    input
        .lines()
        .map(|line| {
            let mut iter = line.matches(char::is_numeric);
            let first: u32 = iter.next().unwrap().parse().unwrap();
            let last = iter.last().map_or(first, |v| v.parse().unwrap());
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
                .map(|s| line.match_indices(s))
                .flatten()
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
    for name in ["example", "example2", "input"] {
        let input = fs::read_to_string(name).unwrap();
        if name != "example2" {
            println!("part 1 answer for {name}: {}", part1(&input));
        }
        if name != "example" {
            println!("part 2 answer for {name}: {}", part2(&input));
        }
    }
}
