use std::fs::File;
use std::io::{BufRead, BufReader};
use itertools::Itertools;
use image::{ImageBuffer, Rgb, RgbImage};
use statrs::statistics::Statistics;

#[derive(Clone, Copy, Debug)]
struct Point {
    x: i32,
    y: i32,
}

impl Point {
    const fn new(x: i32, y: i32) -> Point {
        Point { x, y }
    }
}

#[derive(Clone, Copy, Debug)]
struct Robot {
    position: Point,
    velocity: Point,
}

impl Robot {
    fn new(position: Point, velocity: Point) -> Self {
        Robot { position, velocity }
    }

    fn step(&mut self) {
        self.position.x = (self.position.x + self.velocity.x + WRAP.x) % WRAP.x;
        self.position.y = (self.position.y + self.velocity.y + WRAP.y) % WRAP.y;
    }
}

fn part_one(robots: &mut Vec<Robot>) -> i32 {
    for _ in 0..100 {
        robots.iter_mut().for_each(|robot| robot.step());
    }
    let half_wrap = Point::new(WRAP.x / 2, WRAP.y / 2);
    let mut quadrants = [0, 0, 0, 0];
    robots.iter().for_each(|robot| {
        if robot.position.x == half_wrap.x || robot.position.y == half_wrap.y {
            return;
        }
        let a = robot.position.x < half_wrap.x;
        let b = robot.position.y < half_wrap.y;
        quadrants[2 * (a as usize) + b as usize] += 1;
    });
    quadrants.iter().product()
}

fn part_two_on_drugs(robots: &mut Vec<Robot>) -> i32 {
    for i in 1..WRAP.x * WRAP.y {
        let mut image: RgbImage = ImageBuffer::new(WRAP.y as u32, WRAP.x as u32);
        robots.iter_mut().for_each(|robot| {
            robot.step();
            *image.get_pixel_mut(robot.position.y as u32, robot.position.x as u32) = Rgb([255,255,255]);
        });
        image.save(format!("day14ondrugs/{}.png", i)).unwrap();
    }
    0
}

fn part_two(robots: &mut Vec<Robot>) -> i32 {
    (0..WRAP.x * WRAP.y)
        .map(|_| {
            robots.iter_mut().for_each(|robot| robot.step());
            robots
                .iter()
                .map(|r| r.position.x as f64 + r.position.y as f64)
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

const WRAP: Point = Point::new(103, 101);

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
