const EMPTY_SPACE: u8 = b'.';

type Image = Vec<Vec<u8>>;

fn main() {
    let file_contents = vec![include_str!("example"), include_str!("input")];
    advent2023::calculate_and_print(&file_contents, part1, part1);
}

fn part1(input: &str) -> usize {
    sum_distances_between(find_galaxies(build_image(input)))
}

fn build_image(input: &str) -> Image {
    let mut image: Vec<_> = input.lines().map(|s| Vec::from(s.as_bytes())).collect();

    // expand columns
    for i in (0..image[0].len()).rev() {
        if image.iter().all(|row| row[i] == EMPTY_SPACE) {
            image.iter_mut().for_each(|row| row.insert(i, EMPTY_SPACE));
        }
    }

    // expand rows
    for i in (0..image.len()).rev() {
        if image[i].iter().all(|b| *b == EMPTY_SPACE) {
            image.insert(i, vec![EMPTY_SPACE; image[i].len()]);
        }
    }

    image
}

fn find_galaxies(image: Image) -> Vec<(usize, usize)> {
    let mut galaxies = vec![];
    for (i, row) in image.iter().enumerate() {
        galaxies.extend(row.iter().enumerate().filter_map(|(j, b)| {
            if *b != EMPTY_SPACE {
                Some((i, j))
            } else {
                None
            }
        }));
    }
    galaxies
}

fn sum_distances_between(galaxies: Vec<(usize, usize)>) -> usize {
    galaxies
        .iter()
        .enumerate()
        .map(|(i, (x1, y1))| {
            galaxies[i..]
                .iter()
                .map(|(x2, y2)| x2.abs_diff(*x1) + y2.abs_diff(*y1))
                .sum::<usize>()
        })
        .sum()
}

#[cfg(test)]
mod day11 {
    use super::*;

    #[test]
    fn test_part1() {
        assert_eq!(part1(include_str!("example")), 374);
        assert_eq!(part1(include_str!("input")), 9918828);
    }

    //#[test]
    //fn test_part2() {
    //    assert_eq!(part2(include_str!("example")), 2);
    //    assert_eq!(part2(include_str!("input")), 864);
    //}
}
