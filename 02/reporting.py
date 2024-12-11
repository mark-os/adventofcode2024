import os


def calculate_safe(number_list):
    # safe contitions
    # all increasing or all decreasing
    # increment from 1 to 3
    direction = ""
    is_safe = True
    for i, v in enumerate(number_list):
        if i > 0:
            diff = v - number_list[i-1]
        else:
            continue
        
        if not (0 < abs(diff) <= 3):
            is_safe = False
            break
            
        if diff > 0:  # increasing
            if direction == "dec":
                is_safe = False
                break
            direction = "inc"
        elif diff < 0:  # decreasing
            if direction == "inc":
                is_safe = False
                break
            direction = "dec"
    return is_safe

# Read the input file
script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, 'input')
with open(input_path, 'r') as file:
    original_safe_reports = 0
    dampened_safe_reports = 0
    for line in file:
        numbers = list(map(int, line.strip().split()))
        if calculate_safe(numbers):
            original_safe_reports += 1
            dampened_safe_reports += 1
            continue
        for i in range(len(numbers)):
            test = numbers.copy()
            test.pop(i)
            if calculate_safe(test):
                dampened_safe_reports += 1
                break

print(f"safe reports (original): {original_safe_reports}")
print(f"safe reports (dampened): {dampened_safe_reports}")
