from walker import MapWalker

class LoopDetector:
    def __init__(self, themap):
        self.map = themap
        self.height = len(themap)
        self.width = len(themap[0])
        self.walker = MapWalker(themap)
        self.start_pos = self.walker._find_start()
        self.start_dir = self.map[self.start_pos[0]][self.start_pos[1]]
        self.known_loop_states = set()  # Cache of states known to be in loops

    def _make_state_key(self, row, col, direction):
        # Encode position and direction into a single integer
        dir_val = {'^': 0, '>': 1, 'v': 2, '<': 3}[direction]
        return (row << 10) | (col << 2) | dir_val
        
    def _find_start(self):
        for r in range(self.height):
            for c in range(self.width):
                if self.map[r][c] in '^>v<':
                    return (r, c)
        raise ValueError("No start position found")
        
    def test_position(self, test_row, test_col):
        curr_row, curr_col = self.start_pos
        curr_dir = self.start_dir
        visited = set()
        steps = 0
        max_steps = self.height * self.width * 4
        
        while steps < max_steps:
            state = self._make_state_key(curr_row, curr_col, curr_dir)
            
            if state in visited:
                return True
                
            visited.add(state)
            
            dr, dc = self.walker.DIRECTIONS[curr_dir]
            next_row = curr_row + dr
            next_col = curr_col + dc
            
            if not (0 <= next_row < self.height and 0 <= next_col < self.width):
                return False
            
            if (next_row == test_row and next_col == test_col) or self.map[next_row][next_col] == '#':
                curr_dir = self.walker.TURN_RIGHT[curr_dir]
            else:
                curr_row, curr_col = next_row, next_col
            
            steps += 1

        print(f"  Exceeded max steps ({max_steps})")
        return False
        
    def find_loop_positions(self):
        # First get the visited positions from an initial walk
        walker = MapWalker([row[:] for row in self.map])
        initial_visited = set()
        curr_row, curr_col = self.start_pos
        curr_dir = self.start_dir
        
        while True:
            dr, dc = walker.DIRECTIONS[curr_dir]
            next_row = curr_row + dr
            next_col = curr_col + dc
            
            # If we leave the map, break
            if not (0 <= next_row < self.height and 0 <= next_col < self.width):
                break
                
            if self.map[next_row][next_col] == '#':
                curr_dir = walker.TURN_RIGHT[curr_dir]
            else:
                initial_visited.add((next_row, next_col))
                curr_row, curr_col = next_row, next_col
        
        # Now only test positions that were visited
        loop_positions = []
        for r, c in initial_visited:
            if self.map[r][c] == '.' and self.test_position(r, c):
                loop_positions.append((r, c))
        
        return loop_positions
