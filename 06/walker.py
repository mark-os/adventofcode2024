class MapWalker:
    DIRECTIONS = {
        '^': (-1, 0),  # up
        '>': (0, 1),   # right
        'v': (1, 0),   # down
        '<': (0, -1)   # left
    }
    
    TURN_RIGHT = {'<': '^', '^': '>', '>': 'v', 'v': '<'}

    def get_next_position(self, curr_row, curr_col, curr_dir, test_pos=None):
        """Returns (next_row, next_col, next_dir, hit_wall)"""
        dr, dc = self.DIRECTIONS[curr_dir]
        next_row = curr_row + dr
        next_col = curr_col + dc
        
        # Check boundaries - if we're about to leave the map, return that position
        if not (0 <= next_row < self.height and 0 <= next_col < self.width):
            return next_row, next_col, curr_dir, False
            
        # Check for wall or test position
        if (test_pos and (next_row, next_col) == test_pos) or self.map[next_row][next_col] == '#':
            return curr_row, curr_col, self.TURN_RIGHT[curr_dir], True
            
        return next_row, next_col, curr_dir, False

    def __init__(self, themap):
        self.map = themap
        self.height = len(themap)
        self.width = len(themap[0])
        self.start_pos = self._find_start()
        
    def _find_start(self):
        for r in range(self.height):
            for c in range(self.width):
                if self.map[r][c] in '^>v<':
                    return (r, c)
        raise ValueError("No start position found")

    def _make_state_key(self, row, col, direction):
        # Encode position and direction into a single integer
        dir_val = {'^': 0, '>': 1, 'v': 2, '<': 3}[direction]
        return (row << 10) | (col << 2) | dir_val

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
        visited_states = set()
        steps = 0
        max_steps = self.height * self.width * 4
        
        while steps < max_steps:
            state = self._make_state_key(curr_row, curr_col, curr_dir)
            
            if state in visited_states:
                return False
                
            visited_states.add(state)
            next_row, next_col, next_dir, hit_wall = self.get_next_position(curr_row, curr_col, curr_dir)
            
            if not (0 <= next_row < self.height and 0 <= next_col < self.width):
                # Count unique positions from states
                unique_positions = {(state >> 10, (state >> 2) & 0xFF) for state in visited_states}
                return len(unique_positions)
                
            if hit_wall:
                curr_dir = next_dir
                self.map[curr_row][curr_col] = curr_dir
            else:
                self.map[curr_row][curr_col] = '.'
                curr_row, curr_col = next_row, next_col
                curr_dir = next_dir
                self.map[curr_row][curr_col] = curr_dir
            
            steps += 1
            
        raise RuntimeError(f"Exceeded maximum steps ({max_steps})")
