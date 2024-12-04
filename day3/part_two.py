import re
from aocd import get_data, submit

data = get_data(day=3, year=2024)


def part_two():
    mul_pattern = r"mul\((\d+),(\d+)\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    mul_enabled = True
    total_sum = 0

    tokens = re.split(r"(mul\(\d+,\d+\)|do\(\)|don't\(\))", data)
    tokens = [token for token in tokens if token.strip()]  # Remove empty

    for token in tokens:
        if re.match(mul_pattern, token):
            if mul_enabled:
                x, y = map(int, re.findall(r"\d+", token))
                total_sum += x * y
        elif re.match(do_pattern, token):
            mul_enabled = True
        elif re.match(dont_pattern, token):
            mul_enabled = False

    return total_sum


submit(part_two(), part='b', day=3, year=2024)
