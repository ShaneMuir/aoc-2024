from collections import Counter
from aocd import get_data, submit

# Get the data from the AoC API
data = get_data(day=1, year=2024)


def part_two():
    # Parse the input into two lists
    left_list = []
    right_list = []

    # Each line contains two numbers separated by whitespace
    for line in data.strip().splitlines():
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

    # Count occurrences of each number in the right list
    right_count = Counter(right_list)

    # Calculate the similarity score
    similarity_score = 0
    for number in left_list:
        similarity_score += number * right_count[number]

    return similarity_score


submit(part_two(), part='b', day=1, year=2024)
