from aocd import get_data, submit

data = get_data(day=1, year=2024)


def part_one():
    # Parse the input into two lists
    left_list = []
    right_list = []

    # Each line contains two numbers separated by whitespace
    for line in data.strip().splitlines():
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

    # Sort both lists
    left_list.sort()
    right_list.sort()

    # Calculate the total distance
    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))

    return total_distance


submit(part_one(), part='a', day=1, year=2024)
