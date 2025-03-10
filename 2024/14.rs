use std::fs::File;
use std::io::{BufRead, BufReader};
use itertools::Itertools;
use image::{ImageBuffer, Rgb, RgbImage};
use statrs::statistics::Statistics;
mod helpers;
use helpers::Point;

#[derive(Clone, Copy, Debug)]
struct Robot {
    position: Point<i32>,
    velocity: Point<i32>,
}

impl Robot {
    fn new(position: Point<i32>, velocity: Point<i32>) -> Self {
        Robot { position, velocity }
    }

    fn step(&mut self) {
        self.position.i = (self.position.i + self.velocity.i + WRAP.i) % WRAP.i;
        self.position.j = (self.position.j + self.velocity.j + WRAP.j) % WRAP.j;
    }
}

fn part_one(robots: &mut Vec<Robot>) -> i32 {
    for _ in 0..100 {
        robots.iter_mut().for_each(|robot| robot.step());
    }
    let half_wrap = Point::new(WRAP.i / 2, WRAP.j / 2);
    let mut quadrants = [0, 0, 0, 0];
    robots.iter().for_each(|robot| {
        if robot.position.i == half_wrap.i || robot.position.j == half_wrap.j {
            return;
        }
        let a = robot.position.i < half_wrap.i;
        let b = robot.position.j < half_wrap.j;
        quadrants[2 * (a as usize) + b as usize] += 1;
    });
    quadrants.iter().product()
}

fn part_two_on_drugs(robots: &mut Vec<Robot>) -> i32 {
    for i in 1..WRAP.i * WRAP.j {
        let mut image: RgbImage = ImageBuffer::new(WRAP.j as u32, WRAP.i as u32);
        robots.iter_mut().for_each(|robot| {
            robot.step();
            *image.get_pixel_mut(robot.position.j as u32, robot.position.i as u32) = Rgb([255,255,255]);
        });
        image.save(format!("day14ondrugs/{}.png", i)).unwrap();
    }
    0
}

fn part_two(robots: &mut Vec<Robot>) -> i32 {
    (0..WRAP.i * WRAP.j)
        .map(|_| {
            robots.iter_mut().for_each(|robot| robot.step());
            robots
                .iter()
                .map(|r| r.position.i as f64 + r.position.j as f64)
                .collect::<Vec<_>>()
                .as_slice()
                .std_dev()
        })
        .collect_vec()
        .iter()
        .enumerate()
        .min_by(|(_, a), (_, b)| a.partial_cmp(b).unwrap())
        .map(|(index, _)| index)
        .unwrap() as i32 + 1
}

const WRAP: Point<i32> = Point::new(103, 101);

fn main_fn(res: &dyn Fn(&mut Vec<Robot>) -> i32) -> i32 {
    let reader: BufReader<File> = BufReader::new(File::open("input").unwrap());
    let mut robots: Vec<Robot> = reader
        .lines()
        .map(|line| {
            let (position, velocity) = line
                .unwrap()
                .split_whitespace()
                .map(|s| {
                    let (y, x) = s[2..]
                        .split(',')
                        .map(|num| num.parse::<i32>().unwrap())
                        .collect_tuple()
                        .unwrap();
                    Point::new(x, y)
                })
                .collect_tuple()
                .unwrap();
            Robot::new(position, velocity)
        })
        .collect();
    res(&mut robots)
}

fn main() {
    println!("{}", main_fn(&part_one));
    println!("{}", main_fn(&part_two));
}
