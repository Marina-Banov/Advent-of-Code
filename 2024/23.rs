use std::collections::{HashMap, HashSet};
use std::fs::File;
use std::io::{BufRead, BufReader};
use itertools::Itertools;

fn dfs(
    graph: &HashMap<String, HashSet<String>>,
    marked: &mut HashMap<String, bool>,
    n: usize,
    vert: &String, start: &String,
    path: &mut Vec<String>,
    cycles: &mut Vec<Vec<String>>,
) {
    path.push(vert.to_string());
    marked.insert(vert.to_string(), true);
    if n == 0 {
        marked.insert(vert.to_string(), false);
        if graph[vert].contains(start) {
            cycles.push(path.clone());
        }
        return;
    }
    for i in graph.keys() {
        if !marked[i] && graph[vert].contains(i) {
            dfs(graph, marked, n-1, i, start, path, cycles);
            path.pop();
        }
    }
    marked.insert(vert.to_string(), false);
}

fn part_one(graph: &HashMap<String, HashSet<String>>) -> String {
    // https://www.geeksforgeeks.org/cycles-of-length-n-in-an-undirected-and-connected-graph/
    let mut marked: HashMap<String, bool> = graph.keys()
        .map(|p| (p.to_string(), false))
        .collect();
    let n = 3;
    let mut cycles: Vec<Vec<String>> = Vec::new();
    for i in graph.keys() {
        dfs(graph, &mut marked, n-1, i, i, &mut Vec::new(), &mut cycles);
        marked.insert(i.to_string(), true);
    }
    (cycles.iter().filter(|&cycle| {
        cycle.iter().any(|s| s.starts_with("t"))
    }).count() as i32 / 2).to_string()
}

fn bron_kerbosch(
    graph: &HashMap<String, HashSet<String>>,
    r: &HashSet<String>,
    p: &mut HashSet<String>,
    x: &mut HashSet<String>,
    cliques: &mut Vec<Vec<String>>,
) {
    // https://rosettacode.org/wiki/Bron%E2%80%93Kerbosch_algorithm
    if p.is_empty() && x.is_empty() {
        if r.len() > 2 {
            let mut clique: Vec<String> = r.iter().cloned().collect();
            clique.sort();
            cliques.push(clique);
        }
        return;
    }
    if let Some(pivot_vertex) = p.union(x)
        .max_by_key(|v| graph.get(*v).map_or(0, |neighbors| neighbors.len()))
        .cloned() {
        let neighbors = graph.get(&pivot_vertex).cloned().unwrap_or_default();
        let candidates: Vec<String> = p.difference(&neighbors).cloned().collect();
        for v in candidates {
            let mut new_r = r.clone();
            new_r.insert(v.clone());
            let neighbors_v = graph.get(&v).cloned().unwrap_or_default();
            let mut new_p: HashSet<String> = p.intersection(&neighbors_v).cloned().collect();
            let mut new_x: HashSet<String> = x.intersection(&neighbors_v).cloned().collect();
            bron_kerbosch(graph, &new_r, &mut new_p, &mut new_x, cliques);
            p.remove(&v);
            x.insert(v);
        }
    }
}

fn part_two(graph: &HashMap<String, HashSet<String>>) -> String {
    let mut keys: HashSet<String> = graph.keys().cloned().collect();
    let mut cliques: Vec<Vec<String>> = Vec::new();
    bron_kerbosch(&graph, &HashSet::new(), &mut keys, &mut HashSet::new(), &mut cliques);
    cliques.iter().max_by_key(|&clique| clique.len()).unwrap().join(",")
}

fn main_fn(res: &dyn Fn(&HashMap<String, HashSet<String>>) -> String) -> String {
    let reader: BufReader<File> = BufReader::new(File::open("input").unwrap());
    let mut graph: HashMap<String, HashSet<String>> = HashMap::new();
    for line in reader.lines().flatten() {
        let (u, v) = line.split("-").collect_tuple().unwrap();
        graph.entry(u.to_string()).or_insert_with(HashSet::new).insert(v.to_string());
        graph.entry(v.to_string()).or_insert_with(HashSet::new).insert(u.to_string());
    }
    res(&graph)
}

fn main() {
    println!("{}", main_fn(&part_one));
    println!("{}", main_fn(&part_two));
}
