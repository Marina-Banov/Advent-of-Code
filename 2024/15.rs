use std::collections::HashMap;
use std::fs::File;
use std::io::{BufRead, BufReader};
use lazy_static::lazy_static;
mod helpers;
use helpers::{Point, get_element, set_element};

fn get_cur_pos(matrix: &mut Vec<Vec<char>>) -> Point<isize> {
    matrix.iter()
        .enumerate()
        .flat_map(|(i, row)| row.iter().enumerate().map(move |(j, &c)| (i, j, c)))
        .find(|&(_, _, c)| c == '@')
        .map(|(i, j, _)| Point::new(i as isize, j as isize))
        .unwrap()
}

fn part_one(matrix: &mut Vec<Vec<char>>, moves: &Vec<char>) -> char {
    let mut cur_pos = get_cur_pos(matrix);
    for m in moves.iter() {
        let new_pos = cur_pos + DIRS[m];
        match get_element(&matrix, new_pos) {
            '#' => continue,
            'O' => {
                let mut check_pos = new_pos;
                loop {
                    check_pos = check_pos + DIRS[m];
                    if get_element(&matrix, check_pos) != 'O' {
                        break;
                    }
                }
                if get_element(&matrix, check_pos) == '.' {
                    set_element(matrix, check_pos, 'O');
                } else {
                    continue;
                }
            },
            _ => {}
        }
        set_element(matrix, cur_pos, '.');
        set_element(matrix, new_pos, '@');
        cur_pos = new_pos;
    }
    'O'
}

fn part_two(matrix: &mut Vec<Vec<char>>, _moves: &Vec<char>) -> char {
    for row in matrix.iter_mut() {
        *row = row
            .iter()
            .flat_map(|ch| match ch {
                '.' => vec!['.', '.'],
                '#' => vec!['#', '#'],
                'O' => vec!['[', ']'],
                '@' => vec!['@', '.'],
                _ => vec![],
            })
            .collect();
    }
    // let mut cur_pos = get_cur_pos(matrix);
    '['
}

lazy_static! {
    static ref DIRS: HashMap<char, Point<isize>> = HashMap::from([
        ('^', Point::new(-1, 0)),
        ('<', Point::new(0, -1)),
        ('>', Point::new(0, 1)),
        ('v', Point::new(1, 0)),
    ]);
}

fn main_fn(res: &dyn Fn(&mut Vec<Vec<char>>, &Vec<char>) -> char) -> i32 {
    let reader: BufReader<File> = BufReader::new(File::open("input").unwrap());
    let mut matrix: Vec<Vec<char>> = Vec::new();
    let mut moves: Vec<char> = Vec::new();
    for line in reader.lines().flatten() {
        if matrix.len() == 0 || matrix.len() < matrix[0].len() {
            matrix.push(line.chars().collect());
        } else if !line.is_empty() {
            moves.extend(line.chars().collect::<Vec<_>>());
        }
    }
    let box_char = res(&mut matrix, &moves);
    matrix
        .iter()
        .enumerate()
        .flat_map(|(i, row)| row.iter().enumerate().map(move |(j, &c)| (i, j, c)))
        .filter(|&(_, _, c)| c == box_char)
        .map(|(i, j, _)| 100 * i as i32 + j as i32)
        .sum()
}

fn main() {
    println!("{}", main_fn(&part_one));
    println!("{}", main_fn(&part_two));
}
