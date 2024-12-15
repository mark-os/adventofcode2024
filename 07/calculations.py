import os
from itertools import product
OPERATORS = {0: "+", 1: "*", 2: "||"}
def check_equation(line):
    term, operands = line.split(':')
    numbers = [int(x) for x in operands.split()]
    term = int(term)
    operator_sets = [o for o in product([0,1,2], repeat=len(numbers)-1)]
    # 0 = + (addition)
    # 1 = * (multiplication)
    # 2 = || (concatenation)
    test_value = 0
    for s in operator_sets:
        for i,n in enumerate(numbers):
            # print(f"n: {n}, i: {i}, set: {s}")
            if i == 0:
                test_value = n
            else:
                operator = s[i-1]
                # print(f"next operand test: {OPERATORS[operator]}")
                if operator == 0:
                    test_value += n
                elif operator == 1:
                    test_value *= n
                elif operator == 2:
                    test_value = int(str(test_value)+str(n))
        # print(f"Term: {term}, Numbers: {numbers}, Test Value: {test_value}")
        if test_value == term:
            # print(f"success")
            return term
    return False


script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, 'input')
with open(input_path, 'r') as file:
    final_sum = 0
    lines = [line for line in file if line.strip()]
    for line in lines:
        if t := check_equation(line):
            final_sum += t
    print(f"final sum: {final_sum}")

