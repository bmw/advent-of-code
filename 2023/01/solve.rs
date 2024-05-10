use std::fs;

const DIGITS: [&str; 9] = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
];

fn part1(input: &str) -> u32 {
    input.lines()
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
    input.lines()
        .map(|line| {
            let mut matches: Vec<_> = line.match_indices(char::is_numeric).collect();
            for digit in DIGITS {
                matches.extend(line.match_indices(digit));
            }
            matches.sort();
            let first = convert_digit(matches[0].1);
            let last = convert_digit(matches[matches.len() - 1].1);
            first * 10 + last
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
