use std::fs::File;
use std::io::{BufRead, BufReader};
use pathfinding::prelude::bfs;
mod helpers;
use helpers::in_bounds;

fn traverse(bytes: &Vec<(isize, isize)>, n_rows: usize, n_cols: usize, n: usize) -> Option<Vec<(isize, isize)>> {
    bfs(
        &(0, 0),
        |&(x, y)| {
            [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
                .into_iter()
                .filter({
                    move |&(i, j)| {
                        let index = bytes.iter().position(|&el| el == (i, j));
                        in_bounds(i, j, n_rows, n_cols) && (index.is_none() || index.unwrap() > n)
                    }
                })
        },
        |&_end| _end == (n_rows as isize - 1, n_cols as isize - 1),
    )
}

fn part_one(bytes: &Vec<(isize, isize)>, n_rows: usize, n_cols: usize) -> String {
    (traverse(&bytes, n_rows, n_cols, 1023).unwrap().len() - 1).to_string()
}

fn part_two(bytes: &Vec<(isize, isize)>, n_rows: usize, n_cols: usize) -> String {
    let mut lo: usize = 0;
    let mut hi: usize = bytes.len() - 1;
    while hi > lo + 1 {
        let mid: usize = (hi + lo) / 2;
        if traverse(&bytes, n_rows, n_cols, mid).is_some() {
            lo = mid;
        } else {
            hi = mid;
        }
    }
    format!("{},{}", bytes[hi].1, bytes[hi].0).to_string()
}

fn main_fn(res: &dyn Fn(&Vec<(isize, isize)>, usize, usize) -> String) -> String {
    let reader: BufReader<File> = BufReader::new(File::open("input").unwrap());
    let n_rows: usize = 71;
    let n_cols: usize = 71;
    let bytes: Vec<(isize, isize)> = reader
        .lines()
        .flatten()
        .map(|line| {
            let split: Vec<&str> = line.split(",").collect();
            (split[1].parse::<isize>().unwrap(), split[0].parse::<isize>().unwrap())
        })
        .collect();
    res(&bytes, n_rows, n_cols)
}

fn main() {
    println!("{}", main_fn(&part_one));
    println!("{}", main_fn(&part_two));
}
