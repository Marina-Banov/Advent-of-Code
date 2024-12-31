use std::cmp::min;
use std::collections::{HashMap, HashSet};
use std::io::{BufRead, BufReader};
use std::fs::File;
use itertools::Itertools;
mod helpers;
use helpers::{Point, in_bounds};

fn calculate_max_steps(a: Point<isize>, diff: Point<isize>, n_rows: usize, n_cols: usize) -> (isize, isize) {
    let steps_up = a.i / diff.i.abs();
    let steps_down = (n_rows as isize-a.i-1) / diff.i.abs();
    let steps_left = a.j / diff.j.abs();
    let steps_right = (n_cols as isize-a.j-1) / diff.j.abs();
    if diff.i * diff.j > 0 {
        return (min(steps_up, steps_left), min(steps_down, steps_right));
    }
    (min(steps_up, steps_right), min(steps_down, steps_left))
}

fn part_one(frequencies: HashMap<char, Vec<Point<isize>>>, n_rows: usize, n_cols: usize) -> usize {
    let mut antinodes: HashSet<Point<isize>> = HashSet::new();
    for points in frequencies.values() {
        for pair in points.iter().combinations(2) {
            let a = *pair[0];
            let b = *pair[1];
            let diff = b - a;
            antinodes.insert(a - diff);
            antinodes.insert(b + diff);
        }
    }
    antinodes.iter().filter(|p| in_bounds(p.i, p.j, n_rows, n_cols)).count()
}

fn part_two(frequencies: HashMap<char, Vec<Point<isize>>>, n_rows: usize, n_cols: usize) -> usize {
    let mut antinodes: HashSet<Point<isize>> = HashSet::new();
    for points in frequencies.values() {
        for pair in points.iter().combinations(2) {
            let mut a = *pair[0];
            let diff = *pair[1] - a;
            antinodes.insert(a);
            let (max_neg_steps, max_pos_steps) = calculate_max_steps(a, diff, n_rows, n_cols);
            for _ in 0..max_neg_steps {
                let sub = a - diff;
                antinodes.insert(sub);
                a = sub;
            }
            a = *pair[0];
            for _ in 0..max_pos_steps {
                let add = a + diff;
                antinodes.insert(add);
                a = add;
            }
        }
    }
    antinodes.iter().count()
}

fn main_fn(res: &dyn Fn(HashMap<char, Vec<Point<isize>>>, usize, usize) -> usize) -> usize {
    let reader: BufReader<File> = BufReader::new(File::open("input").expect("Could not open file"));
    let matrix: Vec<Vec<char>> = reader
        .lines()
        .map(|l| l.unwrap().chars().collect())
        .collect();
    let frequencies: HashMap<char, Vec<Point<isize>>> = matrix
        .iter()
        .enumerate()
        .flat_map(|(i, row)| {
            row.iter()
                .enumerate()
                .map(move |(j, &c)| (c, i as isize, j as isize))
        })
        .filter(|&(c, _, _)| c != '.')
        .fold(HashMap::new(), |mut acc, (c, i, j)| {
            acc.entry(c).or_insert_with(Vec::new).push(Point::new(i, j));
            acc
        });
    res(frequencies, matrix.len(), matrix[0].len())
}

fn main() {
    println!("{}", main_fn(&part_one));
    println!("{}", main_fn(&part_two));
}
