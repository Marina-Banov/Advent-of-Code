use std::fs::File;
use std::io::{BufRead, BufReader};
use std::ops;
use itertools::Itertools;
use regex::Regex;

#[derive(Copy, Clone, Debug, Eq, Hash, PartialEq)]
struct Point(i64, i64);

impl Point {
    const fn new(x: i64, y: i64) -> Point {
        Self(x, y)
    }
}

impl ops::Add<i64> for Point {
    type Output = Self;

    fn add(self, scalar: i64) -> Self::Output {
        Point::new(self.0 + scalar, self.1 + scalar)
    }
}

fn get_point(re: &Regex, s: &String) -> Point {
    let pa: Vec<(i64, i64)> = re.find_iter(s).map(
        |m| m.as_str().parse::<i64>().unwrap()
    ).tuples().collect();
    Point::new(pa[0].0, pa[0].1)
}

fn part_one() -> i64 { 0 }

fn part_two() -> i64 { 10000000000000 }

fn main_fn(modifier: &dyn Fn() -> i64) -> i64 {
    let reader: BufReader<File> = BufReader::new(File::open("input").unwrap());
    let lines: Vec<String> = reader.lines().flatten().filter(|l| !l.is_empty()).collect();
    let re: Regex = Regex::new(r"\d+").unwrap();
    lines.chunks(3).map(|chunk| {
        let [button_a, button_b, prize] = chunk else { return 0; };
        let a0 = get_point(&re, &button_a);
        let a1 = get_point(&re, &button_b);
        let b = get_point(&re, &prize) + modifier();
        let det = a0.0 * a1.1 - a0.1 * a1.0;
        let x0 = a1.1 * b.0 - a1.0 * b.1;
        let x1 = a0.0 * b.1 - a0.1 * b.0;
        if x0 % det == 0 && x1 % det == 0 {
            return (3 * x0 + x1) / det;
        }
        0
    }).sum()
}

fn main() {
    println!("{}", main_fn(&part_one));
    println!("{}", main_fn(&part_two));
}
