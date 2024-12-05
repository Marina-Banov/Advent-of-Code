use std::io::{BufRead, BufReader};
use std::fs::File;

fn get_diffs(record: &Vec<i32>) -> Vec<i32> {
    let mut diffs: Vec<i32> = Vec::new();
    let mut prev = -1;
    for i in 0..record.len() {
        if prev != -1 {
            diffs.push(record[i] - prev);
        }
        prev = record[i];
    }
    diffs
}

fn part_one(diffs: &Vec<i32>) -> bool {
    diffs.iter().all(|&d| d > 0 && d <= 3) || diffs.iter().all(|&d| d < 0 && d >= -3)
}

fn part_two(diffs: &Vec<i32>) -> bool {
    if part_one(&diffs) {
        return true;
    }
    for i in 0..diffs.len() {
        let mut _diffs = diffs.clone();
        if i > 0 {
            _diffs[i-1] += _diffs[i];
        }
        _diffs.remove(i);
        if part_one(&_diffs) {
            return true;
        }
    }
    let mut _diffs = diffs.clone();
    _diffs.remove(diffs.len() - 1);
    part_one(&_diffs)
}

fn main_fn(is_safe: &dyn Fn(&Vec<i32>) -> bool) -> i32 {
    let reader: BufReader<File> = BufReader::new(File::open("input").expect("Could not open file"));
    let mut sum: i32 = 0;
    for line in reader.lines() {
        let line: String = line.expect("Could not read file");
        let line_split: Vec<&str> = line.split_whitespace().collect();
        let record: Vec<i32> = line_split.iter().map(|v| v.parse::<i32>().unwrap()).collect();
        let diffs: Vec<i32> = get_diffs(&record);
        sum += is_safe(&diffs) as i32;
    }
    sum
}

fn main() {
    println!("{}", main_fn(&part_one));
    println!("{}", main_fn(&part_two));
}
