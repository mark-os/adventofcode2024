import os
from itertools import product
from typing import Union

# Operator constants
ADDITION = 0
MULTIPLICATION = 1
CONCATENATION = 2

OPERATORS = {
    ADDITION: "+",
    MULTIPLICATION: "*",
    CONCATENATION: "||"
}
def parse_equation(line: str) -> tuple[int, list[int]]:
    """Parse equation string into term and operands."""
    term, operands = line.split(':')
    return int(term), [int(x) for x in operands.split()]

def evaluate_expression(numbers: list[int], operators: tuple[int, ...]) -> int:
    """Evaluate expression with given numbers and operators."""
    result = numbers[0]
    for i, n in enumerate(numbers[1:], 1):
        op = operators[i-1]
        if op == ADDITION:
            result += n
        elif op == MULTIPLICATION:
            result *= n
        elif op == CONCATENATION:
            result = int(str(result) + str(n))
    return result

def check_equation(line: str, allow_concat: bool = True) -> Union[int, bool]:
    """
    Check if equation can be solved using available operators.
    
    Args:
        line: String in format "result: num1 num2 num3..."
        allow_concat: Whether to allow concatenation operator
    Returns:
        int: The term value if equation is solvable
        bool: False if equation cannot be solved
    """
    term, numbers = parse_equation(line)
    operators = [ADDITION, MULTIPLICATION]
    if allow_concat:
        operators.append(CONCATENATION)
        
    operator_sets = product(operators, repeat=len(numbers)-1)
    
    for operators in operator_sets:
        if evaluate_expression(numbers, operators) == term:
            return term
    return False


def main() -> None:
    """Main execution function."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, 'input')
    
    with open(input_path, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
        
        # Part 1: Without concatenation
        part1_sum = sum(t for line in lines if (t := check_equation(line, allow_concat=False)))
        print(f"Part 1: {part1_sum}")
        
        # Part 2: With concatenation
        part2_sum = sum(t for line in lines if (t := check_equation(line, allow_concat=True)))
        print(f"Part 2: {part2_sum}")

if __name__ == "__main__":
    main()

