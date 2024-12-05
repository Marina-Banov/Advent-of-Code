use std::io::{BufRead, BufReader};
use std::fs::File;

fn part_one(va: &Vec<i32>, vb: &Vec<i32>) -> i32 {
    let mut sum: i32 = 0;
    for i in 0..va.len() {
        sum += (va[i] - vb[i]).abs();
    }
    sum
}

fn part_two(va: &Vec<i32>, vb: &Vec<i32>) -> i32 {
    let mut sum: i32 = 0;
    for i in 0..va.len() {
        sum += va[i] * vb.iter().filter(|&n| *n == va[i]).count() as i32;
    }
    sum
}

fn main_fn(res: &dyn Fn(&Vec<i32>, &Vec<i32>) -> i32) -> i32 {
    let reader: BufReader<File> = BufReader::new(File::open("input").expect("Could not open file"));
    let mut va: Vec<i32> = Vec::new();
    let mut vb: Vec<i32> = Vec::new();
    for line in reader.lines() {
        let line: String = line.expect("Could not read file");
        let line_split: Vec<&str> = line.split_whitespace().collect();
        va.push(line_split[0].parse::<i32>().unwrap());
        vb.push(line_split[1].parse::<i32>().unwrap());
    }
    va.sort();
    vb.sort();
    res(&va, &vb)
}

fn main() {
    println!("{}", main_fn(&part_one));
    println!("{}", main_fn(&part_two));
}
