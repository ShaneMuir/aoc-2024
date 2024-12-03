from aocd import get_data, submit

data = get_data(day=2, year=2024)


def is_safe(report):
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]

    all_increasing = all(1 <= diff <= 3 for diff in differences)
    all_decreasing = all(-3 <= diff <= -1 for diff in differences)

    # Return True if the report is safe
    return all_increasing or all_decreasing


def part_one():
    # Parse the input into a list of reports
    reports = [list(map(int, line.split())) for line in data.strip().splitlines()]

    safe_count = sum(1 for report in reports if is_safe(report))

    return safe_count


submit(part_one(), part='a', day=2, year=2024)