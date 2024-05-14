use std::collections::HashMap;
use std::cmp::max;

#[derive(Clone,Copy,Debug)]
pub struct Game {
    pub id: u32,
    pub max_red: u32,
    pub max_green: u32,
    pub max_blue: u32,
}

fn parse_id(header: &str) -> u32 {
    header.split_whitespace().nth(1).unwrap().parse().unwrap()
}

fn parse_color_counts(rounds: &str) -> HashMap<&str, u32> {
    let mut max_counts: HashMap<&str, u32> = HashMap::new();
    for round in rounds.split(&[';', ',']) {
        let (count, color) = round.trim().split_once(' ').unwrap();
        let count = count.parse().unwrap();
        max_counts.entry(color).and_modify(|prev_count| *prev_count = max(*prev_count, count)).or_insert(count);
    }
    max_counts
}

impl Game {
    pub fn new(input: &str) -> Self {
        let (header, rounds) = input.split_once(':').unwrap();
        let counts = parse_color_counts(rounds);
        Game {
            id: parse_id(header),
            max_red: counts["red"],
            max_green: counts["green"],
            max_blue: counts["blue"],
        }
    }
}
