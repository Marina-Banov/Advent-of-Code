use std::cmp::Reverse;
use std::fs::File;
use std::io::Read;

#[derive(Clone, Copy, Debug)]
pub struct Block {
    id: i32,
    pos: u32,
    len: u32,
}

impl Block {
    pub fn add(&mut self, id: i32, pos: u32, len: u32) {
        self.id = id;
        self.pos = pos;
        self.len = len;
    }
}

fn get_layout_one(line: String) -> Vec<i32> {
    let mut layout: Vec<i32> = Vec::new();
    let mut flag = true;
    let mut id = 0;
    for c in line.chars() {
        let len = c.to_digit(10).unwrap();
        if flag {
            layout.extend(vec![id; len as usize]);
            id += 1;
        } else {
            layout.extend(vec![-1; len as usize]);
        }
        flag = !flag;
    }
    layout
}

fn compress_one(layout: &mut Vec<i32>) {
    for i in 0..layout.len() {
        if layout[i] != -1 {
            continue;
        }
        for j in (i..layout.len()).rev() {
            if layout[j] == -1 {
                continue;
            }
            layout[i] = layout[j];
            layout[j] = -1;
            break;
        }
    }
}

fn calculate_one(layout: &Vec<i32>) -> i64 {
    layout.iter()
        .take_while(|&&c| c != -1)
        .enumerate()
        .map(|(i, &c)| i as i64 * c as i64)
        .sum()
}

fn part_one(line: String) -> i64 {
    let mut layout = get_layout_one(line);
    compress_one(&mut layout);
    calculate_one(&layout)
}

fn get_layout_two(line: String) -> Vec<Block> {
    let mut layout: Vec<Block> = Vec::new();
    let mut flag = true;
    let mut id = 0;
    let mut pos: u32 = 0;
    for c in line.chars() {
        let len = c.to_digit(10).unwrap();
        if len > 0 {
            if flag {
                layout.push(Block { id, pos, len });
                id += 1;
            } else {
                layout.push(Block { id: -1, pos, len });
            }
            pos += len;
        }
        flag = !flag;
    }
    layout
}

fn compress_two(layout: &mut Vec<Block>) {
    let mut full: Vec<Block> = layout.iter().filter(|&&block| block.id != -1).cloned().collect();
    let mut free: Vec<Block> = layout.iter().filter(|&&block| block.id == -1).cloned().collect();
    full.sort_by_key(|block| Reverse(block.pos));
    free.sort_by_key(|block| block.pos);
    let mut counter: usize = 0;
    while counter < full.len() {
        let mut found_swap = false;
        let full_block = full[counter];
        for i in 0..free.len() {
            let free_block = free[i];
            if free_block.pos > full_block.pos {
                break;
            }
            if full_block.len == free_block.len {
                full[counter].pos = free_block.pos;
                free[i].pos = full_block.pos;
                found_swap = true;
                break;
            }
            if full_block.len < free_block.len {
                full[counter].pos = free_block.pos;
                free[i].pos += full_block.len;
                free[i].len -= full_block.len;
                free.push(Block { id: -1, pos: full_block.pos, len: full_block.len});
                found_swap = true;
                break;
            }
        }
        if found_swap {
            full.sort_by_key(|block| Reverse(block.pos));
            free.sort_by_key(|block| block.pos);
        } else {
            counter += 1;
        }
    }
    layout.clear();
    layout.extend(full);
}

fn calculate_two(layout: &Vec<Block>) -> i64 {
    let mut res = 0;
    for block in layout {
        for i in 0..block.len {
            res += block.id as i64 * (block.pos + i) as i64;
        }
    }
    res
}

fn part_two(line: String) -> i64 {
    let mut layout = get_layout_two(line);
    compress_two(&mut layout);
    calculate_two(&layout)
}

fn main_fn(res: &dyn Fn(String) -> i64) -> i64 {
    let mut line: String = "".to_string();
    File::open("input").unwrap().read_to_string(&mut line).unwrap();
    res(line)
}

fn main() {
    println!("{}", main_fn(&part_one));
    println!("{}", main_fn(&part_two));
}
