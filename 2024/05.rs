use std::cmp::Ordering;
use std::io::{BufRead, BufReader};
use std::fs::File;
use std::collections::HashMap;

fn is_sorted(rules: &HashMap<i32,Vec<i32>>, updates: &mut Vec<i32>) -> bool {
    updates.windows(2).all(|pair| {
        rules.get(&pair[0]).map_or(false, |values| values.contains(&pair[1]))
    })
}

fn part_one(rules: &HashMap<i32,Vec<i32>>, updates: &mut Vec<i32>) -> i32 {
    if is_sorted(rules, updates) { updates[updates.len()/2] } else { 0 }
}

fn part_two(rules: &HashMap<i32,Vec<i32>>, updates: &mut Vec<i32>) -> i32 {
    if is_sorted(rules, updates) {
        return 0
    }
    updates.sort_by(|a, b| {
        if rules.get(a).map_or(false, |values| values.contains(b)) {
            return Ordering::Less;
        }
        if rules.get(b).map_or(false, |values| values.contains(a)) {
            return Ordering::Greater;
        }
        Ordering::Equal
    });
    updates[updates.len()/2]
}

fn main_fn(res: &dyn Fn(&HashMap<i32,Vec<i32>>, &mut Vec<i32>) -> i32) -> i32 {
    let reader: BufReader<File> = BufReader::new(File::open("input").expect("Could not open file"));
    let mut rules: HashMap<i32,Vec<i32>> = HashMap::new();
    let mut updates: Vec<Vec<i32>> = Vec::new();
    let mut delimiter = '|';

    for line in reader.lines().flatten() {
        if line == "" {
            delimiter = ',';
            continue;
        }

        let vector: Vec<i32> = line
            .split(delimiter)
            .map(|p| p.parse::<i32>().unwrap())
            .collect();

        match delimiter {
            '|' => rules.entry(vector[0]).or_insert(Vec::new()).push(vector[1]),
            ',' => updates.push(vector),
            _ => {}
        }
    }

    updates.into_iter().map(|u| res(&rules, &mut u.clone())).sum()
}

fn main() {
    println!("{}", main_fn(&part_one));
    println!("{}", main_fn(&part_two));
}
