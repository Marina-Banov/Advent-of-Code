use std::cmp::min;
use std::collections::{HashMap, HashSet};
use std::io::{BufRead, BufReader};
use std::fs::File;
use std::ops;
use itertools::Itertools;

#[derive(Copy, Clone, Debug, Eq, Hash, PartialEq)]
struct Point(isize, isize);

impl ops::Add for Point {
    type Output = Self;

    fn add(self, other: Self) -> Self::Output {
        Point(self.0 + other.0, self.1 + other.1)
    }
}

impl ops::Sub for Point {
    type Output = Self;

    fn sub(self, other: Self) -> Self::Output {
        Point(self.0 - other.0, self.1 - other.1)
    }
}

fn calculate_max_steps(a: Point, diff: Point, n_rows: usize, n_cols: usize) -> (isize, isize) {
    let steps_up = a.0 / diff.0.abs();
    let steps_down = (n_rows as isize-a.0-1) / diff.0.abs();
    let steps_left = a.1 / diff.1.abs();
    let steps_right = (n_cols as isize-a.1-1) / diff.1.abs();
    if diff.0 * diff.1 > 0 {
        return (min(steps_up, steps_left), min(steps_down, steps_right));
    }
    (min(steps_up, steps_right), min(steps_down, steps_left))
}

fn in_bounds(i: isize, j: isize, n_rows: usize, n_cols: usize) -> bool {
    i >= 0 && j >= 0 && (i as usize) < n_rows && (j as usize) < n_cols
}

fn part_one(frequencies: HashMap<char, Vec<Point>>, n_rows: usize, n_cols: usize) -> usize {
    let mut antinodes: HashSet<Point> = HashSet::new();
    for points in frequencies.values() {
        for pair in points.iter().combinations(2) {
            let a = *pair[0];
            let b = *pair[1];
            let diff = b - a;
            antinodes.insert(a - diff);
            antinodes.insert(b + diff);
        }
    }
    antinodes.iter().filter(|p| in_bounds(p.0, p.1, n_rows, n_cols)).count()
}

fn part_two(frequencies: HashMap<char, Vec<Point>>, n_rows: usize, n_cols: usize) -> usize {
    let mut antinodes: HashSet<Point> = HashSet::new();
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

fn main_fn(res: &dyn Fn(HashMap<char, Vec<Point>>, usize, usize) -> usize) -> usize {
    let reader: BufReader<File> = BufReader::new(File::open("input").expect("Could not open file"));
    let matrix: Vec<Vec<char>> = reader
        .lines()
        .map(|l| l.unwrap().chars().collect())
        .collect();
    let frequencies: HashMap<char, Vec<Point>> = matrix
        .iter()
        .enumerate()
        .flat_map(|(i, row)| {
            row.iter()
                .enumerate()
                .map(move |(j, &c)| (c, i as isize, j as isize))
        })
        .filter(|&(c, _, _)| c != '.')
        .fold(HashMap::new(), |mut acc, (c, i, j)| {
            acc.entry(c).or_insert_with(Vec::new).push(Point(i, j));
            acc
        });
    res(frequencies, matrix.len(), matrix[0].len())
}

fn main() {
    println!("{}", main_fn(&part_one));
    println!("{}", main_fn(&part_two));
}
