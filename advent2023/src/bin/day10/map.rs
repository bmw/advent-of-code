use std::collections::HashMap;
use std::ops::{Add, Index};

pub struct Map<'a> {
    map: MapType<'a>,
    start: Point,
}

impl<'a> Map<'a> {
    pub fn new(map: &'a str) -> Self {
        let map = map.lines().map(|s| s.as_bytes()).collect();
        let start = find_start(&map);
        Map { map, start }
    }

    pub fn track_cycle(&self) -> Vec<Point> {
        let mut current = self.find_second_pipe();
        let mut path = vec![self.start];
        while current != self.start {
            let deltas = DELTAS.get(&self[current]).unwrap();
            let mut next = (current + deltas.0).unwrap();
            if next == *path.last().unwrap() {
                next = (current + deltas.1).unwrap();
            }
            path.push(current);
            current = next;
        }
        path
    }

    fn find_second_pipe(&self) -> Point {
        for delta in POSSIBLE_DIRECTIONS {
            if let Some(point) = self.start + delta {
                if let Some(deltas) = DELTAS.get(&self[point]) {
                    // flip the delta so it's going the other direction
                    let delta = Delta(-delta.0, -delta.1);
                    if delta == deltas.0 || delta == deltas.1 {
                        return point;
                    }
                }
            }
        }
        panic!("can't find the second pipe!");
    }
}

static START: u8 = b'S';
static POSSIBLE_DIRECTIONS: [Delta; 4] = [Delta(-1, 0), Delta(1, 0), Delta(0, -1), Delta(0, 1)];

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
struct Delta(i8, i8);
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub struct Point(u8, u8);
type MapType<'a> = Vec<&'a [u8]>;

lazy_static! {
    static ref DELTAS: HashMap<u8, (Delta, Delta)> = HashMap::from([
        (b'|', (Delta(-1, 0), Delta(1, 0))),
        (b'-', (Delta(0, 1), Delta(0, -1))),
        (b'L', (Delta(-1, 0), Delta(0, 1))),
        (b'J', (Delta(-1, 0), Delta(0, -1))),
        (b'7', (Delta(1, 0), Delta(0, -1))),
        (b'F', (Delta(1, 0), Delta(0, 1))),
    ]);
}

fn find_start(map: &MapType) -> Point {
    for (i, row) in map.iter().enumerate() {
        for (j, value) in row.iter().enumerate() {
            if *value == START {
                return Point(i.try_into().unwrap(), j.try_into().unwrap());
            }
        }
    }
    panic!("i can't find the start!");
}

impl Add<Delta> for Point {
    type Output = Option<Self>;

    fn add(self, other: Delta) -> Self::Output {
        let x = self.0.checked_add_signed(other.0);
        let y = self.1.checked_add_signed(other.1);
        match (x, y) {
            (Some(x), Some(y)) => Some(Point(x, y)),
            _ => None,
        }
    }
}

impl Index<Point> for Map<'_> {
    type Output = u8;

    fn index(&self, index: Point) -> &Self::Output {
        let Point(x, y) = index;
        &self.map[x as usize][y as usize]
    }
}
