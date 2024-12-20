use std::collections::HashMap;
use std::fs::File;
use std::io::Read;

fn part_one() -> i32 { 25 }

fn part_two() -> i32 { 75 }

fn main_fn(res: &dyn Fn() -> i32) -> u64 {
    let mut line: String = String::new();
    File::open("input").unwrap().read_to_string(&mut line).unwrap();
    let mut next_map: HashMap<u64, Vec<u64>> = HashMap::from([(0, vec![1])]);
    let mut counts: HashMap<u64, u64> = line.split_whitespace()
        .map(|s| s.parse::<u64>().unwrap())
        .fold(HashMap::new(), |mut acc, val| {
            *acc.entry(val).or_insert(0) += 1;
            acc
        });
    for _ in 0..res() {
        let mut new_counts: HashMap<u64, u64> = HashMap::new();
        for key in counts.keys() {
            if !next_map.contains_key(&key) {
                let n_digits = (*key as f64 + 0.1).log10().ceil() as usize;
                let splitter = 10_u64.pow((n_digits / 2) as u32);
                if n_digits % 2 == 0 {
                    next_map.insert(*key, vec![key / splitter, key % splitter]);
                } else {
                    next_map.insert(*key, vec![key * 2024]);
                }
            }
            for &next in next_map.get(&key).unwrap() {
                *new_counts.entry(next).or_insert(0) += counts[&key];
            }
        }
        counts = new_counts;
    }
    counts.values().sum()
}

fn main() {
    println!("{}", main_fn(&part_one));
    println!("{}", main_fn(&part_two));
}
