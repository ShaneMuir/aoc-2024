from aocd import get_data, submit

data = get_data(day=2, year=2024)


def is_safe(report):
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]

    all_increasing = all(1 <= diff <= 3 for diff in differences)
    all_decreasing = all(-3 <= diff <= -1 for diff in differences)

    # Return True if the report is safe
    return all_increasing or all_decreasing


def can_be_safe_with_removal(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_safe(modified_report):
            return True
    return False


def part_two():
    reports = [list(map(int, line.split())) for line in data.strip().splitlines()]

    safe_count = 0
    for report in reports:
        if is_safe(report) or can_be_safe_with_removal(report):
            safe_count += 1

    return safe_count


submit(part_two(), part='b', day=2, year=2024)