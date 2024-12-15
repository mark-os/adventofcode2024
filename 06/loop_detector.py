from walker import MapWalker

class LoopDetector:
    def __init__(self, themap):
        self.map = themap
        self.height = len(themap)
        self.width = len(themap[0])
        self.start_pos = self._find_start()
        self.start_dir = self.map[self.start_pos[0]][self.start_pos[1]]
        
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
        max_steps = self.height * self.width * 4
        steps = 0
        
        while steps < max_steps:
            state = (curr_row, curr_col, curr_dir)
            if state in visited:
                return True
                
            visited.add(state)
            dr, dc = MapWalker.DIRECTIONS[curr_dir]
            next_row = curr_row + dr
            next_col = curr_col + dc
            
            if not (0 <= next_row < self.height and 0 <= next_col < self.width):
                return False
            
            if (next_row == test_row and next_col == test_col) or self.map[next_row][next_col] == '#':
                curr_dir = MapWalker.TURN_RIGHT[curr_dir]
            else:
                curr_row, curr_col = next_row, next_col
            
            steps += 1
        
        return False
        
    def find_loop_positions(self):
        loop_positions = []
        for r in range(self.height):
            for c in range(self.width):
                if self.map[r][c] == '.' and self.test_position(r, c):
                    loop_positions.append((r, c))
        return loop_positions
