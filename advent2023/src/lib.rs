use std::fmt::Display;

pub type ByteGrid<'a> = Vec<&'a [u8]>;

struct Input<'a> {
    contents: &'a str,
    title: &'a str,
    run_part1: bool,
    run_part2: bool,
}

impl<'a> Input<'a> {
    /// This is based on my own usual workflow where I first get part 1 to work with an example, I
    /// solve part 1 for the real input, and then I make part 2 work with a possibly different
    /// example. In the case of two examples, it is assumed the first example is for part 1 and the
    /// second is for part 2.
    fn new(file_contents: &'a str, file_index: usize, file_count: usize) -> Input<'a> {
        assert!(file_count < 4);
        if file_index == 0 {
            Input {
                contents: file_contents,
                title: "example",
                run_part1: true,
                run_part2: file_count != 3,
            }
        } else if file_index + 1 == file_count {
            Input {
                contents: file_contents,
                title: "input",
                run_part1: true,
                run_part2: true,
            }
        } else {
            Input {
                contents: file_contents,
                title: "example2",
                run_part1: false,
                run_part2: true,
            }
        }
    }
}

pub fn calculate_and_print<A: Display, B: Display>(
    file_contents: &[&str],
    part1: fn(&str) -> A,
    part2: fn(&str) -> B,
) {
    let file_count = file_contents.len();
    let inputs: Vec<_> = file_contents
        .iter()
        .enumerate()
        .map(|(i, s)| Input::new(s, i, file_count))
        .collect();
    for input in inputs {
        if input.run_part1 {
            println!(
                "part 1 answer for {}: {}",
                input.title,
                part1(input.contents)
            );
        }
        if input.run_part2 {
            println!(
                "part 2 answer for {}: {}",
                input.title,
                part2(input.contents)
            );
        }
    }
}
