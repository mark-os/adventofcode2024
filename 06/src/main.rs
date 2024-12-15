use std::fs;
use std::collections::HashSet;

mod walker;
use walker::MapWalker;

fn find_loop_positions(map: &Vec<Vec<char>>, initial_walker: &MapWalker) -> Vec<(usize, usize)> {
    let mut loop_positions = Vec::new();
    let visited_positions: HashSet<(usize, usize)> = initial_walker.get_visited_positions();

    for &(r, c) in visited_positions.iter() {
        if map[r][c] == '.' {
            // Create new map with test position as wall
            let mut test_map = map.clone();
            test_map[r][c] = '#';
            let walker = MapWalker::new(&test_map);

            // Test if this position creates a loop
            match walker.walk() {
                Ok(None) => loop_positions.push((r, c)), // Found a loop
                _ => continue, // Either got a count or error, skip it
            }
        }
    }
    loop_positions
}

fn main() {
    let contents = fs::read_to_string("input")
        .expect("Failed to read input file");
    
    let map: Vec<Vec<char>> = contents
        .lines()
        .filter(|line| !line.is_empty())
        .map(|line| line.chars().collect())
        .collect();

    // Part 1: Walk the map
    let walker = MapWalker::new(&map);
    match walker.walk() {
        Ok(Some(count)) => println!("Visited positions: {}", count),
        Ok(None) => println!("Found a loop!"),
        Err(e) => println!("Error: {}", e),
    }

    // Part 2: Find loop positions
    let loop_positions = find_loop_positions(&map, &walker);
    println!("Number of loop positions: {}", loop_positions.len());
}
