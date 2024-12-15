class MapWalker:
    DIRECTIONS = {
        '^': (-1, 0),  # up
        '>': (0, 1),   # right
        'v': (1, 0),   # down
        '<': (0, -1)   # left
    }
    
    TURN_RIGHT = {'<': '^', '^': '>', '>': 'v', 'v': '<'}

    def get_next_position(self, curr_row, curr_col, curr_dir):
        """Returns (next_row, next_col, next_dir, hit_wall, out_of_bounds)"""
        dr, dc = self.DIRECTIONS[curr_dir]
        next_row = curr_row + dr
        next_col = curr_col + dc
        
        # Check boundaries first
        if next_row < 0 or next_row >= self.height or next_col < 0 or next_col >= self.width:
            return next_row, next_col, curr_dir, False, True
            
        # Check for wall
        if self.map[next_row][next_col] == '#':
            return curr_row, curr_col, self.TURN_RIGHT[curr_dir], True, False
            
        return next_row, next_col, curr_dir, False, False

    def __init__(self, themap):
        self.map = themap
        self.height = len(themap)
        self.width = len(themap[0])
        self.start_pos = self._find_start()
        self.visited_states = set()
        
    def _find_start(self):
        for r in range(self.height):
            for c in range(self.width):
                if self.map[r][c] in '^>v<':
                    return (r, c)
        raise ValueError("No start position found")



    def walk(self):
        """Walk the map from the starting position.
        
        Returns:
            False if a loop is detected (same state visited twice)
            int: number of unique positions visited if the walk exits the map
            
        Raises:
            RuntimeError: if maximum steps are exceeded
        """
        curr_row, curr_col = self.start_pos
        curr_dir = self.map[curr_row][curr_col]
        self.visited_states.clear()
        steps = 0
        max_steps = self.height * self.width * 4
        
        while steps < max_steps:
            state = (curr_row, curr_col, curr_dir)
            
            if state in self.visited_states:
                return False
                
            self.visited_states.add(state)
            next_row, next_col, next_dir, hit_wall, out_of_bounds = self.get_next_position(curr_row, curr_col, curr_dir)
            
            if out_of_bounds:
                # Count unique positions from states - just take row,col from the (row,col,dir) tuples
                unique_positions = {(state[0], state[1]) for state in self.visited_states}
                return len(unique_positions)
                
            if hit_wall:
                curr_dir = next_dir
            else:
                curr_row, curr_col = next_row, next_col
                curr_dir = next_dir
            
            steps += 1
            
        raise RuntimeError(f"Exceeded maximum steps ({max_steps})")
