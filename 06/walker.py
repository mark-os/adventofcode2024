class MapWalker:
    DIRECTIONS = {
        '^': (-1, 0),  # up
        '>': (0, 1),   # right
        'v': (1, 0),   # down
        '<': (0, -1)   # left
    }
    
    TURN_RIGHT = {'<': '^', '^': '>', '>': 'v', 'v': '<'}

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

    def walk(self):
        curr_row, curr_col = self.start_pos
        curr_dir = self.map[curr_row][curr_col]
        visited = {(curr_row, curr_col)}
        
        while True:
            dr, dc = self.DIRECTIONS[curr_dir]
            next_row, next_col = curr_row + dr, curr_col + dc
            
            if not (0 <= next_row < self.height and 0 <= next_col < self.width):
                break
                
            if self.map[next_row][next_col] == '#':
                curr_dir = self.TURN_RIGHT[curr_dir]
                self.map[curr_row][curr_col] = curr_dir
            else:
                self.map[curr_row][curr_col] = '.'
                curr_row, curr_col = next_row, next_col
                self.map[curr_row][curr_col] = curr_dir
                visited.add((curr_row, curr_col))
                
        return len(visited)
