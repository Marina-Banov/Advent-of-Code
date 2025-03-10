use std::io::Read;
use std::fs::File;
use regex::Regex;

fn multiply(mul: &String) -> i32 {
    let substring: String = mul.chars().skip(4).take(mul.len()-5).collect();
    let parts: Vec<i32> = substring.split(",").map(|p| p.parse::<i32>().unwrap()).collect();
    parts[0] * parts[1]
}

fn part_one(line: &str) -> Vec<String> {
    let re: Regex = Regex::new(r"mul\(\d+,\d+\)").unwrap();
    re.find_iter(line).map(|m| m.as_str().to_string()).collect()
}

fn part_two(line: &str) -> Vec<String> {
    let mut muls: Vec<String> = Vec::new();
    let mut should_add: bool = true;
    let re: Regex = Regex::new(r"do\(\)|don't\(\)|mul\(\d+,\d+\)").unwrap();
    for _match in re.find_iter(line).map(|m| m.as_str().to_string()) {
        if _match == "do()" {
            should_add = true;
            continue;
        }
        if _match == "don't()" {
            should_add = false;
        }
        if should_add {
            muls.push(_match);
        }
    }
    muls
}

fn main_fn(res: &dyn Fn(&str) -> Vec<String>) -> i32 {
    let mut line: String = "".to_string();
    File::open("input").unwrap().read_to_string(&mut line).expect("Could not read file");
    let muls: Vec<String> = res(&line);
    muls.iter().map(|m| multiply(m)).sum()
}

fn main() {
    println!("{}", main_fn(&part_one));
    println!("{}", main_fn(&part_two));
}
