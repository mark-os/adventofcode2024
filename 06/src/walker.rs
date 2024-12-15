use std::collections::HashSet;

pub struct MapWalker {
    map: Vec<Vec<char>>,
    height: usize,
    width: usize,
    start_pos: (usize, usize),
    visited_states: HashSet<(usize, usize, char)>,
}

impl MapWalker {
    const DIRECTIONS: [(i32, i32); 4] = [(-1, 0), (0, 1), (1, 0), (0, -1)];

    pub fn new(map: &Vec<Vec<char>>) -> Self {
        let height = map.len();
        let width = map[0].len();
        let start_pos = Self::find_start(map);
        
        MapWalker {
            map: map.clone(),
            height,
            width,
            start_pos,
            visited_states: HashSet::new(),
        }
    }

    fn find_start(map: &Vec<Vec<char>>) -> (usize, usize) {
        for (r, row) in map.iter().enumerate() {
            for (c, &ch) in row.iter().enumerate() {
                if "^>v<".contains(ch) {
                    return (r, c);
                }
            }
        }
        panic!("No start position found");
    }

    fn get_next_position(&self, curr_row: usize, curr_col: usize, curr_dir: char) 
        -> (Option<(usize, usize)>, char, bool, bool) 
    {
        let (dr, dc) = match curr_dir {
            '^' => Self::DIRECTIONS[0],
            '>' => Self::DIRECTIONS[1],
            'v' => Self::DIRECTIONS[2],
            '<' => Self::DIRECTIONS[3],
            _ => panic!("Invalid direction"),
        };

        let next_row = curr_row as i32 + dr;
        let next_col = curr_col as i32 + dc;

        // Check boundaries
        if next_row < 0 || next_row >= self.height as i32 || 
           next_col < 0 || next_col >= self.width as i32 {
            return (None, curr_dir, false, true);
        }

        let next_row = next_row as usize;
        let next_col = next_col as usize;

        // Check for wall
        if self.map[next_row][next_col] == '#' {
            let next_dir = match curr_dir {
                '<' => '^',
                '^' => '>',
                '>' => 'v',
                'v' => '<',
                _ => panic!("Invalid direction"),
            };
            return (Some((curr_row, curr_col)), next_dir, true, false);
        }

        (Some((next_row, next_col)), curr_dir, false, false)
    }

    pub fn walk(&mut self) -> Result<Option<usize>, String> {
        let mut curr_pos = self.start_pos;
        let mut curr_dir = self.map[curr_pos.0][curr_pos.1];
        self.visited_states.clear();
        let max_steps = self.height * self.width * 4;
        let mut steps = 0;

        while steps < max_steps {
            let state = (curr_pos.0, curr_pos.1, curr_dir);
            
            if self.visited_states.contains(&state) {
                return Ok(None);
            }
            
            self.visited_states.insert(state);
            
            let (next_pos, next_dir, hit_wall, out_of_bounds) = 
                self.get_next_position(curr_pos.0, curr_pos.1, curr_dir);
            
            if out_of_bounds {
                let unique_positions: HashSet<(usize, usize)> = 
                    self.visited_states.iter().map(|&(r, c, _)| (r, c)).collect();
                return Ok(Some(unique_positions.len()));
            }
            
            curr_dir = next_dir;
            if !hit_wall {
                curr_pos = next_pos.unwrap();
            }
            
            steps += 1;
        }
        
        Err(format!("Exceeded maximum steps ({})", max_steps))
    }

    pub fn get_visited_positions(&self) -> HashSet<(usize, usize)> {
        self.visited_states.iter().map(|&(r, c, _)| (r, c)).collect()
    }
}
