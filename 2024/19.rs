use std::fs::File;
use std::io::{BufRead, BufReader};
use memoize::memoize;

#[memoize]
fn word_break_backtrace(s: String, vec: Vec<String>, curr: String, start: usize) -> i64 {
    // https://www.geeksforgeeks.org/word-break-problem-using-backtracking/
    if start == s.len() {
        return 1;
    }
    let mut res = 0;
    for end in (start+1)..(s.len()+1) {
        let word = &s[start..end];
        if vec.contains(&word.to_string()) {
            res += word_break_backtrace(s.clone(), vec.clone(), format!("{curr}{word}"), end);
        }
    }
    res
}

fn part_one(s: String, vec: Vec<String>) -> i64 {
    (word_break_backtrace(s, vec, String::new(), 0) > 0) as i64
}

fn part_two(s: String, vec: Vec<String>) -> i64 {
    word_break_backtrace(s, vec, String::new(), 0)
}

fn main_fn(res: &dyn Fn(String, Vec<String>) -> i64) -> i64 {
    let reader: BufReader<File> = BufReader::new(File::open("input").unwrap());
    let mut vec: Vec<String> = Vec::new();
    let mut sum: i64 = 0;
    for line in reader.lines().flatten() {
        if vec.len() == 0 {
            vec = line.split(", ").map(|s| s.to_string()).collect();
        } else if !line.is_empty() {
            sum += res(line, vec.clone());
        }
    }
    sum
}

fn main() {
    println!("{}", main_fn(&part_one));
    println!("{}", main_fn(&part_two));
}
