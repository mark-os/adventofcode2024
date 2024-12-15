import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, 'input')



DIRECTIONS = {
    '^': (-1, 0),  # up
    '>': (0, 1),   # right
    'v': (1, 0),   # down
    '<': (0, -1)   # left
}



def print_map(themap, visited, curr_pos=None):
    for r in range(len(themap)):
        for c in range(len(themap[0])):
            print(themap[r][c], end='')
        print()  # New line after each row
    print()  # Blank line after map

def walk_map(themap):
    # Find starting position and direction
    start_row = start_col = None
    for r in range(len(themap)):
        for c in range(len(themap[0])):
            if themap[r][c] in '^>v<':  # Changed from DIRECTIONS to actual characters
                start_row, start_col = r, c
                break
        if start_row is not None:
            break
            
    # Track visited positions and current state
    visited = {(start_row, start_col)}
    curr_row, curr_col = start_row, start_col
    curr_dir = themap[start_row][start_col]
    steps = 0
    
    # Simulate movement until leaving map
    while True:
        dr, dc = DIRECTIONS[curr_dir]
        next_row, next_col = curr_row + dr, curr_col + dc
        
        # Check if next move would leave map
        if (next_row < 0 or next_row >= len(themap) or 
            next_col < 0 or next_col >= len(themap[0])):
            break
            
        # Check if blocked
        if themap[next_row][next_col] == '#':
            # Turn right if blocked
            curr_dir = {'<': '^', '^': '>', '>': 'v', 'v': '<'}[curr_dir]
            themap[curr_row][curr_col] = curr_dir
        else:
            # Move forward if not blocked
            themap[curr_row][curr_col] = '.'  # Clear old position
            curr_row, curr_col = next_row, next_col
            themap[curr_row][curr_col] = curr_dir
            visited.add((curr_row, curr_col))
            steps += 1
            
        if steps > 10000:
            break
    return len(visited)


def test_position(themap, test_row, test_col, start_row, start_col, start_dir):
    height = len(themap)
    width = len(themap[0])
    curr_row, curr_col = start_row, start_col
    curr_dir = start_dir
    
    visited = set()
    steps = 0
    max_steps = height * width * 4

    while steps < max_steps:
        state = (curr_row, curr_col, curr_dir)
        if state in visited:
            return True
            
        visited.add(state)
        
        dr, dc = DIRECTIONS[curr_dir]
        next_row = curr_row + dr
        next_col = curr_col + dc
        
        # Combine all boundary checks
        if not (0 <= next_row < height and 0 <= next_col < width):
            return False
        
        # Check if we hit the test position or a wall
        if (next_row == test_row and next_col == test_col) or themap[next_row][next_col] == '#':
            curr_dir = {'<': '^', '^': '>', '>': 'v', 'v': '<'}[curr_dir]
        else:
            curr_row, curr_col = next_row, next_col
        
        steps += 1
    
    return False

def locate_loop_positions(themap):
    height = len(themap)
    width = len(themap[0])
    
    # Find starting position
    start_row = start_col = None
    for r in range(height):
        for c in range(width):
            if themap[r][c] in '^>v<':
                start_row, start_col = r, c
                start_dir = themap[r][c]
                break
        if start_row is not None:
            break

    loop_positions = []
    
    # Test each empty position
    for r in range(height):
        for c in range(width):
            if themap[r][c] == '.' and test_position(themap, r, c, start_row, start_col, start_dir):
                loop_positions.append((r, c))

    print("\nPositions that create loops when blocked:")
    for pos in loop_positions:
        print(f"Row: {pos[0]}, Col: {pos[1]}")

    return len(loop_positions)

if __name__ == '__main__':
    with open(input_path, 'r') as file:
        themap = [list(line.strip()) for line in file if line.strip()]
        mapcopy = [row[:] for row in themap]
        visited = walk_map(themap)
        print(f"Visited positions: {visited}")
        loop_positions = locate_loop_positions(mapcopy)
        print(f"Number of loop positions: {loop_positions}")


