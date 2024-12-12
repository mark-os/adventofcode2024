import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, 'input')
old_sum = 0
new_sum = 0
with open(input_path, 'r') as file:
    content = file.read()
    # Find all matches
    matches = re.finditer(r"mul\((\d+),(\d+)\)|(do(?:n't)?\(\))", content)
    op = "do()"
    for match in matches:
        if match.group(1):
            a = int(match.group(1))
            b = int(match.group(2))
            product = a*b
            old_sum += product
            if op == "do()":
                new_sum += product
        elif match.group(3):
            op = match.group(3)
            print(f"found op: {op}")

        print(f"Found match: {match.group(0)}, product: {product}")
    print(f"Old sum: {old_sum}")
    print(f"New sum: {new_sum}")
