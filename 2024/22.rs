use std::collections::HashMap;
use std::fs::File;
use std::io::{BufRead, BufReader};
use itertools::{repeat_n, Itertools};
use circular_buffer::CircularBuffer;

fn mix_and_prune(n: u64, secret: u64) -> u64 {
    (n ^ secret) % 16777216
}

fn next_price(secret: u64) -> u64 {
    let mut n = secret;
    n = mix_and_prune(n * 64, n);
    n = mix_and_prune(n / 32, n);
    mix_and_prune(n * 2048, n)
}

fn part_one(secret_numbers: &Vec<u64>) -> u64 {
    secret_numbers
        .iter()
        .map(|&secret| {
            let mut s = secret;
            for _ in 0..2000 { s = next_price(s); }
            s
        })
        .sum()
}

fn part_two(secret_numbers: &Vec<u64>) -> u64 {
    let mut bananas: HashMap<String, u64> = repeat_n(-9..=9, 4)
        .multi_cartesian_product()
        .map(|p| (format!("{:?}", p), 0))
        .collect();
    for &secret in secret_numbers {
        let mut s = secret;
        let mut perms: HashMap<String, bool> = HashMap::new();
        let mut buf: CircularBuffer<4, i8> = CircularBuffer::new();
        for _ in 0..2000 {
            let prev = (s % 10) as i8;
            s = next_price(s);
            buf.push_back((s % 10) as i8 - prev);
            if buf.len() < 4 || s % 10 == 0 {
                continue;
            }
            let key = format!("{:?}", buf);
            if !perms.contains_key(&key) {
                *bananas.get_mut(&key).unwrap() += s % 10;
                perms.insert(key, true);
            }
        }
    }
    *bananas.values().max().unwrap()
}

fn main_fn(res: &dyn Fn(&Vec<u64>) -> u64) -> u64 {
    let reader: BufReader<File> = BufReader::new(File::open("input").unwrap());
    let secret_numbers: Vec<u64> = reader.lines().flatten().map(
        |line| line.parse().unwrap()
    ).collect();
    res(&secret_numbers)
}

fn main() {
    println!("{}", main_fn(&part_one));
    println!("{}", main_fn(&part_two));
}
