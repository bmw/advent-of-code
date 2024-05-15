mod game;
use crate::game::Game;

fn part1(input: &str) -> u32 {
    input
        .lines()
        .map(|line| {
            let game = Game::new(line);
            if game.max_red <= 12 && game.max_green <= 13 && game.max_blue <= 14 {
                game.id
            } else {
                0
            }
        })
        .sum()
}

fn part2(input: &str) -> u32 {
    input
        .lines()
        .map(|line| {
            let game = Game::new(line);
            game.max_red * game.max_green * game.max_blue
        })
        .sum()
}

fn main() {
    let file_contents = vec![include_str!("example"), include_str!("input")];
    advent2023::calculate_and_print(&file_contents, part1, part2);
}

#[cfg(test)]
mod day02 {
    use super::*;

    #[test]
    fn test_part1() {
        assert!(part1(include_str!("example")) == 8);
        assert!(part1(include_str!("input")) == 2085);
    }

    #[test]
    fn test_part2() {
        assert!(part2(include_str!("example")) == 2286);
        assert!(part2(include_str!("input")) == 79315);
    }
}
