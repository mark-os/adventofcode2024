import os
from walker import MapWalker
from loop_detector import LoopDetector

script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, 'input')

def print_map(themap):
    """Print the current state of the map."""
    for r in range(len(themap)):
        for c in range(len(themap[0])):
            print(themap[r][c], end='')
        print()  # New line after each row
    print()  # Blank line after map

if __name__ == '__main__':
    with open(input_path, 'r') as file:
        themap = [list(line.strip()) for line in file if line.strip()]
        
        # Part 1: Walk the map
        walker = MapWalker([row[:] for row in themap])
        visited_count = walker.walk()
        print(f"Visited positions: {visited_count}")
        
        # Part 2: Find loop positions
        detector = LoopDetector(themap)
        loop_positions = detector.find_loop_positions()
        print(f"Number of loop positions: {len(loop_positions)}")


