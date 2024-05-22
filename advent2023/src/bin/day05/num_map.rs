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

#[derive(Clone, Copy, Debug, PartialEq)]
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
        let iter = second_map.overlapping_entries(first_dest, first_len);
        for entry in iter {
            let second_src = entry.src;
            let second_dest = entry.dest;
            let second_len = entry.len;
            // make merged map apply both maps in sequence
            let first_offset = second_src - first_dest;
            let overlap_len = min(second_len, first_len - first_offset);
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
        let old_end = old_src + old_result.len;
        let mut split_ranges = Vec::new();
        println!("considering {old_src} {old_result:?}");

        let iter = new_map.overlapping_entries(old_src, old_result.len);
        let iter = iter.collect::<Vec<_>>().into_iter().rev().collect::<Vec<_>>();
        for entry in iter {
            let new_src = entry.src;
            let new_len = entry.len;
            println!("found overlap {new_src} {new_len}");
            if old_src < new_src {
                split_ranges.push((old_src, old_dest, new_src - old_src));
            }
            let tmp = new_src + new_len;
            old_dest += tmp - old_src;
            old_src = tmp;
        }
        if old_src < old_end {
            split_ranges.push((old_src, old_dest, old_end - old_src));
        }
        println!("{split_ranges:?}");
        for (src, dest, len) in split_ranges {
            new_map.insert(src, dest, len);
        }
    }
}

impl NumMap {
    fn containing_entry(&self, value: u64) -> Option<(&u64, &MapResult)> {
        self.map.range(..=value).next_back().and_then(|v| {
            let (&range_src, &range_result) = v;
            if value >= range_src && value < range_src + range_result.len {
                Some(v)
            } else {
                None
            }
        })
    }

    pub fn insert(&mut self, src: u64, dest: u64, len: u64) {
        println!("inserting {src} {dest} {len} into {self:?}");
        assert!(self.overlapping_entries(src, len).next().is_none());
        self.map.insert(src, MapResult { dest, len });
    }

    pub fn iter(&self) -> impl Iterator<Item=MapEntry> + '_ {
        self.map.iter().map(|(&src, &MapResult { dest, len })| MapEntry { src, dest, len })
    }

    pub fn map_value(&self, value: u64) -> u64 {
        self.overlapping_entries(value, value + 1).next().map_or(value, |entry| {
            assert!(entry.src >= value && value < entry.src + entry.len);
            entry.dest + value - entry.src
        })
    }

    pub fn merged_maps(&self, other: &Self) -> Self {
        let mut merged_map = merge_overlap(self, other);
        merge_no_overlap(&mut merged_map, self);
        merge_no_overlap(&mut merged_map, other);
        merged_map
    }

    fn overlapping_entries(&self, value: u64, len: u64) -> impl Iterator<Item=MapEntry> + '_ {
        self.map.range(..value + len).rev().map_while(move |(&src, &entry)| {
            // src 50, entry len 48, pulled up because first less than, value 98
            if src <= value && value < src + entry.len {
                Some(MapEntry { src, dest: entry.dest, len: entry.len })
            } else {
                None
            }
        })
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
