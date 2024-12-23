use std::collections::HashSet;
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::ops;
use pathfinding::prelude::connected_components;

#[derive(Copy, Clone, Debug, Eq, Hash, PartialEq)]
struct Point(isize, isize);

impl Point {
    const fn new(x: isize, y: isize) -> Point {
        Self(x, y)
    }

    fn get_char(&self, matrix: &Vec<Vec<char>>) -> char {
        matrix[self.0 as usize][self.1 as usize]
    }
}

impl ops::Add for Point {
    type Output = Self;

    fn add(self, other: Self) -> Self::Output {
        Point::new(self.0 + other.0, self.1 + other.1)
    }
}

const NORTH: Point = Point::new(-1, 0);
const SOUTH: Point = Point::new(1, 0);
const EAST: Point = Point::new(0, 1);
const WEST: Point = Point::new(0, -1);

fn add_padding(matrix: Vec<Vec<char>>) -> Vec<Vec<char>> {
    let n_cols: usize = matrix[0].len();
    let mut padded_matrix: Vec<Vec<char>> = matrix.into_iter()
        .map(|mut row| {
            row.insert(0, '.');
            row.push('.');
            row
        })
        .collect::<Vec<Vec<char>>>();
    padded_matrix.insert(0, vec!['.'; n_cols + 2]);
    padded_matrix.push(vec!['.'; n_cols + 2]);
    padded_matrix
}

fn part_one(region: &HashSet<Point>, matrix: &Vec<Vec<char>>) -> i32 {
    region
        .iter()
        .map(|&cell|
            [NORTH, SOUTH, EAST, WEST]
                .iter()
                .map(|&dir| cell+dir)
                .filter(|&neighbour| neighbour.get_char(matrix) != cell.get_char(matrix))
                .count() as i32
        )
        .sum()
}

fn part_two(region: &HashSet<Point>, matrix: &Vec<Vec<char>>) -> i32 {
    region
        .iter()
        .filter(|&&cell|
            [NORTH, SOUTH, EAST, WEST, NORTH+EAST, NORTH+WEST, SOUTH+EAST, SOUTH+WEST]
                .iter()
                .map(|&dir| cell+dir)
                .any(|neighbour| neighbour.get_char(matrix) != cell.get_char(matrix))
        )
        .map(|&outer_cell|
            is_corner(outer_cell, NORTH, EAST, matrix)
                + is_corner(outer_cell, NORTH, WEST, matrix)
                + is_corner(outer_cell, SOUTH, EAST, matrix)
                + is_corner(outer_cell, SOUTH, WEST, matrix)
        )
        .sum()
}

fn is_corner(cell: Point, dir_ns: Point, dir_ew: Point, matrix: &Vec<Vec<char>>) -> i32 {
    // https://www.reddit.com/r/adventofcode/comments/1hcpyic/comment/m1q437r
    let c: char = cell.get_char(matrix);
    let c_ns: char = (cell + dir_ns).get_char(matrix);
    let c_ew: char = (cell + dir_ew).get_char(matrix);
    let c_diagonal: char = (cell + dir_ns + dir_ew).get_char(matrix);
    ((c_ew != c && c_ns != c) || (c_diagonal != c && c_ew == c && c_ns == c)) as i32
}

fn main_fn(get_perimeter: &dyn Fn(&HashSet<Point>, &Vec<Vec<char>>) -> i32) -> i32 {
    let reader: BufReader<File> = BufReader::new(File::open("input").unwrap());
    let matrix: Vec<Vec<char>> = add_padding(
        reader.lines().map(|l| l.unwrap().chars().collect()).collect()
    );
    let n_rows: usize = matrix.len();
    let n_cols: usize = matrix[0].len();

    connected_components(
        &(1..n_rows as isize-1)
            .flat_map(|i| (1..n_cols as isize-1).map(move |j| Point::new(i, j)))
            .collect::<Vec<Point>>(),
        |&cell| {
            let m: &Vec<Vec<char>>  = &matrix;
            [NORTH, SOUTH, EAST, WEST]
                .iter()
                .map(move |&dir| cell + dir)
                .filter(move |&neighbour| neighbour.get_char(m) == cell.get_char(m))
        }
    )
        .iter()
        .map(|region| region.len() as i32 * get_perimeter(region, &matrix))
        .sum()
}

fn main() {
    println!("{}", main_fn(&part_one));
    println!("{}", main_fn(&part_two));
}
