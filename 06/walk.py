import os
from walker import MapWalker

script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, 'input')

def find_loop_positions(themap, initial_walker):
    """Find all positions that, when treated as walls, create loops in the path."""
    loop_positions = []
    
    # Test each visited position
    for r, c in {(state[0], state[1]) for state in initial_walker.visited_states}:
        if themap[r][c] == '.':
            # Create new map with test position as wall
            test_map = [row[:] for row in themap]
            test_map[r][c] = '#'
            walker = MapWalker(test_map)
            
            # Create a walker with the test position
            try:
                if walker.walk() is False:
                    loop_positions.append((r, c))
            except RuntimeError:
                continue  # Skip positions that cause too many steps
                
    return loop_positions

def main():
    with open(input_path, 'r') as file:
        themap = [list(line.strip()) for line in file if line.strip()]
        
        # Part 1: Walk the map
        walker = MapWalker([row[:] for row in themap])
        visited_count = walker.walk()
        print(f"Visited positions: {visited_count}")
        
        # Part 2: Find loop positions
        loop_positions = find_loop_positions(themap, walker)
        print(f"Number of loop positions: {len(loop_positions)}")

if __name__ == '__main__':
    main()

