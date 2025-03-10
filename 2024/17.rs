use std::fs::File;
use std::io::{BufRead, BufReader, Lines};

fn get_next_line(lines: &mut Lines<BufReader<File>>) -> String {
    let line = lines.next().unwrap().unwrap();
    if !line.trim().is_empty() { line.split_whitespace().last().unwrap().to_string() } else { line }
}

fn part_one(mut a: u32, mut b: u32, mut c: u32, program: &Vec<u32>) -> String {
    let mut pointer: usize = 0;
    let mut s = String::new();
    while pointer < program.len() {
        let mut add = true;
        let instruction = program[pointer];
        let literal = program[pointer+1];
        let combo = if literal < 4 { literal } else { vec![a, b, c, 0][(literal % 4) as usize] };
        match instruction {
            0 => { a = a / 2_u32.pow(combo) }
            1 => { b = b ^ literal }
            2 => { b = combo % 8 }
            3 => { if a != 0 { pointer = literal as usize; add = false; } }
            4 => { b = b ^ c }
            5 => { s += &*format!("{},", combo % 8) }
            6 => { b = a / 2_u32.pow(combo) }
            _ => { c = a / 2_u32.pow(combo) }
        }
        if add {
            pointer += 2;
        }
    }
    s.pop().unwrap();
    s
}

fn part_two(_: u32, _: u32, _: u32, _: &Vec<u32>) -> String {
    0.to_string()
}

fn main_fn(res: &dyn Fn(u32, u32, u32, &Vec<u32>) -> String) -> String {
    let reader: BufReader<File> = BufReader::new(File::open("input").unwrap());
    let mut lines = reader.lines();
    let a: u32 = get_next_line(&mut lines).parse().unwrap();
    let b: u32 = get_next_line(&mut lines).parse().unwrap();
    let c: u32 = get_next_line(&mut lines).parse().unwrap();
    get_next_line(&mut lines);
    let program: Vec<u32> = get_next_line(&mut lines)
        .split(",")
        .map(|p| p.parse::<u32>().unwrap())
        .collect();
    res(a, b, c, &program)
}

fn main() {
    println!("{}", main_fn(&part_one));
    println!("{}", main_fn(&part_two));
}
