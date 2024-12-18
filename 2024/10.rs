use std::io::{BufRead, BufReader};
use std::fs::File;
use itertools::iproduct;
use pathfinding::prelude::{count_paths, bfs};

fn in_bounds(i: isize, j: isize, n_rows: usize, n_cols: usize) -> bool {
    i >= 0 && j >= 0 && (i as usize) < n_rows && (j as usize) < n_cols
}

fn find_all(matrix: &Vec<Vec<u32>>, digit: u32) -> Vec<(isize, isize)> {
    matrix.iter()
        .enumerate()
        .flat_map(|(i, row)| row.iter().enumerate().map(move |(j, &c)| (i, j, c)))
        .filter(|&(_, _, c)| c == digit)
        .map(|(i, j, _)| (i as isize, j as isize))
        .collect::<Vec<(isize, isize)>>()
}

fn part_one(matrix: &Vec<Vec<u32>>, start: &(isize, isize), end: &(isize, isize)) -> i32 {
    let n_rows = matrix.len();
    let n_cols = matrix[0].len();
    bfs(
        start,
        |&(x, y)| {
            [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
                .into_iter()
                .filter(move |&(i, j)|
                    in_bounds(i, j, n_rows, n_cols) && matrix[i as usize][j as usize] == matrix[x as usize][y as usize] + 1
                )
        },
        |&_end| _end == *end,
    ).is_some() as i32
}

fn part_two(matrix: &Vec<Vec<u32>>, start: &(isize, isize), end: &(isize, isize)) -> i32 {
    let n_rows = matrix.len();
    let n_cols = matrix[0].len();
    count_paths(
        *start,
        |&(x, y)| {
            [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
                .into_iter()
                .filter(move |&(i, j)|
                    in_bounds(i, j, n_rows, n_cols) && matrix[i as usize][j as usize] == matrix[x as usize][y as usize] + 1
                )
        },
        |&_end| _end == *end,
    ) as i32
}

fn main_fn(res: &dyn Fn(&Vec<Vec<u32>>, &(isize, isize), &(isize, isize)) -> i32) -> i32 {
    let reader: BufReader<File> = BufReader::new(File::open("input").unwrap());
    let matrix: Vec<Vec<u32>> = reader
        .lines()
        .map(|l| l.unwrap().chars().map(|c| c.to_digit(10).unwrap()).collect())
        .collect();
    iproduct!(find_all(&matrix, 0), find_all(&matrix, 9))
        .map(|(start, end)| res(&matrix, &start, &end))
        .sum()
}

fn main() {
    println!("{}", main_fn(&part_one));
    println!("{}", main_fn(&part_two));
}
