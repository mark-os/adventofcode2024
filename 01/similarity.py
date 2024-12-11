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

similarity = 0

for i in column1:
    similarity += column2.count(i) * i

print(f"similarity score = {similarity}")