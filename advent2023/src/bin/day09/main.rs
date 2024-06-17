fn extrapolated_values(seq: &[i64]) -> (i64, i64) {
    if seq.iter().all(|&v| v == 0) {
        return (0, 0);
    }
    let new_seq: Vec<i64> = seq.windows(2).map(|w| w[1] - w[0]).collect();
    let (first, last) = extrapolated_values(&new_seq);
    (seq.first().unwrap() - first, seq.last().unwrap() + last)
}

fn extrapolated_sums(input: &str) -> (i64, i64) {
    input.lines().fold((0, 0), |(first_sum, last_sum), s| {
        let seq: Vec<i64> = s.split_whitespace().map(|i| i.parse().unwrap()).collect();
        let (first, last) = extrapolated_values(&seq);
        (first_sum + first, last_sum + last)
    })
}

fn part1(input: &str) -> i64 {
    extrapolated_sums(input).1
}

fn part2(input: &str) -> i64 {
    extrapolated_sums(input).0
}

fn main() {
    let file_contents = vec![include_str!("example"), include_str!("input")];
    advent2023::calculate_and_print(&file_contents, part1, part2);
}

#[cfg(test)]
mod day09 {
    use super::*;

    #[test]
    fn test_part1() {
        assert_eq!(part1(include_str!("example")), 114);
        assert_eq!(part1(include_str!("input")), 1647269739);
    }

    #[test]
    fn test_part2() {
        assert_eq!(part2(include_str!("example")), 2);
        assert_eq!(part2(include_str!("input")), 864);
    }
}
