//1.create range from str and insert
//2.map num thru
//3.find out if two map ranges intersect
//4.merge new range to existing
//5.iterate over source ranges
//
//1. vec is O(n) insert while btree is olog(n)
//2. map is ologn in either case
//3.
use std::cmp::min;
use std::collections::BTreeMap;
use std::error;

#[derive(Clone, Copy, Debug)]
pub struct MapEntry {
    pub src: u64,
    pub dest: u64,
    pub len: u64,
}

#[derive(Clone, Copy, Debug)]
struct MapResult {
    dest: u64,
    len: u64,
}

#[derive(Clone, Debug, Default)]
pub struct NumMap {
    map: BTreeMap<u64, MapResult>,
}

fn merge_overlap(first_map: &NumMap, second_map: &NumMap) -> NumMap {
    let mut merged_map = NumMap::default();
    // iterate over the first map to be applied
    for (&first_src, &first_result) in &first_map.map {
        let first_dest = first_result.dest;
        let first_len = first_result.len;
        // find the ranges in the second map that applies to the first's output
        let mut iter = second_map.map.range(first_dest..first_dest + first_len);
        for (&second_src, &second_result) in iter {
            // make merged map apply both maps in sequence
            let first_offset = second_src - first_dest;
            let second_dest = second_result.dest;
            let overlap_len = min(second_result.len, first_len - first_offset);
            merged_map.insert(
                first_src + first_offset,
                second_dest,
                overlap_len,
            )
        }
    }
    merged_map
}

fn merge_no_overlap(new_map: &mut NumMap, old_map: &NumMap) {
    for (&old_src, &old_result) in &old_map.map {
        let mut old_src = old_src;
        let mut old_dest = old_result.dest;
        let mut split_ranges = Vec::new();

        let mut iter = new_map.map.range(old_src..old_src + old_result.len);
        for (&new_src, &new_result) in iter {
            if old_src < new_src {
                let tmp = new_src + new_result.len;
                split_ranges.push((old_src, old_dest, new_src - old_src));
                old_dest += tmp - old_src;
                old_src = tmp;
            }
        }
        for (src, dest, len) in split_ranges {
            new_map.insert(src, dest, len);
        }
    }
}

impl NumMap {
    fn containing_entry(&self, src: u64) -> Option<(&u64, &MapResult)> {
        self.map.range(..=src).next_back()
    }

    pub fn insert(&mut self, src: u64, dest: u64, len: u64) {
        println!("{:?}", self.containing_entry(src));
        assert!(self.containing_entry(src).is_none());
        self.map.insert(src, MapResult { dest, len });
    }

    pub fn iter(&self) -> impl Iterator<Item=MapEntry> + '_ {
        self.map.iter().map(|(&src, &MapResult { dest, len })| MapEntry { src, dest, len })
    }

    pub fn map_value(&self, src: u64) -> u64 {
        if let Some((&range_src, range_result)) = self.containing_entry(src) {
            if src < range_src + range_result.len {
                let offset = src - range_src;
                return range_result.dest + offset;
            }
        }
        src
    }

    pub fn merged_maps(&self, other: &Self) -> Self {
        let mut merged_map = merge_overlap(self, other);
        merge_no_overlap(&mut merged_map, self);
        merge_no_overlap(&mut merged_map, other);
        merged_map
    }
}

/// This is specific to day 5, but since it's my only need for this right now...
impl TryFrom<&Vec<&str>> for NumMap {
    type Error = Box<dyn error::Error>;
    fn try_from(lines: &Vec<&str>) -> Result<Self, Self::Error> {
        let mut map = NumMap::default();
        for line in lines {
            let mut values = Vec::new();
            for i in line.split_whitespace() {
                values.push(i.parse()?);
            }
            map.insert(values[1], values[0], values[2]);
        }
        Ok(map)
    }
}
