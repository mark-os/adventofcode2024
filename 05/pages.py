import os
import re
from collections import defaultdict

script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, 'input')

def create_graph(rules, numbers):
    # Create adjacency list representation
    graph = defaultdict(list)
    for before, after in rules:
        if before in numbers and after in numbers:
            graph[before].append(after)
    return graph

def topological_sort(graph, numbers):
    # Keep track of visited nodes
    visited = set()
    # Keep track of nodes in current recursion stack
    temp = set()
    # Store the result
    order = []
    
    def visit(node):
        if node in temp:
            return False
        if node in visited:
            return True
            
        temp.add(node)
        for neighbor in graph[node]:
            if not visit(neighbor):
                return False
        temp.remove(node)
        visited.add(node)
        order.append(node)
        return True
    
    # Visit all nodes from the original list
    for node in numbers:
        if node not in visited:
            if not visit(node):
                return None
    
    return order[::-1]

def is_valid_order(lst, rules):
    for a, b in rules:
        try:
            if lst.index(a) > lst.index(b):
                return False
        except ValueError:
            continue
    return True
    
# example_input="""
# 47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13

# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47"""

with open(input_path, 'r') as file:
    content = file.read() #example_input
    top, bottom = content.strip().split('\n\n')
    rules = [(int(a), int(b)) for a, b in re.findall(r'(\d+)\|(\d+)', top)]
    lists = [list(map(int, line.split(','))) for line in bottom.split('\n') if line.strip()]
    part1 = 0
    part2 = 0

    for l in lists:
        print(f"checking {l}")
        # Part 1 - check if original order is valid
        valid = is_valid_order(l, rules)
        if valid:
            middle = l[len(l)//2]
            print(f"Original order valid, middle: {middle}")
            part1 += middle
            
        else:
            print(f"{l} failed rules, trying topological sort...")
            # Part 2 - find valid ordering using topological sort
            graph = create_graph(rules, l)
            ordered = topological_sort(graph, l)
            if ordered is not None:
                # Fill in any missing numbers that weren't in rules
                missing = [x for x in l if x not in ordered]
                # Add missing numbers to the end
                ordered.extend(missing)
                middle = ordered[len(ordered)//2]
                print(f"Found valid order: {ordered}, middle: {middle}")
                part2 += middle
            else:
                print(f"No valid ordering found for {l} (circular dependencies)")

    print(f"Part 1 (original valid lists middle sum): {part1}")
    print(f"Part 2 (all lists middle sum after reordering): {part2}")
