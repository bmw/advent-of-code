use std::cmp::min;

const PERIOD_AS_U8: u8 = ".".as_bytes()[0];

fn build_grid(input: &str) -> Vec<&[u8]> {
    input.lines().map(|line| line.as_bytes()).collect()
}

fn num_borders_symbol(input: &[&[u8]], row_index: usize, col_start: usize, col_end: usize) -> bool {
    let row_start = row_index.saturating_sub(1);
    let row_end = min(row_index + 2, input.len());
    let col_start = col_start.saturating_sub(1);
    (row_start..row_end)
        .flat_map(|i| {
            let col_end = min(col_end + 1, input[i].len());
            (col_start..col_end).map(move |j| (i, j))
        })
        .any(|(i, j)| {
            let byte = input[i][j];
            !byte.is_ascii_digit() && byte != PERIOD_AS_U8
        })
}

fn part1(input: &str) -> u32 {
    let input = build_grid(input);
    input.iter().enumerate().fold(0, |mut acc, (i, row)| {
        let mut iter = 0..row.len();
        while let Some(start) = iter.find(|&j| row[j].is_ascii_digit()) {
            let end = iter
                .find(|&j| !row[j].is_ascii_digit())
                .unwrap_or(row.len());
            if num_borders_symbol(&input, i, start, end) {
                acc += std::str::from_utf8(&row[start..end])
                    .unwrap()
                    .parse::<u32>()
                    .unwrap();
            }
        }
        acc
    })
}

fn part2(input: &str) -> u32 {
    let _input = build_grid(input);
    42
}

fn main() {
    let file_contents = vec![include_str!("example"), include_str!("input")];
    advent2023::calculate_and_print(&file_contents, part1, part2);
}

#[cfg(test)]
mod day03 {
    use super::*;

    #[test]
    fn test_part1() {
        assert_eq!(part1(include_str!("example")), 4361);
        assert_eq!(part1(include_str!("input")), 544664);
    }

    //#[test]
    //fn test_part2() {
    //    assert!(part2(include_str!("example2")) == 281);
    //    assert!(part2(include_str!("input")) == 54770);
    //}
}
