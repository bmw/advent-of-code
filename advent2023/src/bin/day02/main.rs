mod game;
use crate::game::Game;

fn part1(input: &str) -> u32 {
    input.lines().fold(0, |acc, line| {
        let game = Game::new(line);
        if game.max_red <= 12 && game.max_green <= 13 && game.max_blue <= 14 {
            acc + game.id
        } else {
            acc
        }
    })
}

fn main() {
    let file_contents = vec![
        include_str!("example"),
        include_str!("input"),
    ];
    advent2023::calculate_and_print(&file_contents, part1, part1);
}

#[cfg(test)]
mod day02 {
    use super::*;

    #[test]
    fn test_part1() {
        assert!(part1(include_str!("example")) == 8);
        assert!(part1(include_str!("input")) == 2085);
    }

    //#[test]
    //fn test_part2() {
    //}
}
