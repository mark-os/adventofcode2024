import os


def calculate_safe(nums):
    pairs = list(zip(nums, nums[1:]))
    if not pairs:  # Handle lists with 0 or 1 elements
        return True
    directions = [b > a for a, b in pairs]
    diffs = [abs(b - a) for a, b in pairs]
    return all(0 < d <= 3 for d in diffs) and all(d1 == d2 for d1, d2 in zip(directions, directions[1:]))

def process_reports():
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

    return {"part1": original_safe_reports, "part2": dampened_safe_reports}

