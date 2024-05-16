use std::collections::HashSet;

fn parse_nums(s: &str) -> HashSet<u32> {
    s.split_whitespace().map(|i| i.parse().unwrap()).collect()
}

fn get_matches_per_card(input: &str) -> Vec<usize> {
    input
        .lines()
        .map(|line| {
            let (_card_title, numbers) = line.split_once(':').unwrap();
            let (winning_nums, your_nums) = numbers.split_once('|').unwrap();
            let winning_nums = parse_nums(winning_nums);
            let your_nums = parse_nums(your_nums);

            winning_nums.intersection(&your_nums).count()
        })
        .collect()
}

fn part1(input: &str) -> u32 {
    get_matches_per_card(input)
        .into_iter()
        .map(|i| {
            if i == 0 {
                0
            } else {
                2u32.pow((i - 1).try_into().unwrap())
            }
        })
        .sum()
}

fn part2(input: &str) -> u32 {
    let matches_per_card = get_matches_per_card(input);
    let mut copies_per_card = vec![1; matches_per_card.len()];
    for (i, num_matches) in (0..).zip(matches_per_card) {
        let next = i + 1;
        for j in next..next + num_matches {
            copies_per_card[j] += copies_per_card[i];
        }
    }
    copies_per_card.iter().sum()
}

fn main() {
    let file_contents = vec![include_str!("example"), include_str!("input")];
    advent2023::calculate_and_print(&file_contents, part1, part2);
}

#[cfg(test)]
mod day04 {
    use super::*;

    #[test]
    fn test_part1() {
        assert_eq!(part1(include_str!("example")), 13);
        assert_eq!(part1(include_str!("input")), 19855);
    }

    #[test]
    fn test_part2() {
        assert_eq!(part2(include_str!("example")), 30);
        assert_eq!(part2(include_str!("input")), 10378710);
    }
}
