use std::io::{BufRead, BufReader};
use std::fs::File;

const DIRSX: [isize; 8] = [-1, 1,  1, -1, -1,  0, 0, 1];
const DIRSY: [isize; 8] = [-1, 1, -1,  1,  0, -1, 1, 0];

fn in_bounds(i: isize, j: isize, n_rows: usize, n_cols: usize) -> bool {
    i >= 0 && j >= 0 && (i as usize) < n_rows && (j as usize) < n_cols
}

fn part_one(matrix: &Vec<Vec<char>>, i: usize, j: usize, n_rows: usize, n_cols: usize) -> i32 {
    if matrix[i][j] != 'X' {
        return 0;
    }
    let mut res = 0;
    for k in 0..8 {
        let di = DIRSY[k];
        let dj = DIRSX[k];
        if !in_bounds(i as isize + di * 3, j as isize + dj * 3, n_rows, n_cols) {
            continue;
        }
        let s: String = (0..4)
            .map(|c| matrix[(i as isize + di * c) as usize][(j as isize + dj * c) as usize])
            .collect();
        res += (s == "XMAS") as i32;
    }
    res
}

fn part_two(matrix: &Vec<Vec<char>>, i: usize, j: usize, n_rows: usize, n_cols: usize) -> i32 {
    if matrix[i][j] != 'A' {
        return 0;
    }
    let mut s = String::new();
    let mut matches = -1;
    for k in 0..4 {
        let di = DIRSY[k];
        let dj = DIRSX[k];
        if !in_bounds(i as isize + di, j as isize + dj, n_rows, n_cols) {
            return 0;
        }
        s.push(matrix[(i as isize + di) as usize][(j as isize + dj) as usize]);
        if s.len() == 2 {
            if s.contains('S') && s.contains('M') {
                matches += 1;
            }
            s.clear();
        }
    }
    matches.max(0)
}

fn main_fn(res: &dyn Fn(&Vec<Vec<char>>, usize, usize, usize, usize) -> i32) -> i32 {
    let reader: BufReader<File> = BufReader::new(File::open("input").expect("Could not open file"));
    let matrix: Vec<Vec<char>> = reader
        .lines()
        .map(|l| l.unwrap().chars().collect())
        .collect();
    let n_rows = matrix.len();
    let n_cols = matrix[0].len();
    let mut count = 0;
    for i in 0..n_rows {
        for j in 0..n_cols {
            count += res(&matrix, i, j, n_rows, n_cols);
        }
    }
    count
}

fn main() {
    println!("{}", main_fn(&part_one));
    println!("{}", main_fn(&part_two));
}
