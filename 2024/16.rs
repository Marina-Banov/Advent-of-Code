use std::fs::File;
use std::io::{BufRead, BufReader};
use pathfinding::prelude::dijkstra;
mod helpers;
use helpers::{Point, get_element};

#[derive(Clone, Copy, Debug, Eq, Hash, PartialEq)]
struct Step {
    position: Point<isize>,
    velocity: Point<isize>,
}

impl Step {
    fn new(position: Point<isize>, velocity: Point<isize>) -> Step {
        Step { position, velocity }
    }
}

fn get_step(matrix: &Vec<Vec<char>>, pattern: char) -> Step {
    let position = matrix.iter()
        .enumerate()
        .flat_map(|(i, row)| row.iter().enumerate().map(move |(j, &c)| (i, j, c)))
        .find(|&(_, _, c)| c == pattern)
        .map(|(i, j, _)| Point::new(i as isize, j as isize))
        .unwrap();
    Step::new(position, Point::new(0, 1))
}

fn part_one(start: Step, matrix: &Vec<Vec<char>>, end: Step) -> i32 {
    dijkstra(
        &start,
        |&s| {
            DIRS.into_iter()
                .map(move |vel| Step::new(s.position + vel, vel))
                .filter({
                    let m = matrix.clone();
                    move |&neighbour| get_element(&m, neighbour.position) != '#'
                })
                .into_iter()
                .map(move |new_s| (new_s, if s.velocity == new_s.velocity { 1 } else { 1001 }))
        },
        |&_end| _end.position == end.position,
    ).unwrap().1
}

fn part_two(_start: Step, _matrix: &Vec<Vec<char>>, _end: Step) -> i32 {
    0
}

const DIRS: [Point<isize>; 4] = [
    Point::new(1, 0),
    Point::new(0, 1),
    Point::new(-1, 0),
    Point::new(0, -1)
];

fn main_fn(res: &dyn Fn(Step, &Vec<Vec<char>>, Step) -> i32) -> i32 {
    let reader: BufReader<File> = BufReader::new(File::open("input").unwrap());
    let matrix: Vec<Vec<char>> = reader
        .lines()
        .map(|l| l.unwrap().chars().collect())
        .collect();
    let start = get_step(&matrix, 'S');
    let end = get_step(&matrix, 'E');
    res(start, &matrix, end)
}

fn main() {
    println!("{}", main_fn(&part_one));
    println!("{}", main_fn(&part_two));
}
