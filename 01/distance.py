import os

# Read the input file
script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, 'input')
with open(input_path, 'r') as file:
    # Initialize empty lists for both columns
    column1 = []
    column2 = []
    
    # Read each line and split into columns
    for line in file:
        num1, num2 = map(int, line.strip().split())
        column1.append(num1)
        column2.append(num2)

# Sort both lists
column1.sort()
column2.sort()

distance = 0

# Compare elements
for i in range(len(column1)):
    distance += abs(column1[i]-column2[i])

print(f"distance between the two lists: {distance}")    
