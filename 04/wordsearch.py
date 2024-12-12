import os

def read_grid(file):
    return [list(line.strip()) for line in file]

def search_word(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    matches = 0
    
    # All 8 directions: right, left, up, down, and 4 diagonals
    directions = [
        (0, 1),   # right
        (0, -1),  # left
        (-1, 0),  # up
        (1, 0),   # down
        (1, 1),   # down-right
        (-1, -1), # up-left
        (1, -1),  # down-left
        (-1, 1)   # up-right
    ]
    
    def check_direction(row, col, dx, dy):
        # Check if word can be found starting at (row,col) going in direction (dx,dy)
        if (row + dx * (len(word)-1) < 0 or 
            row + dx * (len(word)-1) >= rows or
            col + dy * (len(word)-1) < 0 or 
            col + dy * (len(word)-1) >= cols):
            return False
            
        for i in range(len(word)):
            if grid[row + dx * i][col + dy * i] != word[i]:
                return False
        return True

    # Try each starting position and direction
    for row in range(rows):
        for col in range(cols):
            for dx, dy in directions:
                if check_direction(row, col, dx, dy):
                    matches += 1
    return matches


def pattern_search(grid):
    rows = len(grid)
    cols = len(grid[0])
    matches = 0
    
    def check_for_pattern(row, col):
        # Need room for 3x3 pattern
        if (row + 2) >= rows or (col + 2) >= cols:
            return False
            
        # Check all 4 possible X patterns
        patterns = [
            # Pattern 1: M top-left and top-right
            lambda: (grid[row][col] == 'M' and
                    grid[row][col+2] == 'M' and
                    grid[row+1][col+1] == 'A' and
                    grid[row+2][col] == 'S' and
                    grid[row+2][col+2] == 'S'),
            # Pattern 2: M bottom-left and bottom-right
            lambda: (grid[row][col] == 'S' and
                    grid[row][col+2] == 'S' and
                    grid[row+1][col+1] == 'A' and
                    grid[row+2][col] == 'M' and
                    grid[row+2][col+2] == 'M'),
            # Pattern 3: M top-left and bottom-left  
            lambda: (grid[row][col] == 'M' and
                    grid[row+2][col] == 'M' and
                    grid[row+1][col+1] == 'A' and
                    grid[row][col+2] == 'S' and
                    grid[row+2][col+2] == 'S'),
            # Pattern 4: M top-right and bottom-right
            lambda: (grid[row][col] == 'S' and
                    grid[row+2][col] == 'S' and
                    grid[row+1][col+1] == 'A' and
                    grid[row][col+2] == 'M' and
                    grid[row+2][col+2] == 'M')
        ]
        
        return any(p() for p in patterns)

    # Try each starting position
    for row in range(rows):
        for col in range(cols):
            if check_for_pattern(row, col):
                matches += 1
                
    return matches

def main():
#     grid = """
# MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX
# """
#     grid = [list(line.strip()) for line in grid.strip().split('\n')]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, 'input')
    
    with open(input_path, 'r') as file:
        grid = read_grid(file)
        word = "XMAS"
        matches = search_word(grid, word)
        print(f"found the word {word} {matches} times")
    with open(input_path, 'r') as file:
        grid = read_grid(file)
        matches_2 = pattern_search(grid)
        print(f"found the special pattern {matches_2} times")

if __name__ == "__main__":
    main()
