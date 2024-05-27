use std::collections::HashMap;
use std::error;
use std::str::FromStr;

#[derive(Clone, Copy, Debug, PartialEq, Eq, PartialOrd, Ord)]
enum HandType {
    HighCard,
    OnePair,
    TwoPair,
    ThreeOfAKind,
    FullHouse,
    FourOfAKind,
    FiveOfAKind,
}

#[derive(Clone, Debug, PartialEq, Eq, PartialOrd, Ord)]
struct Hand {
    hand_type: HandType,
    cards: [u8; 5],
}

fn determine_hand_type(cards: &[u8; 5]) -> HandType {
    let mut map = HashMap::<u8, u8>::new();
    for &card in cards {
        *map.entry(card).or_default() += 1;
    }
    let card_counts: Vec<_> = map.into_values().collect();
    if card_counts.len() == 5 {
        HandType::HighCard
    } else if card_counts.contains(&5) {
        HandType::FiveOfAKind
    } else if card_counts.contains(&4) {
        HandType::FourOfAKind
    } else if card_counts.contains(&3) {
        if card_counts.contains(&2) {
            HandType::FullHouse
        } else {
            HandType::ThreeOfAKind
        }
    } else if card_counts.len() == 3 {
        HandType::TwoPair
    } else {
        assert_eq!(card_counts.len(), 4);
        HandType::OnePair
    }
}

impl FromStr for Hand {
    type Err = Box<dyn error::Error>;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let mut cards = [0; 5];
        for (i, v) in s.as_bytes().iter().enumerate() {
            cards[i] = match *v {
                b'A' => b'9' + 5,
                b'K' => b'9' + 4,
                b'Q' => b'9' + 3,
                b'J' => b'9' + 2,
                b'T' => b'9' + 1,
                v if (b'2'..=b'9').contains(&v) => v,
                _ => panic!("bad card"),
            };
        }
        Ok(Hand {
            hand_type: determine_hand_type(&cards),
            cards,
        })
    }
}

fn parse(input: &str) -> Vec<(Hand, u64)> {
    input
        .lines()
        .map(|s| {
            let (cards, bid) = s.split_once(char::is_whitespace).unwrap();
            (cards.parse().unwrap(), bid.parse().unwrap())
        })
        .collect()
}

fn part1(input: &str) -> u64 {
    let mut v = parse(input);
    v.sort_unstable();
    (1..).zip(v).map(|(i, (_, bid))| i * bid).sum()
}

fn main() {
    let file_contents = vec![include_str!("example"), include_str!("input")];
    advent2023::calculate_and_print(&file_contents, part1, part1);
}

#[cfg(test)]
mod day07 {
    use super::*;

    #[test]
    fn test_part1() {
        assert_eq!(part1(include_str!("example")), 6440);
        assert_eq!(part1(include_str!("input")), 250474325);
    }

    //#[test]
    //fn test_part2() {
    //    assert_eq!(part2(include_str!("example")), 71503);
    //    assert_eq!(part2(include_str!("input")), 38017587);
    //}
}
