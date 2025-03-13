use std::collections::HashMap;
use std::fs::File;
use std::io::{BufRead, BufReader};
use itertools::Itertools;

fn part_one(wires: &mut HashMap<String, bool>, gates: &Vec<Vec<String>>) -> String {
    let mut done = false;
    while !done {
        done = true;
        for gate in gates {
            if !wires.contains_key(&gate[0]) || !wires.contains_key(&gate[2]) {
                done = false;
                continue;
            }
            let a = wires.get(&gate[0]).unwrap().clone();
            let b = wires.get(&gate[2]).unwrap().clone();
            wires.insert(gate[4].clone(), match gate[1].as_str() {
                "AND" => a & b,
                "OR" => a | b,
                _ => a ^ b,
            });
        }
    }
    wires.iter()
        .filter(|(k, _)| k.starts_with("z"))
        .sorted_by(|a, b| a.0.cmp(&b.0))
        .enumerate()
        .map(|(i, (_, &v))| if v { 2_u64.pow(i as u32) } else { 0 })
        .sum::<u64>()
        .to_string()
}

fn part_two(_wires: &mut HashMap<String, bool>, _gates: &Vec<Vec<String>>) -> String {
    "".to_string()
}

fn main_fn(res: &dyn Fn(&mut HashMap<String, bool>, &Vec<Vec<String>>) -> String) -> String {
    let reader: BufReader<File> = BufReader::new(File::open("input").unwrap());
    let mut wires: HashMap<String, bool> = HashMap::new();
    let mut gates: Vec<Vec<String>> = Vec::new();
    let mut inputs = true;
    for line in reader.lines().flatten() {
        if line.is_empty() {
            inputs = false;
            continue;
        }
        if inputs {
            let (key, value) = line.split(": ").map(|s| s.to_string()).collect_tuple().unwrap();
            wires.insert(key, value.parse::<u8>().unwrap() != 0);
        } else {
            gates.push(line.split_whitespace().map(|s| s.to_string()).collect());
        }
    }
    res(&mut wires, &gates)
}

fn main() {
    println!("{}", main_fn(&part_one));
    println!("{}", main_fn(&part_two));
}
