use std::fs::File;
use std::io::{BufRead, BufReader};

fn pair_fits(lock: &Vec<u8>, key: &Vec<u8>) -> bool {
    lock.iter().zip(key).map(|(l, k)| l+k).all(|slot| slot < 6)
}

fn part_one(locks: &Vec<Vec<u8>>, keys: &Vec<Vec<u8>>) -> i32 {
    locks.iter()
        .flat_map(|lock|
            keys.iter().map(move |key| (lock, key))
        )
        .filter(|(lock, key)| pair_fits(lock, key))
        .count() as i32
}

fn part_two(_locks: &Vec<Vec<u8>>, _keys: &Vec<Vec<u8>>) -> i32 {
    0
}

fn read_scheme(scheme: &Vec<Vec<char>>) -> Vec<u8> {
    let mut result: Vec<u8> = vec![0; 5];
    for i in 1..6 {
        for j in 0..5 {
            if scheme[i][j] == '#' {
                result[j] += 1;
            }
        }
    }
    result
}

fn main_fn(res: &dyn Fn(&Vec<Vec<u8>>, &Vec<Vec<u8>>) -> i32) -> i32 {
    let reader: BufReader<File> = BufReader::new(File::open("input").unwrap());
    let mut locks: Vec<Vec<u8>> = Vec::new();
    let mut keys: Vec<Vec<u8>> = Vec::new();
    let mut scheme: Vec<Vec<char>> = Vec::new();
    for line in reader.lines().flatten() {
        if !line.is_empty() {
            scheme.push(line.chars().collect());
        } else {
            if scheme[0].contains(&'#') {
                locks.push(read_scheme(&scheme));
            } else {
                keys.push(read_scheme(&scheme));
            }
            scheme = Vec::new();
        }
    }
    res(&locks, &keys)
}

fn main() {
    println!("{}", main_fn(&part_one));
    println!("{}", main_fn(&part_two));
}
