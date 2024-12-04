from aocd import get_data, submit
import re

data = get_data(day=3, year=2024)


def part_one():
    # Regular expression to match valid mul(X,Y) instructions
    pattern = r"mul\((\d+),(\d+)\)"

    matches = re.findall(pattern, data)

    # Calculate the sum of the results of the multiplications
    total = sum(int(x) * int(y) for x, y in matches)

    return total


submit(part_one(), part='a', day=3, year=2024)
