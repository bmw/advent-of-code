use std::fs;

const DIGITS: [&str; 9] = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
];

fn numeric_digits(line: &str) -> (Option<(usize, u32)>, Option<(usize, u32)>) {
    let mut iter = line.match_indices(char::is_numeric);
    let first = iter.next().map(|(i, v)| (i, v.parse().unwrap()));
    let last = iter.last().map_or(first, |(i, v)| Some((i, v.parse().unwrap())));
    (first, last)
}

fn part1(input: &str) -> u32 {
    input.lines()
        .map(|line| {
            let (first, last) = numeric_digits(line);
            first.unwrap().1 * 10 + last.unwrap().1
        })
        .sum()
}

fn part2(input: &str) -> u32 {
    input.lines()
        .map(|line| {
            let (mut first, mut last) = numeric_digits(line);
            for (i, digit) in (1..).zip(DIGITS) {
                let mut iter = line.match_indices(digit).peekable();
                first = iter.peek().map_or(first, |&(j, _)| {
                    if first.is_none() || j < first.unwrap().0 {
                        return Some((j, i));
                    }
                    first
                });
                last = iter.last().map_or(last, |(j, _)| {
                    if last.is_none() || j > last.unwrap().0 {
                        return Some((j, i));
                    }
                    last
                });
            }
            first.unwrap().1 * 10 + last.unwrap().1
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
