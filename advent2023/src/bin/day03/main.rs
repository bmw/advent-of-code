use std::cmp::min;
use std::collections::HashMap;
use std::ops::Range;
use std::str::from_utf8;

type ByteGrid<'a> = Vec<&'a [u8]>;

const PERIOD_AS_U8: u8 = ".".as_bytes()[0];
const GEAR_AS_U8: u8 = "*".as_bytes()[0];

fn build_grid(input: &str) -> ByteGrid {
    input.lines().map(|line| line.as_bytes()).collect()
}

fn find_number_indices(input: &ByteGrid) -> Vec<(usize, Range<usize>)> {
    input
        .iter()
        .enumerate()
        .flat_map(|(i, row)| {
            let mut iter = 0..row.len();
            let mut nums = Vec::new();
            while let Some(start) = iter.find(|&j| row[j].is_ascii_digit()) {
                let end = iter
                    .find(|&j| !row[j].is_ascii_digit())
                    .unwrap_or(row.len());
                nums.push((i, (start..end)));
            }
            nums
        })
        .collect()
}

fn get_border_indices(
    input: &[&[u8]],
    row_index: usize,
    col_start: usize,
    col_end: usize,
) -> Vec<(usize, usize)> {
    let row_start = row_index.saturating_sub(1);
    let row_end = min(row_index + 2, input.len());
    let col_start = col_start.saturating_sub(1);
    (row_start..row_end)
        .flat_map(|i| {
            let col_end = min(col_end + 1, input[i].len());
            (col_start..col_end).map(move |j| (i, j))
        })
        .collect()
}

fn has_border_symbol(input: &[&[u8]], row_index: usize, col_start: usize, col_end: usize) -> bool {
    let border = get_border_indices(input, row_index, col_start, col_end);
    border.into_iter().any(|(i, j)| {
        let byte = input[i][j];
        !byte.is_ascii_digit() && byte != PERIOD_AS_U8
    })
}

fn part1(input: &str) -> u32 {
    let input = build_grid(input);
    let number_indices = find_number_indices(&input);
    number_indices
        .into_iter()
        .filter_map(|(row, cols)| {
            if has_border_symbol(&input, row, cols.start, cols.end) {
                Some(
                    from_utf8(&input[row][cols])
                        .unwrap()
                        .parse::<u32>()
                        .unwrap(),
                )
            } else {
                None
            }
        })
        .sum()
}

fn get_border_gears(
    input: &[&[u8]],
    row_index: usize,
    col_start: usize,
    col_end: usize,
) -> Vec<(usize, usize)> {
    let border = get_border_indices(input, row_index, col_start, col_end);
    border
        .into_iter()
        .filter(|(i, j)| input[*i][*j] == GEAR_AS_U8)
        .collect()
}

fn part2(input: &str) -> u32 {
    let input = build_grid(input);
    let number_indices = find_number_indices(&input);
    let mut gear_nums: HashMap<(usize, usize), Vec<u32>> = HashMap::new();
    for (row, cols) in number_indices {
        let col_start = cols.start;
        let col_end = cols.end;
        let num = from_utf8(&input[row][cols]).unwrap().parse().unwrap();
        for indices in get_border_gears(&input, row, col_start, col_end) {
            gear_nums.entry(indices).or_default().push(num);
        }
    }
    gear_nums
        .values()
        .filter_map(|v| {
            if v.len() == 2 {
                Some(v.iter().product::<u32>())
            } else {
                None
            }
        })
        .sum()
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

    #[test]
    fn test_part2() {
        assert_eq!(part2(include_str!("example")), 467835);
        assert_eq!(part2(include_str!("input")), 84495585);
    }
}
