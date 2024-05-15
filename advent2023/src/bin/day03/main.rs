const PERIOD_AS_U8: u8 = ".".as_bytes()[0];

fn num_borders_symbol(
    input: &[&[u8]],
    row_index: usize,
    mut col_start: usize,
    col_end: usize,
) -> bool {
    let row_start = row_index.saturating_sub(1);
    let row_end = row_index + 1;
    col_start = col_start.saturating_sub(1);
    (row_start..=row_end).any(|i| {
        input.get(i).map_or(false, |row| {
            (col_start..=col_end).any(|j| {
                row.get(j).map_or(false, |&byte| {
                    !byte.is_ascii_digit() && byte != PERIOD_AS_U8
                })
            })
        })
    })
}

fn sum_for_row(input: &[&[u8]], row_index: usize) -> u32 {
    let row = input[row_index];
    let mut iter = 0..row.len();
    let mut result = 0;
    while let Some(start) = iter.find(|&i| row[i].is_ascii_digit()) {
        let end = iter
            .find(|&i| !row[i].is_ascii_digit())
            .unwrap_or(row.len());
        if num_borders_symbol(input, row_index, start, end) {
            result += std::str::from_utf8(&row[start..end])
                .unwrap()
                .parse::<u32>()
                .unwrap();
        }
    }
    result
}

fn part1(input: &str) -> u32 {
    let input: Vec<_> = input.lines().map(|line| line.as_bytes()).collect();
    (0..input.len()).map(|i| sum_for_row(&input, i)).sum()
}

fn main() {
    let file_contents = vec![include_str!("example"), include_str!("input")];
    advent2023::calculate_and_print(&file_contents, part1, part1);
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
