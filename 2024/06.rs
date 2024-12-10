use std::collections::HashSet;
use std::io::{BufRead, BufReader};
use std::fs::File;

const DIRSX: [isize; 4] = [ 0, 1, 0, -1];
const DIRSY: [isize; 4] = [-1, 0, 1,  0];

fn in_bounds(i: isize, j: isize, n_rows: usize, n_cols: usize) -> bool {
    i >= 0 && j >= 0 && (i as usize) < n_rows && (j as usize) < n_cols
}

fn get_positions(traversed: &HashSet<(isize, isize, usize)>) -> HashSet<(isize, isize)> {
    traversed.into_iter().map(|(x, y, _)| (*x, *y)).collect()
}

fn traverse_once(
    matrix: &[Vec<char>],
    mut current_pose: (isize, isize),
    loop_detection: bool,
) -> (HashSet<(isize, isize, usize)>, bool) {
    let n_rows = matrix.len();
    let n_cols = matrix[0].len();
    let mut dir = 0;
    let mut di = DIRSY[dir];
    let mut dj = DIRSX[dir];
    let mut traversed: HashSet<(isize, isize, usize)> = HashSet::new();

    loop {
        traversed.insert((current_pose.0, current_pose.1, dir));
        let new_pose = (current_pose.0 + di, current_pose.1 + dj);
        if loop_detection && traversed.contains(&(new_pose.0, new_pose.1, dir)) {
            return (traversed, true);
        }
        if !in_bounds(new_pose.0, new_pose.1, n_rows, n_cols) {
            break;
        }
        if matrix[new_pose.0 as usize][new_pose.1 as usize] == '#' {
            dir = (dir + 1) % 4;
            di = DIRSY[dir];
            dj = DIRSX[dir];
            continue;
        }
        current_pose = new_pose;
    }

    (traversed, false)
}

fn part_one(
    _matrix: &mut Vec<Vec<char>>,
    traversed: HashSet<(isize, isize, usize)>,
    _initial_pose: (isize, isize)
) -> i32 {
    get_positions(&traversed).len() as i32
}

fn part_two(
    matrix: &mut Vec<Vec<char>>,
    traversed: HashSet<(isize, isize, usize)>,
    initial_pose: (isize, isize)
) -> i32 {
    let mut count = 0;
    for key in get_positions(&traversed) {
        if key == initial_pose {
            continue;
        }
        matrix[key.0 as usize][key.1 as usize] = '#';
        count += traverse_once(matrix, initial_pose, true).1 as i32;
        matrix[key.0 as usize][key.1 as usize] = '.';
    }
    count
}

fn main_fn(res: &dyn Fn(&mut Vec<Vec<char>>, HashSet<(isize, isize, usize)>, (isize, isize)) -> i32) -> i32 {
    let reader: BufReader<File> = BufReader::new(File::open("input").expect("Could not open file"));
    let matrix: Vec<Vec<char>> = reader
        .lines()
        .map(|l| l.unwrap().chars().collect())
        .collect();
    let initial_pose = matrix.iter()
        .enumerate()
        .flat_map(|(i, row)| row.iter().enumerate().map(move |(j, &c)| (i, j, c)))
        .find(|&(_, _, c)| c == '^')
        .map(|(i, j, _)| (i as isize, j as isize))
        .unwrap();
    let (traversed, _) = traverse_once(&matrix, initial_pose, false);
    res(&mut matrix.clone(), traversed, initial_pose)
}

fn main() {
    println!("{}", main_fn(&part_one));
    println!("{}", main_fn(&part_two));
}
