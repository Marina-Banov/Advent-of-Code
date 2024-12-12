use std::io::{BufRead, BufReader};
use std::fs::File;
use itertools::Itertools;

fn gen_combinations(chars: &str, length: usize) -> impl Iterator<Item = String> + '_ {
    std::iter::repeat_with(|| chars.chars())
        .take(length)
        .multi_cartesian_product()
        .map(|comb| comb.into_iter().collect())
}


fn parse_line(line: String) -> (i64, Vec<i64>) {
    let split: Vec<&str> = line.split(": ").collect();
    (
        split[0].parse::<i64>().unwrap(),
        split[1].split_whitespace().map(|p| p.parse::<i64>().unwrap()).collect()
    )
}

fn eval(test_value: i64, numbers: &Vec<i64>, operators: String) -> bool {
    let mut res = numbers[0];
    for i in 0..operators.len() {
        match operators.chars().nth(i).unwrap() {
            '*' => res *= numbers[i+1],
            '+' => res += numbers[i+1],
            '|' => {
                let n_digits = (numbers[i+1] as f64).log10().floor() as u32 + 1;
                res = res * 10_i64.pow(n_digits) + numbers[i+1];
            },
            _ => {}
        }
    }
    res == test_value
}

fn part_one(test_value: i64, numbers: Vec<i64>) -> i64 {
    for operators in gen_combinations("+*", numbers.len()-1).into_iter() {
        if eval(test_value, &numbers, operators) {
            return test_value;
        }
    }
    0
}

fn part_two(test_value: i64, numbers: Vec<i64>) -> i64 {
    for operators in gen_combinations("+*|", numbers.len()-1).into_iter() {
        if eval(test_value, &numbers, operators) {
            return test_value;
        }
    }
    0
}

fn main_fn(res: &dyn Fn(i64, Vec<i64>) -> i64) -> i64 {
    let reader: BufReader<File> = BufReader::new(File::open("input").expect("Could not open file"));
    reader.lines().flatten().map(|line| {
        let (test_value, numbers) = parse_line(line);
        res(test_value, numbers)
    }).sum()
}

fn main() {
    println!("{}", main_fn(&part_one));
    println!("{}", main_fn(&part_two));
}
